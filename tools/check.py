#!/usr/bin/env python3
"""check.py — the REVENUE continuity linter.

    python3 tools/check.py                      # lint manuscript/ (all three build targets)
    python3 tools/check.py file.md ...          # lint specific manuscript/ or docs/ files
    python3 tools/check.py --md                 # emit findings as a markdown table
    python3 tools/check.py --all                # include docs/ (outline + bibles) in the sweep
    python3 tools/check.py --stats              # Pass-4 audit: the tic count, dash and filter budgets

Exit codes: 0 clean or warnings only · 1 a BAN hit (a BAN fails all three builds) · 2 usage error.

Design rule: **the linter is generated from the prose.** The ban list is parsed from the `lexicon`
fence in docs/bibles/vocabulary-tone-bible.md §7, so editing that table edits the check — the
house's answer to "the bibles and the draft drift apart." Continuity anchors are the small set of
facts canon §10 says are mechanically checkable. Style Guide §6.1.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
DOCS = ROOT / "docs"
LEXICON_DOC = DOCS / "bibles" / "vocabulary-tone-bible.md"

DASH = "[—–]"
ROW = re.compile(r"^\|\s*(BAN|FLAG|NOTE|TIC)\s*\|(.+?)\|\s*([^|]*?)\s*\|\s*$")


# --------------------------------------------------------------------------
# 1. the lexicon, read from the bible
# --------------------------------------------------------------------------

def parse_lexicon(path: Path):
    """Rows `| SEVERITY | regex | note |` inside a ```lexicon fence. The note becomes the rule
    name (so notes must be unique). Returns (rules, source_name)."""
    rules, src = [], path.name
    in_block = False
    for line in path.read_text(encoding="utf-8").splitlines():
        ln = line.strip()
        if ln.startswith("```lexicon"):
            in_block = True
            continue
        if in_block and ln.startswith("```"):
            in_block = False
            continue
        if not in_block:
            continue
        m = ROW.match(ln)
        if not m:
            continue
        sev, pat, note = m.group(1).upper(), m.group(2).strip(), m.group(3).strip()
        try:
            rx = re.compile(pat)
        except re.error as e:
            print(f"  ! bad regex in {src} ({pat}): {e}", file=sys.stderr)
            continue
        slug = "-".join(re.findall(r"[A-Za-z0-9]+", note)[:5]).lower() or pat[:16]
        rules.append({"severity": sev, "name": f"lex:{slug}", "pattern": rx,
                      "note": f"{note}  (rule from {src})", "message": note, "starts_with": [],
                      "in_dialogue": sev != "NOTE"})
    seen = {}
    for r in rules:
        seen[r["name"]] = r
    return list(seen.values()), src


# Structure rules can't be expressed as one regex row, so they live here.
BUILTIN = [
    {"severity": "FLAG", "name": "chapter-heading-numbering",
     "pattern": re.compile(r"^##\s+(?!Chapter\s+\d+:)(.+)$"),
     "starts_with": ["## "], "in_dialogue": False, "note": "chapter H2 must be '## Chapter N: Title' (manuscript convention)"},
    {"severity": "NOTE", "name": "chapter-heading-wrong-number",
     "pattern": re.compile(r"^##\s+Chapter\s+(\d+):"),
     "starts_with": ["## "], "in_dialogue": False, "note": "chapter number in the heading must match the filename prefix"},
    {"severity": "FLAG", "name": "scene-break-form",
     "pattern": re.compile(r"^\s*(\*\s*\*\s*\*|\*\*\*|~~~|…)\s*$"),
     "starts_with": [], "in_dialogue": False, "note": "scene break must be a bare '---' line; compile.py turns it into a centered asterism"},
    {"severity": "FLAG", "name": "age-drift",
     "pattern": re.compile(r"\b(Jacob|Joshua|Matthew|Caleb|Parrish|Harper)\b[^.]{0,40}?\(\s*(\d{2})\s*\)"),
     "starts_with": [], "in_dialogue": True, "note": "age in prose must match canon §10 (resolve Q-3, then update the table)"},
    {"severity": "NOTE", "name": "bare-age-in-prose",
     "pattern": re.compile(r"\b(?:aged|a man of|a woman of)\s+\d{2}\b"),
     "starts_with": [], "in_dialogue": True, "note": "ages are stage directions; convert to a fact about work or debt (canon R-1)"},
]

CANON_AGES = {"Jacob": 47, "Joshua": 45, "Matthew": 19, "Caleb": 21, "Harper": 60}


# --------------------------------------------------------------------------
# 2. narration vs. dialogue (Guide §4 Pass 3: ban lists apply to narration, not character speech)
# --------------------------------------------------------------------------

def strip_dialogue(text: str) -> str:
    """Blank out quoted speech, keeping line structure so line numbers stay usable."""
    out, keep = [], True
    for line in text.splitlines():
        buf, i = [], 0
        while i < len(line):
            ch = line[i]
            if ch in "“\"":
                close = "”" if ch == "“" else '"'
                j = line.find(close, i + 1)
                if j == -1:                       # run-on speech to end of line
                    buf.append(" " * (len(line) - i)); break
                buf.append(" " * (j - i + 1)); i = j
            else:
                buf.append(ch)
            i += 1
        out.append("".join(buf))
        i = 0
    return "\n".join(out)


def is_dialogue(line: str, fmt: str) -> bool:
    s = line.lstrip()
    if fmt == "play":
        return bool(re.match(r"^[A-Z][A-Z .']{2,}:", s))
    return s.startswith(('"', "“"))


def narration_lines(text: str, fmt: str):
    """Yield (lineno, line) for prose only — fenced code (the linter's own lexicon block), headings,
    tables, stage directions and quoted speech are excluded, per the style guide's split between
    narration and character voice."""
    in_fence = False
    for n, line in enumerate(text.splitlines(), 1):
        st = line.strip()
        if st.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not st:
            continue
        if st.startswith(("---", "***")) or st.startswith("|") or st.startswith("```"):
            continue
        if fmt == "play":
            if re.match(r"^\[.*\]\s*$", st) or st.startswith(("**SETTING", "**TIME", "**STATUS")):
                continue
            if is_dialogue(st, fmt):
                continue
        else:
            if st.startswith("#"):
                if "Act" in st:
                    yield n, st
                continue
            if '"' in st or "“" in st:
                continue
        yield n, line


# --------------------------------------------------------------------------
# 3. the lint
# --------------------------------------------------------------------------

class Hit:
    __slots__ = ("file", "line", "severity", "name", "excerpt", "note")

    def __init__(self, file, line, severity, name, excerpt, note):
        self.file, self.line, self.severity = file, line, severity
        self.name, self.excerpt, self.note = name, excerpt, note


def lint(relname: str, text: str, fmt: str, rules) -> list:
    hits = []
    for n, line in narration_lines(text, fmt):
        for r in rules:
            if r.get("starts_with") and not any(line.lstrip().startswith(p) for p in r["starts_with"]):
                continue
            m = r["pattern"].search(line)
            if not m:
                continue
            if m:
                lo = max(0, m.start() - 30)
                exc = line[lo:m.end() + 40].strip()
                hits.append(Hit(relname, n, r["severity"], r["name"], exc, r.get("note") or r.get("message", "")))
    # duplicate act titles — a real bug in the outline, and a build failure for us
    acts = re.findall(r"^#\s*Act\s+([IVX]+|[A-Z][a-z]+)\s*[:—–-]\s*(.+?)\s*$", text, re.M | re.I)
    seen = {}
    for tag, title in acts:
        key = title.strip().upper().strip(":")
        if key in seen:
            hits.append(Hit(relname, 0, "BAN", "act-title-unique",
                            f"Act {tag}: '{title}' repeats Act {seen[key]}", "every act title unique — canon §10"))
        seen[key] = tag
    for name, age in CANON_AGES.items():
        for m in re.finditer(rf"\b{name}\b[^.\n]{{0,40}}?\((\d{{2}})\)", text):
            if int(m.group(1)) != age:
                hits.append(Hit(relname, text[:m.start()].count("\n") + 1, "FLAG", "canon-age-table",
                                m.group(0), f"canon §10 has {name} at {age} in 1878 — resolve Q-3"))
    return hits


# --------------------------------------------------------------------------
# 4. Pass-4 audit
# --------------------------------------------------------------------------

TIC = re.compile(rf"(?:is|was|were|are|’s|'s)\s*not\b[^.!?\n]{{1,110}}?[—–]\s*(?:it(?:’|')?s|he|she|they|this|that|it)\b[^.!?\n]{{0,60}}?\b(just|only|what|because|who|not)\b|{DASH}\s*not\s+\w+[^.!?\n]{{0,60}}?[—–;]\s*(?:it(?:’|')?s|this is|that (?:was|is))[^.!?\n]{{0,50}}?\b(just|only|what|because|who)\b|(?:^|[.!?]\s)(?:[Ii]t|[Tt]his|[Tt]hat)\s*(?:’s|'s|is|was)?\s*not\b[^.!?\n]{{1,110}}?[—–;]\s*(?:[Ii]t|[Tt]his|[Tt]hat)\s*(?:’s|'s|is|was)\b[^.!?\n]{{0,60}}?\b(just|only|what|because|who)\b", re.M)
FILTER_WORDS = r"thought|knew|understood|realized|noticed|saw|heard|felt|remembered|was aware|could (?:see|hear|feel)"
CRUTCH = r"\bjust\b|\bsimply\b|\bvery\b"


def audit(relname: str, text: str) -> dict:
    plain = strip_dialogue(text)
    narr = "\n".join(l for _, l in narration_lines(plain, "md"))
    words = len(re.findall(r"[A-Za-z0-9’']+", plain))
    d = plain.count("—") + plain.count("–")
    ticks = len(TIC.findall(narr)) + len(TIC.findall(text)) // 2
    filt = len(re.findall(rf"\b(?:{FILTER_WORDS})\b", narr, re.I))
    return {
        "file": relname, "words": words, "em_dash": d,
        "em_dash_per_1k": round(1000 * d / max(1, words), 1),
        "tic": ticks, "tic_budget": 2,
        "filter_words": filt, "filter_per_1k": round(1000 * filt / max(1, words), 2),
        "crutch": {c: len(re.findall(c, narr, re.I)) for c in (r"just", r"simply", r"very")},
    }


# --------------------------------------------------------------------------

def load_corpus(args):
    files = []
    if args.paths:
        for p in args.paths:
            path = Path(p) if Path(p).is_absolute() else ROOT / p
            if path.is_dir():
                files += sorted(path.glob("*.md"))
            elif path.exists():
                files.append(path)
            else:
                print(f"no such file: {path}", file=sys.stderr); sys.exit(2)
    else:
        if MANUSCRIPT.is_dir():
            files += sorted(MANUSCRIPT.glob("*.md"))
        if args.all:
            # Bibles and the style guide quote banned words on purpose — they are the rule
            # source, not the object of the check. Pass --meta to lint them anyway.
            for f in sorted(DOCS.glob("*.md")) + sorted((DOCS / "bibles").glob("*.md")):
                if not args.meta and re.search(r"(bible|style-guide|period-audit|beta-reader)", f.name):
                    continue
                files.append(f)
    out = []
    for f in files:
        if f.name.lower() in ("readme.md",):
            continue
        fmt = "md"
        text = f.read_text(encoding="utf-8")
        if re.search(r"^\*\*SETTING:\*\*|^\[[A-Z0-9 .,'\-–—]+\]", text, re.M):
            fmt = "play"
        out.append((str(f.relative_to(ROOT)), text, fmt))
    if not out:
        print("no manuscript/*.md yet — create manuscript/NN-slug.md files to lint.", file=sys.stderr)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="REVENUE continuity linter")
    ap.add_argument("paths", nargs="*", help="files to lint (default: manuscript/*.md)")
    ap.add_argument("--md", action="store_true", help="markdown table output")
    ap.add_argument("--all", action="store_true", help="also sweep docs/ (outline, gaps, pitch)")
    ap.add_argument("--meta", action="store_true", help="with --all: include the bibles themselves")
    ap.add_argument("--stats", action="store_true", help="print the Pass-4 audit")
    args = ap.parse_args(argv)

    rules, lexsrc = parse_lexicon(LEXICON_DOC)
    rules = rules + BUILTIN
    corpus = load_corpus(args)
    if not corpus:
        return 0

    findings, audits = [], []
    for name, text, fmt in corpus:
        findings += lint(name, text, fmt, rules)
        audits.append(audit(name, text))

    order = {"BAN": 0, "FLAG": 1, "NOTE": 2}
    findings.sort(key=lambda h: (order.get(h.severity, 3), h.file, h.line))

    if args.md:
        print("| sev | rule | file:line | excerpt | note |")
        print("|---|---|---|---|---|")
        for h in findings:
            print(f"| {h.severity} | {h.name} | {h.file}:{h.line} | `{h.excerpt[:90]}` | {h.note} |")
    else:
        cur = None
        for h in findings:
            if h.file != cur:
                cur = h.file
                print(f"\n── {cur} ──")
            print(f"[{h.severity}] {h.name}  line {h.line}\n      …{h.excerpt[:150]}…\n      → {h.note}")
        if not findings:
            print("no findings — manuscript is clean against the lexicon.")

    if args.stats:
        tot = {k: sum(a[k] for a in audits) for k in ("words", "em_dash", "tic", "filter_words")}
        print(f"\nPass-4 audit  ({len(audits)} file(s), lexicon from {lexsrc})")
        print(f"  words (plain text)        : {tot['words']:,}")
        print(f"  'not X — it's Y'          : {tot['tic']}   budget {2 * len(audits)} over this corpus (2 for the whole book)")
        print(f"  em dashes                 : {tot['em_dash']}  ({round(1000*tot['em_dash']/max(1,tot['words']),1)} per 1k; target ≤6 for narration)")
        print(f"  filter words in narration : {tot['filter_words']}  ({round(1000*tot['filter_words']/max(1,tot['words']),2)} per 1k; budget <1.0)")
        for key in ("just", "simply", "very"):
            n = sum(a["crutch"][key] for a in audits)
            if n:
                print(f"    {key:<10} {n}")
        for a in audits:
            if a["tic"] > 2 or a["filter_per_1k"] > 1.0:
                print(f"    · {a['file']}: tic {a['tic']}, filters/1k {a['filter_per_1k']}")

    counts = {s: sum(1 for h in findings if h.severity == s) for s in ("BAN", "FLAG", "NOTE")}
    print(f"\n{len(corpus)} file(s), {sum(a['words'] for a in audits):,} words — "
          f"{counts['BAN']} BAN, {counts['FLAG']} FLAG, {counts['NOTE']} NOTE"
          + ("  ✗ build blocked" if counts["BAN"] else "  ✓ clean"))
    return 1 if counts["BAN"] else 0


if __name__ == "__main__":
    sys.exit(main())

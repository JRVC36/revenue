#!/usr/bin/env python3
"""readability.py — narration-only sentence and syllable diagnostics for *REVENUE*.

Implements Style Guide §3.3 (bimodal rhythm) and §3.2 (legible vs. opaque difficulty).
Dialogue is excluded: only narration is scored, because only narration carries the
sentence-music ruling (canon §8.4: long periodic sentences for night/wait/landscape,
4-12-word declaratives for work and crisis).

    python3 tools/readability.py                 # per-chapter report for manuscript/
    python3 tools/readability.py file.md ...     # specific files
    python3 tools/readability.py --csv           # machine-readable
    python3 tools/readability.py --long 38       # flag sentences longer than N words

Python 3.9+ standard library only.
"""
from __future__ import annotations

import argparse
import csv
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"

# Opaque difficulty (Guide 3.2): distance to the grammatical subject, stacked -ing,
# abstract nouns that explain an image after the image landed.
HEDGE = re.compile(r"\b(kind of|sort of|in a way that|something that was not quite|"
                   r"the particular \w+ of|a sense that|as if somehow)\b", re.I)
ING_STACK = re.compile(r"\w+ing\b[^.,;]{0,60},\s*\w+ing\b[^.,;]{0,60},\s*\w+ing\b", re.I)
THESIS_NOUN = re.compile(r"\b(claim|dignity|justice|honor|freedom|pride|respect|reckoning|"
                         r"tragedy|legacy|memory|identity|the old economy|collective injury)\b", re.I)
FILTER = re.compile(r"\b(thought|knew|understood|realized|noticed|saw|heard|felt|"
                    r"remembered|was aware|could (?:see|hear|feel))\b", re.I)
LATIN_TAIL = re.compile(r"\b\w{8,}\b")

VOWELS = "aeiouy"


def syllables(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")):
        w = w[:-1]
    count, prev_v = 0, False
    for ch in w:
        is_v = ch in VOWELS
        if is_v and not prev_v:
            count += 1
        prev_v = is_v
    return max(1, count)


def narration_only(text: str) -> str:
    """Drop scene/act headings, markdown, and quoted speech."""
    out = []
    for line in text.splitlines():
        if line.startswith(("#", ">", "|", "---", "*   *   *")):
            continue
        line = re.sub(r"[*_`]", "", line)
        line = re.sub(r"[“\"].*?[”\"]", " ", line)          # balanced quotes
        line = re.sub(r"[“\"].*$", " ", line)                 # unbalanced run-on speech
        out.append(line)
    return "\n".join(out)


def sentences(text: str):
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?…])\s+", text) if len(re.findall(r"[A-Za-z]+", s)) > 1]


def score(name: str, text: str, long_limit: int):
    sents = sentences(narration_only(text))
    lengths = [len(re.findall(r"[A-Za-z’']+", s)) for s in sents]
    if not lengths:
        return None
    words = sum(lengths)
    syls = sum(syllables(w) for w in re.findall(r"[A-Za-z’']+", " ".join(sents)))
    long_periodic = [s for s, n in zip(sents, lengths) if 25 <= n <= 45]
    clipped = [s for s, n in zip(sents, lengths) if 4 <= n <= 12]
    over = [s for s, n in zip(sents, lengths) if n > long_limit]
    joined = " ".join(sents)
    return {
        "chapter": name,
        "narration_words": words,
        "sentences": len(sents),
        "mean_len": round(words / len(sents), 1),
        "median_len": int(statistics.median(lengths)),
        "pct_long_25_45": round(100 * len(long_periodic) / len(sents), 1),
        "pct_short_4_12": round(100 * len(clipped) / len(sents), 1),
        "syll_per_word": round(syls / max(1, words), 2),
        "latinate_over_8": round(100 * len(re.findall(r"\b\w{9,}\b", joined)) / max(1, words), 2),
        "filter_words_per_1k": round(1000 * len(FILTER.findall(joined)) / max(1, words), 2),
        "hedges": len(HEDGE.findall(joined)),
        "ing_stacks": len(ING_STACK.findall(joined)),
        "thesis_nouns": len(THESIS_NOUN.findall(joined)),
        "over_long": len(over),
        "worst_sentence": max(sents, key=lambda s: len(re.findall(r"[A-Za-z’']+", s)))[:150] if over else "",
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="narration readability for REVENUE")
    ap.add_argument("paths", nargs="*", help="markdown files (default: manuscript/*.md)")
    ap.add_argument("--csv", action="store_true")
    ap.add_argument("--long", type=int, default=48, help="flag sentences longer than N words")
    args = ap.parse_args(argv)

    if args.paths:
        files = []
        for p in args.paths:
            path = Path(p) if Path(p).is_absolute() else ROOT / p
            files += sorted(path.glob("*.md")) if path.is_dir() else [path]
    else:
        files = sorted(MANUSCRIPT.glob("*.md"))
    files = [f for f in files if f.is_file() and f.name.lower() != "readme.md"]
    if not files:
        print("no manuscript files found — nothing to score yet.", file=sys.stderr)
        return 0

    rows = [r for r in (score(f.stem, f.read_text(encoding="utf-8"), args.long) for f in files) if r]
    if not rows:
        print("no scorable narration.", file=sys.stderr)
        return 0

    if args.csv:
        w = csv.DictWriter(sys.stdout, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
        return 0

    hdr = (f"{'chapter':<34}{'words':>7}{'sent':>6}{'mean':>6}{'med':>5}"
           f"{'>=25w':>7}{'4-12w':>7}{'syl/w':>7}{'filt/k':>8}{'ing^3':>7}{'thesis':>7}")
    print(hdr); print("-" * len(hdr))
    for r in rows:
        print(f"{r['chapter'][:33]:<34}{r['narration_words']:>7}{r['sentences']:>6}{r['mean_len']:>6}"
              f"{r['median_len']:>5}{r['pct_long_25_45']:>7}{r['pct_short_4_12']:>7}"
              f"{r['syll_per_word']:>7}{r['filter_words_per_1k']:>8}{r['ing_stacks']:>7}{r['thesis_nouns']:>7}")
    print("-" * len(hdr))
    mean_of = lambda k: round(statistics.mean(r[k] for r in rows), 2) if len(rows) > 1 else rows[0][k]
    print(f"book means — median sentence {mean_of('median_len')} · long {mean_of('pct_long_25_45')}% · "
          f"clipped {mean_of('pct_short_4_12')}% · syllables/word {mean_of('syll_per_word')} · "
          f"filter words/1k {mean_of('filter_words_per_1k')}")

    print("\nRules being enforced (Guide §3.2–3.3 + canon §8.4):")
    bad = 0
    for r in rows:
        notes = []
        if 13 <= r["median_len"] <= 24:
            notes.append(f"median {r['median_len']} words is the dead middle — commit to periodic or clipped")
        if r["pct_long_25_45"] < 8:
            notes.append("no landscape/procedural long sentence band")
        if r["pct_short_4_12"] < 15:
            notes.append("crisis beats are not being shortened")
        if r["filter_words_per_1k"] > 1.0:
            notes.append("Pass-3 filter words over budget")
        if r["hedges"] or r["ing_stacks"]:
            notes.append(f"opaque difficulty: {r['hedges']} hedges, {r['ing_stacks']} stacked -ing")
        if r["thesis_nouns"]:
            notes.append(f"{r['thesis_nouns']} thesis nouns — Pass 2 cut")
        if r["over_long"]:
            notes.append(f"{r['over_long']} sentence(s) over {args.long} words")
        if notes:
            bad += 1
            print(f"  {r['chapter']}: " + "; ".join(notes))
            if r["worst_sentence"]:
                print(f"      longest: {r['worst_sentence']}…")
    if not bad:
        print("  none — every chapter is bimodal and unhedged")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""compile.py — build *REVENUE* from manuscript/ into dist/.

Three outputs, per Style Guide §6.2 and §6.3:
  dist/revenue.md            concatenated book (front matter, Contents, acts, chapters)
  dist/revenue.html          typeset HTML for Google Docs import (Georgia, page architecture,
                             [[PAGE_BREAK]] tokens, centered asterisms, book indentation)
  dist/revenue-audiobook.txt Kokoro TTS script (no markup, dashes converted by syntactic
                             context, abbreviations and all digits expanded to words)

    python3 tools/compile.py                 # build all three
    python3 tools/compile.py --only html     # one target (md|html|audiobook)
    python3 tools/compile.py --title "REVENUE" --author "Kevin Russell"

Python 3.9+ standard library only.

Note on the Docs side-effects the Guide requires: the importer mangles
`font-family: 'Georgia', serif` into the web font Geo, so we emit bare Georgia and the
caller must follow upload with a document-wide updateTextStyle (weightedFontFamily: Georgia)
and convert every [[PAGE_BREAK]] token into a true insertPageBreak in REVERSE index order.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "manuscript"
DIST = ROOT / "dist"
PAGE_BREAK = "[[PAGE_BREAK]]"
ASTERISM = "*   *   * "

ACTS = {"one": "I", "two": "II", "three": "III", "four": "IV", "five": "V"}

UNITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
         "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
         "nineteen"]
TENS = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def words_1_999(n: int) -> str:
    if n < 20:
        return UNITS[n]
    if n < 100:
        t, u = divmod(n, 10)
        return TENS[t] + ("" if not u else "-" + UNITS[u])
    h, r = divmod(n, 100)
    out = (UNITS[h] + " hundred") if h else ""
    if r:
        out += (" and " if out else "") + words_1_999(r)
    return out


def year_words(n: int) -> str:
    """1879 -> eighteen seventy-nine ; 1802 -> eighteen oh-two ; 1900 -> nineteen hundred."""
    if not 1000 <= n <= 9999:
        return number_words(n)
    hi, lo = divmod(n, 100)
    if lo == 0:
        return f"{words_1_999(hi)} hundred"
    if 1 <= lo <= 9:
        return f"{words_1_999(hi)} oh-{UNITS[lo]}"
    return f"{words_1_999(hi)} {words_1_999(lo)}"


def number_words(n: int) -> str:
    if n < 0:
        return "minus " + number_words(-n)
    if n < 1000:
        return words_1_999(n)
    out, rest = [], n
    for scale, val in (("thousand", 1000), ("million", 1_000_000)):
        if rest >= val:
            c, rest = divmod(rest, val)
            out.append(f"{words_1_999(c)} {scale}")
    if rest:
        out.append(words_1_999(rest))
    return " ".join(out)


# --------------------------------------------------------------------------
# manuscript parsing
# --------------------------------------------------------------------------

def load_chapters():
    """Chapter files are NN-slug.md; the number orders the book and names the chapter."""
    chapters = []
    for path in sorted(SRC.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        m = re.match(r"^(\d+)-(.+)\.md$", path.name)
        if not m:
            print(f"  ! skipping {path.name}: expected NN-slug.md", file=sys.stderr)
            continue
        num, slug = int(m.group(1)), m.group(2).replace("-", " ")
        body = path.read_text(encoding="utf-8").strip()
        # a file may carry its own H2; otherwise derive it from the filename
        head = re.search(r"^##\s+(.+?)\s*$", body, re.M)
        title = head.group(1) if head else f"Chapter {num}: {slug.title()}"
        if head:
            body = (body[:head.start()] + body[head.end():]).lstrip("\n")
        if not re.match(r"^Chapter\s+\d+:", title):
            title = f"Chapter {num}: {title}"
        chapters.append({"num": num, "path": path, "title": title, "body": body})
    return chapters


def split_acts(chapters):
    """An act is declared inside a chapter file by '# Act Two: The Reckoning' or inherited."""
    acts, current = [], {"name": None, "sub": "", "chapters": []}
    for ch in chapters:
        m = re.search(r"^#\s*Act\s+([IVX]+|One|Two|Three|Four)\s*[:—–-]\s*(.+?)\s*$",
                      ch["body"], re.M | re.I)
        if m:
            nm = m.group(1).title()
            nm = ACTS.get(nm.lower(), nm)
            if current["chapters"]:
                acts.append(current)
            current = {"name": nm, "sub": m.group(2), "chapters": []}
            ch["body"] = re.sub(r"^#\s*Act\s+.*$", "", ch["body"], count=1, flags=re.M).strip()
        current["chapters"].append(ch)
    if current["chapters"]:
        acts.append(current)
    if len(acts) == 1 and acts[0]["name"] is None:
        acts = [{"name": None, "sub": "", "chapters": chapters}]
    seen = {}
    for a in acts:
        if a["name"]:
            key = a["sub"].lower()
            if key in seen:
                print(f"  ! duplicate act title '{a['sub']}' — fix canon 10 before typesetting",
                      file=sys.stderr)
            seen[key] = a["name"]
    return acts


# --------------------------------------------------------------------------
# 1. concatenated markdown
# --------------------------------------------------------------------------

def build_md(title, author, acts) -> str:
    out = [f"# {title}", "", f"### {author}", "", "---", "", "## Contents", ""]
    for a in acts:
        if a["name"]:
            out += [f"**Act {a['name']}: {a['sub']}**", ""]
        for ch in a["chapters"]:
            out.append(f"- {ch['title']}")
        out.append("")
    out += ["---", ""]
    for a in acts:
        if a["name"]:
            out += [f"# Act {a['name']}: {a['sub']}", "", PAGE_BREAK, ""]
        for ch in a["chapters"]:
            out += [f"## {ch['title']}", "", PAGE_BREAK if ch is not a["chapters"][0] else "",
                    ch["body"].strip(), "", "---", ""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


# --------------------------------------------------------------------------
# 2. typeset HTML for Google Docs import
# --------------------------------------------------------------------------

def paras_to_html(body: str) -> str:
    """First paragraph of a chapter and after each scene break is flush left; the rest are
    indented 21.6pt (Guide 6.2). '---' becomes a centered asterism, never a rule."""
    blocks, flush = [], True
    for raw in re.split(r"\n\s*(?:---|\*\s\*\s\*)\s*\n", body.strip()):
        chunk = [p for p in re.split(r"\n\s*\n", raw.strip()) if p]
        first = True
        for p in chunk:
            p = re.sub(r"\s+", " ", p).strip()
            if not p:
                continue
            p = html.escape(p, quote=False)
            p = re.sub(r"&quot;", '"', p)
            ind = "0pt" if (flush and first) else "21.6pt"
            blocks.append(f'  <p style="text-indent:{ind}">{p}</p>')
            first = False
        flush = False
        if len(chunk) > 1 or chunk:
            blocks.append(f'  <p style="text-align:center">{ASTERISM.strip()}</p>')
            flush = True
    while blocks and "asterism" in blocks[-1]:
        blocks.pop()
    if blocks and ASTERISM.strip() in blocks[-1]:
        blocks.pop()
    return "\n".join(blocks)


CSS = f"""
body {{ font-family: Georgia; font-size: 12pt; line-height: 1.38; margin: 1in; }}
p {{ margin: 0 0 0 0; orphans: 2; widows: 2; }}
h1 {{ font-family: Georgia; font-size: 16pt; text-align: center; margin: 0 0 0 0; }}
h2 {{ font-family: Georgia; font-size: 13pt; text-align: center; font-weight: bold;
      margin: 48pt 0 24pt 0; page-break-before: always; }}
.act {{ text-align: center; font-size: 16pt; font-weight: bold; margin-top: 170pt;
        page-break-before: always; }}
.act-sub {{ text-align: center; font-style: italic; margin-top: 6pt; }}
.title-page {{ text-align: center; margin-top: 200pt; }}
.title-page .t {{ font-size: 30pt; letter-spacing: 3pt; font-weight: bold; }}
.contents li {{ list-style: none; margin: 0 0 4pt 0; }}
.pagebreak {{ break-before: page; }}
"""


def build_html(title, author, acts) -> str:
    s = ["<!DOCTYPE html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
         f"<title>{html.escape(title)}</title>", f"<style>{CSS}</style>", "</head>", "<body>"]
    s += ['<div class="title-page">', f'  <p class="t">{html.escape(title)}</p>',
          f"  <p>{html.escape(author)}</p>", "</div>", PAGE_BREAK]
    s += ['<h1>Contents</h1>', '<ul class="contents">']
    for a in acts:
        if a["name"]:
            s.append(f'  <li><b>Act {a["name"]}: {html.escape(a["sub"])}</b></li>')
        for ch in a["chapters"]:
            s.append(f'  <li>&nbsp;&nbsp;&nbsp;{html.escape(ch["title"])}</li>')
    s += ["</ul>", PAGE_BREAK]
    for a in acts:
        if a["name"]:
            s += [f'<p class="act">Act {a["name"]}</p>',
                  f'<p class="act-sub">{html.escape(a["sub"])}</p>', PAGE_BREAK]
        for ch in a["chapters"]:
            s += [f'<h2>{html.escape(ch["title"])}</h2>', paras_to_html(ch["body"]),
                  '<p style="text-align:center">&thinsp;</p>']
    s += ["</body>", "</html>"]
    return "\n".join(s) + "\n"


# --------------------------------------------------------------------------
# 3. Kokoro TTS script
# --------------------------------------------------------------------------

ABBREV = [
    (r"\bMr\.\s", "Mister "), (r"\bMrs\.\s", "Missus "), (r"\bMs\.\s", "Miss "),
    (r"\bDr\.\s", "Doctor "), (r"\bCol\.\s", "Colonel "), (r"\bCapt\.\s", "Captain "),
    (r"\bLt\.\s", "Lieutenant "), (r"\bMaj\.\s", "Major "), (r"\bGen\.\s", "General "),
    (r"\bGov\.\s", "Governor "), (r"\bSen\.\s", "Senator "), (r"\bRep\.\s", "Representative "),
    (r"\bHon\.\s", "The Honorable "), (r"\bRev\.\s", "Reverend "), (r"\bDea?c?on\.\s", "Deacon "),
    (r"\bNo\.\s", "Number "), (r"\bNos\.\s", "Numbers "), (r"\bSt\.\s", "Street "),
    (r"\bAve\.\s", "Avenue "), (r"\bCo\.\s", "Company "), (r"\best\.\s", "estimated "),
    (r"\bft\.\b", " feet "), (r"\bmiles?\.\b", " miles "), (r"\bU\.?S\.?\s", "United States "),
    (r"\bU\.?S\.?\s?A\.?", "United States of America"), (r"\b&\b", " and "),
    (r"\bvs\.?\b", " versus "), (r"\betc\.?", "et cetera"), (r"\bJr\.?", "Junior"),
    (r"\bSr\.?", "Senior"), (r"\b[Pp]m\b", " P M"), (r"\bam\b", " A M"),
]

ROMAN = {"I": "One", "II": "Two", "III": "Three", "IV": "Four", "V": "Five"}


def speechify(text: str) -> str:
    t = text
    # 1. drop markdown and scene breaks
    t = re.sub(r"^\s*(---|\*\s\*\s\*|===+)\s*$", "\n\n", t, flags=re.M)
    t = re.sub(r"^#{1,6}\s*", "", t, flags=re.M)
    t = re.sub(r"[*_`>#]", "", t)
    t = re.sub(r"[\[\]()]|[|]", " ", t)
    t = t.replace(PAGE_BREAK, " ")
    # strip non-Latin glyph blocks (Cherokee syllabary etc.) — espeak-ng cannot phonemize them
    t = re.sub(r"[^\x00-\x7F“”‘’—–…°£]", "", t)
    # 2. dash conversion, by syntactic context
    t = re.sub(r"\u2014([\u201d\"]?)\s+(?=[a-z]+(?:\s+\w+){0,3}\s+(?:said|asked|replied|called|told|answered|cried|whispered|muttered)\b)",
               r",\1 ", t)      # "I—" he said.    ->  "I," he said.
    t = re.sub(r"\u2014([\u201d\"]?)\s+(?=[A-Z])", r".\1 ", t)   # "Wait—" He turned.  ->  "Wait." He turned.
    t = t.replace("\u2014", ",").replace("\u2013", " to ").replace("--", ",")
    t = re.sub(r"\s*,\s*,", ",", t)                     # collapse duplicate punctuation
    t = re.sub(r",\s*([.;:!?])", r"\1", t)
    t = t.replace("\u201c", '"').replace("\u201d", '"').replace("\u2018", "'").replace("\u2019", "'")
    # 3. abbreviations and initials
    for pat, rep in ABBREV:
        t = re.sub(pat, rep, t)
    t = re.sub(r"\b([A-Z])\.\s*([A-Z])\.(?=\s|$)", r"\1 \2", t)   # J. R. -> J R
    t = re.sub(r"(?<=[a-z] )\b([A-Z])\.(?=\s|$)", r"\1", t)
    # 4. spelled-out numbers so zero digits survive... none may survive
    def roman(mo):
        return f"Act {ROMAN.get(mo.group(1).upper(), mo.group(1))}"
    t = re.sub(r"\bAct\s+([IVX]+)\b", roman, t)
    t = re.sub(r"\bChapter\s+(\d+)\b", lambda m: f"Chapter {number_words(int(m.group(1)))}", t)
    t = re.sub(r"\b(?:Act|Section|Article|Tract|Plate|Figure|Table)\s+(\d+)\b",
               lambda m: f"{m.group(1)} {number_words(int(m.group(2)))}", t)
    t = re.sub(r"\b(1[0-9]\d\d|[12]0\d\d)\s*[-\u2013\u2014]\s*(\d{2,4})\b",
               lambda m: (f"{year_words(int(m.group(1)))} to "
                          f"{year_words(int(m.group(2))) if len(m.group(2)) == 4 else words_1_999(int(m.group(2)))}"), t)
    t = re.sub(r"\b(1[0-9]\d\d|20\d\d)\b", lambda m: year_words(int(m.group(1))), t)
    t = re.sub(r"\$(\d{1,3})(?:,(\d{3}))?", lambda m: f"{number_words(int(m.group(1)+ (m.group(2) or '')))} dollars", t)
    t = re.sub(r"(\d+)\s?(cents|¢)", lambda m: f"{number_words(int(m.group(1)))} cents", t)
    t = re.sub(r"(\d+(?:\.\d+)?)", lambda m: number_words(int(float(m.group(1))))
               if "." not in m.group(1) else m.group(1).replace(
                   ".", " point ").join([""]) or number_words(int(m.group(1).split(".")[0])), t)
    # single-letter glosses must not be read as the article
    t = re.sub(r'"\s*[Aa]\.\s*"', '"Ah."', t)
    t = re.sub(r"\b(?:Ah|Oh|Mm|Hm|Mm)\b", lambda m: {"Oh": "Oh", "Mm": "Mm"}.get(m.group(0), m.group(0)), t)
    t = re.sub(r"\s+([,.;:!?])", r"\1", t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def build_audiobook(title, author, acts) -> str:
    chunks = [f"{title}. By {author}. A novel.", ""]
    for a in acts:
        if a["name"]:
            act_word = ROMAN.get(a["name"], a["name"])
            chunks += [f"Act {act_word}. {a['sub']}.", ""]
        for ch in a["chapters"]:
            head = re.sub(r"^Chapter\s+(\d+):\s*", lambda m: f"Chapter {number_words(int(m.group(1)))}. ",
                          ch["title"])
            chunks += [head, ""]
            chunks += [speechify(ch["body"]), ""]
    out = "\n".join(chunks)
    out = re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"
    digits = re.findall(r"\d", out)
    if digits:
        print(f"  ! {len(digits)} digit(s) left in the audiobook script (Guide 6.3 requires zero)",
              file=sys.stderr)
        for mo in list(re.finditer(r".{0,40}\d.{0,40}", out))[:8]:
            print("      " + mo.group(0).replace("\n", " "), file=sys.stderr)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="build dist/ outputs for REVENUE")
    ap.add_argument("--title", default="REVENUE")
    ap.add_argument("--author", default="Kevin Russell")
    ap.add_argument("--only", choices=["md", "html", "audiobook", "all"], default="all")
    ap.add_argument("--src", default=None, help="chapter directory (default: manuscript/)")
    ap.add_argument("--out", default=None, help="output directory (default: dist/)")
    args = ap.parse_args(argv)

    global SRC, DIST
    if args.src:
        SRC = Path(args.src) if Path(args.src).is_absolute() else ROOT / args.src
    if args.out:
        DIST = Path(args.out) if Path(args.out).is_absolute() else ROOT / args.out
    if not SRC.is_dir():
        print(f"missing {SRC}", file=sys.stderr)
        return 2
    chapters = load_chapters()
    if not chapters:
        print("manuscript/ has no NN-slug.md chapters yet — nothing to build.", file=sys.stderr)
        return 0
    acts = split_acts(chapters)
    DIST.mkdir(exist_ok=True)
    words = sum(len(re.findall(r"\w+", c["body"])) for c in chapters)
    wrote = []
    if args.only in ("md", "all"):
        p = DIST / "revenue.md"
        p.write_text(build_md(args.title, args.author, acts), encoding="utf-8")
        wrote.append(p)
    if args.only in ("html", "all"):
        p = DIST / "revenue.html"
        p.write_text(build_html(args.title, args.author, acts), encoding="utf-8")
        wrote.append(p)
    if args.only in ("audiobook", "all"):
        p = DIST / "revenue-audiobook.txt"
        p.write_text(build_audiobook(args.title, args.author, acts), encoding="utf-8")
        wrote.append(p)
    print(f"built {len(chapters)} chapter(s) in {len(acts)} act(s), {words:,} words →")
    for p in wrote:
        try:
            label = str(p.relative_to(ROOT))
        except ValueError:
            label = str(p)
        print(f"  {label}  ({p.stat().st_size:,} bytes)")
    print("\nDocs follow-up required: after upload, set weightedFontFamily=Georgia document-wide "
          "and convert each [[PAGE_BREAK]] token to a real insertPageBreak in reverse index order.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

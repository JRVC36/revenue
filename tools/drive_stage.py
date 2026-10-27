#!/usr/bin/env python3
"""drive_stage.py — stage typeset HTML into dist/drive/ for Google Drive / Google Docs sync.

Git remains the canonical source of truth; this script renders:
  - dist/drive/chapters/NN-slug.html  (individual chapter Google Docs, Guide §6.2)
  - dist/drive/docs/<slug>.html       (canon/ and docs/ project documents as Google Docs)

Python 3.9+ standard library only.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import compile as book_compile  # noqa: E402

OUT = ROOT / "dist" / "drive"

DOC_TARGETS = [
    ("canon/canon-v1.md", "canon-v1", "Canon v1 — REVENUE"),
    ("docs/author-style-guide.md", "author-style-guide", "Author Style & Craft Guide — Kevin Russell"),
    ("docs/act-1-beat-sheet.md", "act-1-beat-sheet", "Act One Beat Sheet (Chs. 1–8)"),
    ("docs/act-1-style-audit.md", "act-1-style-audit", "Act One Style Audit (Chs. 1–8)"),
    ("docs/period-audit.md", "period-audit", "Period & Historical Audit"),
    ("docs/research-gaps-and-questions.md", "research-gaps-and-questions", "Research Gaps & Rulings Log"),
    ("docs/pitch-and-blurb.md", "pitch-and-blurb", "Pitch & Blurb"),
    ("docs/beta-reader-note.md", "beta-reader-note", "Beta-Reader Note"),
    ("docs/bibles/character-bible.md", "character-bible", "Bible — Characters"),
    ("docs/bibles/historical-context-bible.md", "historical-context-bible", "Bible — Historical Context"),
    ("docs/bibles/related-documents-bible.md", "related-documents-bible", "Bible — Related Documents"),
    ("docs/bibles/vocabulary-tone-bible.md", "vocabulary-tone-bible", "Bible — Vocabulary & Tone"),
]

DOC_CSS = """
body { font-family: Georgia; font-size: 11pt; line-height: 1.38; margin: 1in; color: #111111; }
h1 { font-family: Georgia; font-size: 18pt; font-weight: bold; margin: 18pt 0 8pt 0; }
h2 { font-family: Georgia; font-size: 14pt; font-weight: bold; margin: 16pt 0 6pt 0; }
h3 { font-family: Georgia; font-size: 12pt; font-weight: bold; margin: 12pt 0 4pt 0; }
h4 { font-family: Georgia; font-size: 11pt; font-weight: bold; font-style: italic; margin: 10pt 0 4pt 0; }
p { margin: 0 0 8pt 0; }
ul, ol { margin: 0 0 8pt 18pt; }
li { margin: 0 0 3pt 0; }
blockquote { margin: 6pt 0 8pt 18pt; padding-left: 10pt; border-left: 2pt solid #888888; font-style: italic; }
pre { font-family: Courier New; font-size: 9.5pt; background-color: #f5f5f5; padding: 8pt; margin: 6pt 0 8pt 0; white-space: pre-wrap; }
code { font-family: Courier New; font-size: 9.5pt; background-color: #f2f2f2; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0 12pt 0; font-size: 10pt; }
th, td { border: 1pt solid #cccccc; padding: 5pt 6pt; vertical-align: top; text-align: left; }
th { background-color: #f0f0f0; font-weight: bold; }
hr { border: none; border-top: 1pt solid #cccccc; margin: 14pt 0; }
"""


def md_inline(s: str) -> str:
    """Convert inline Markdown spans (`code`, **bold**, *italic*, [label](url)) cleanly."""
    parts = re.split(r"(`[^`]+`)", s)
    out = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) >= 2:
            out.append(f"<code>{html.escape(part[1:-1], quote=False)}</code>")
        else:
            t = html.escape(part, quote=False)
            t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
            t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
            t = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", t)
            out.append(t)
    return "".join(out)


def md_doc_to_html(md_text: str, title: str) -> str:
    lines = md_text.replace("\r\n", "\n").split("\n")
    out = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        f"<title>{html.escape(title)}</title>",
        f"<style>{DOC_CSS}</style>",
        "</head>",
        "<body>",
    ]
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Fenced code block
        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            if i < n:
                i += 1
            out.append(f"<pre>{html.escape(chr(10).join(buf), quote=False)}</pre>")
            continue

        # Horizontal rule
        if re.match(r"^(---+|\*\*\*+|___+)$", stripped):
            out.append("<hr>")
            i += 1
            continue

        # Heading
        m_head = re.match(r"^(#{1,4})\s+(.+?)\s*$", stripped)
        if m_head:
            lvl = len(m_head.group(1))
            out.append(f"<h{lvl}>{md_inline(m_head.group(2))}</h{lvl}>")
            i += 1
            continue

        # Markdown table
        if "|" in stripped and i + 1 < n and re.match(r"^\s*\|?[\s:-]+\|[\s|:-]*$", lines[i + 1]):
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append("<table><thead><tr>" + "".join(f"<th>{md_inline(h)}</th>" for h in headers) + "</tr></thead><tbody>")
            for r in rows:
                if len(r) < len(headers):
                    r += [""] * (len(headers) - len(r))
                out.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in r[: len(headers)]) + "</tr>")
            out.append("</tbody></table>")
            continue

        # Blockquote
        if stripped.startswith(">"):
            bq = []
            while i < n and lines[i].strip().startswith(">"):
                bq.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            out.append(f"<blockquote><p>{md_inline(' '.join(bq))}</p></blockquote>")
            continue

        # Unordered or ordered list
        if re.match(r"^([-*+])\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            ordered = bool(re.match(r"^\d+\.\s+", stripped))
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>")
            while i < n:
                s = lines[i].strip()
                m_li = re.match(r"^(?:\d+\.|[-*+])\s+(.+)$", s)
                if not m_li:
                    break
                item_parts = [m_li.group(1)]
                i += 1
                while i < n and lines[i].startswith("  ") and not re.match(r"^\s*(?:\d+\.|[-*+])\s+", lines[i]):
                    if not lines[i].strip():
                        break
                    item_parts.append(lines[i].strip())
                    i += 1
                out.append(f"<li>{md_inline(' '.join(item_parts))}</li>")
            out.append(f"</{tag}>")
            continue

        # Paragraph
        para = [stripped]
        i += 1
        while i < n:
            s = lines[i].strip()
            if (
                not s
                or s.startswith("```")
                or s.startswith("#")
                or s.startswith(">")
                or re.match(r"^(---+|\*\*\*+|___+)$", s)
                or re.match(r"^(?:\d+\.|[-*+])\s+", s)
                or ("|" in s and i + 1 < n and re.match(r"^\s*\|?[\s:-]+\|[\s|:-]*$", lines[i + 1]))
            ):
                break
            para.append(s)
            i += 1
        out.append(f"<p>{md_inline(' '.join(para))}</p>")

    out += ["</body>", "</html>"]
    return "\n".join(out) + "\n"


def build_chapter_html(ch: dict) -> str:
    body = re.sub(r"^#\s*Act\s+.*$", "", ch["body"], count=1, flags=re.M).strip()
    s = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        f"<title>{html.escape(ch['title'])}</title>",
        f"<style>{book_compile.CSS}</style>",
        "</head>",
        "<body>",
        f"<h2>{html.escape(ch['title'])}</h2>",
        book_compile.paras_to_html(body),
        "</body>",
        "</html>",
    ]
    return "\n".join(s) + "\n"


def main() -> int:
    ch_dir = OUT / "chapters"
    doc_dir = OUT / "docs"
    ch_dir.mkdir(parents=True, exist_ok=True)
    doc_dir.mkdir(parents=True, exist_ok=True)

    chapters = book_compile.load_chapters()
    for ch in chapters:
        stem = ch["path"].stem
        target = ch_dir / f"{stem}.html"
        target.write_text(build_chapter_html(ch), encoding="utf-8")
        print(f"  staged chapter → {target.relative_to(ROOT)}  ({target.stat().st_size:,} bytes)")

    for rel_src, slug, title in DOC_TARGETS:
        src = ROOT / rel_src
        if not src.exists():
            print(f"  ! missing {rel_src}", file=sys.stderr)
            continue
        target = doc_dir / f"{slug}.html"
        target.write_text(md_doc_to_html(src.read_text(encoding="utf-8"), title), encoding="utf-8")
        print(f"  staged doc     → {target.relative_to(ROOT)}  ({target.stat().st_size:,} bytes)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# manuscript/

**One canonical Markdown file per chapter** (Style Guide §6.1). Nothing else lives here — no outlines,
no notes, no "chapter 2 draft FINAL v3".

## Naming

```
01-the-measured-hollow.md
02-the-second-chain.md
11-the-empty-year.md
```

- `NN` is the book's running order and the chapter number. `compile.py` numbers the chapter from the
  filename, so the file `07-….md` **is** Chapter 7 whatever its heading says.
- The slug is the chapter's *object or hour*, not its theme (`07-the-loose-mules.md`, never
  `07-the-reckoning.md`). It becomes the Drive/Google Docs title if a chapter is ever exported.
- The heading inside is `## Chapter NN: Title Case Title`, and it must agree with the filename
  (`check.py` flags both directions of disagreement).
- An act opens with a first-level heading on the first line of the chapter that opens it:
  `# Act Two: The Weight of It`. One act heading per act, and **no two acts share a title** — the
  outline has "THE RECKONING" twice and the build will fail until that's resolved.

## Form rules inside a chapter file

| Thing | Do this | Because |
|---|---|---|
| Scene break | a bare `---` line on its own | `compile.py` renders it as a centered asterism `*   *   *`; a horizontal rule in the typeset build is the mark of a draft, not a book |
| Dialogue | `“Curly quotes,” he said.` | the linter's anachronism bans apply to **narration only**; character speech is exempt by design (§5.2) |
| Numbers | spelled out in prose — *ninety cents*, *two years*, *the eighteenth of October*; digits allowed only in a ledger, a notice, or a heading | the audiobook build must end with **zero digits** (§6.3) |
| Years | every printed year needs a row in `docs/period-audit.md` | §5.1: verify by exact year. `check.py` NOTEs every year so the ledger can't fall behind the draft |
| Dash | one em dash per paragraph maximum in dialogue; ~6 per 1,000 words of narration | the outline runs 14/1k. `check.py` counts |
| Interiority | only when the POV is alone | §2.3, hard law |
| The tic | `not X — it's Y` is at **two in the whole book** | §4 Pass 4 |

## Workflow

1. Draft in the repo file. Never in Drive. Drive is for sharing a build, not for holding the text.
2. `python3 tools/check.py manuscript` before ending a session; a `BAN` means stop and fix it now,
   because a banned word in chapter 3 is in twelve chapters by the time you notice.
3. `python3 tools/readability.py` when a chapter feels *smooth* — smooth is the failure mode here; the
   report tells you whether the chapter is bimodal or stuck in the dead middle.
4. When a scene works on the page and contradicts a bible, **the page wins** and you update
   `canon/canon-v1.md` in the same commit (the guide's precedence rule).

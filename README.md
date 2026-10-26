# REVENUE

**A novel. Western North Carolina, 1878–1881.** The whiskey tax at ninety cents on the proof gallon, and
the law that takes the land underneath the still. A railroad is coming the whole time and never shows up.

Status: **scaffolded, not drafted.** The structure, the canon, the bibles and the tools exist; the
manuscript does not. Working title `REVENUE` per the author's own outline; the subtitle is working.

---

## What this repository is for

`REVENUE` is one of the book projects under `Drive/Books/`. The house rule (Style Guide §6.1) is that a
book is **self-contained in Git with zero external dependencies** — the repo is the source of truth and
Google Drive is where a *build* gets shared. The Drive copy of the outline is preserved verbatim at
`docs/outline-v1-verbatim.md` and is never edited; every change to the story happens in `canon/`.

## Structure

```
canon/
  canon-v1.md                     SOURCE OF TRUTH: rulings, timeline, cast, legal mechanics,
                                  voice rules, the blocked-question list, continuity anchors
docs/
  author-style-guide.md           standing craft rules (verbatim from Drive; repo copy wins)
  outline-v1-verbatim.md          the outline as written in Drive, unaltered, with line numbers
  research-gaps-and-questions.md  the research asks handed back to the author (18 asks, 23 questions)
  period-audit.md                 verification ledger: every year, law, and object the book prints
  pitch-and-blurb.md              one line, paragraph, genre promise, blurb
  beta-reader-note.md             the one-page questionnaire sent with partials
  bibles/
    character-bible.md            who wants what, what they will not say, and how each of them talks
    historical-context-bible.md   the 1878–82 revenue war, the court, the railroad, what is invented
    vocabulary-tone-bible.md      the words, the bans, AND the linter's rule table (§7)
    related-documents-bible.md    what exists where, and the archive list still owed
manuscript/
  NN-chapter-slug.md              one file per chapter (see manuscript/README.md)
tools/
  check.py                        anachronism + continuity linter, built FROM the vocabulary bible
  readability.py                  narration-only sentence and syllable diagnostics
  compile.py                      dist/revenue.md · dist/revenue.html · dist/revenue-audiobook.txt
  sample/                         the fixture the tools are tested against (deliberately dirty)
dist/                             compiled outputs — gitignored
google_drive/                     raw text exports of the four Drive docs — gitignored, not editable
```

## Commands

```bash
python3 tools/check.py                      # lint manuscript/ — a BAN exits 1 and blocks all builds
python3 tools/check.py --stats              # Pass-4 audit: the tic count, dash and filter budgets
python3 tools/check.py --all                # sweep the outline and the gap list too (bibles excluded)
python3 tools/readability.py                # per-chapter rhythm report (dialogue is not scored)
python3 tools/compile.py                    # build dist/ (md + typeset html + TTS script)
python3 tools/compile.py --src tools/sample --out /tmp/dist   # dry run against the fixture
```

No third-party packages, Python 3.9 standard library only. `compile.py` prints the two Google Docs API
steps it cannot do itself (the Georgia `weightedFontFamily` pass and the reverse-order
`[[PAGE_BREAK]]` → real page break conversion).

## The rulings that govern everything

Recorded in `canon/canon-v1.md` §1 and re-derived nowhere else. Summarized here only so a new reader
knows what shape the book is in:

1. **R-1 — It is a novel.** The outline's stage idiom is *translated*, not honored: settings become
   weather and labor, exits become bodies, the cast list's ages become debts and calluses.
2. **R-2 — The railroad is in the book as approach.** Grading powder, a federal transit, men who walk out
   for the grade. **No rails and no train before mid-1882** — and, per R-5, none at all.
3. **R-3 — The engine is forfeiture of the land, not the 90 cents.** The triable question is *did the
   neighbor know and permit*, not *does the distiller owe*. That makes the barn fire a crime against the
   government's own interest, makes the missing written order the eloquent page, and gives Margaret
   standing in her own right.
4. **R-4 — Joshua is the spine (~80%), Margaret the secondary (~20%).** Two heads in the whole book;
   Parrish is never inside, so his turn has to be legible in what he writes and what he leaves out.
5. **R-5 — The book ends in autumn 1881 and the train is never seen.** The final sound is powder off the
   far side of a ridge, or a report of a date; a whistle would be an anachronism (Hampton was the rail head
   in October 1881) and a picture would be a symbol, and both are refused on purpose.
6. **R-6 — Joshua is the elder brother and the owner in fee.** He inherited the farm and mortgaged it, so
   the forfeiture reaches his deed as well as his brother's wife's; an owner in fee is presumed to know, so
   the man whose whole function is not-knowing is the one man who cannot plead it. Jacob 45, Joshua 50.
7. **R-7 — Margaret owns the forty acres the still stands on**, as a married woman's separate estate under
   the 1868 constitution. That is why Jacob put the still there — it is the only ground his creditors cannot
   reach — and why the trial is about her knowledge rather than his debt. It also corrected R-6: the barn is
   on her freehold, adjoining Joshua's mortgaged farm, and the government's second move is to argue that
   those two places are one place.
9. **R-9 — What Parrish pays is an audit of himself.** The Department asks him why a barn the United States
   had a claim on was burned; both honest answers end him, he writes the second one in his fair hand, and the
   complaint closes without adverse finding. Because R-4 keeps us out of his head, his whole cost is carried
   in paperwork — and the last thing he does in the book is shut a file.
8. **R-8 — Caleb is Joshua's firstborn**, given to Jacob's house in 1862 when Joshua enlisted and the boy's
   mother died. The informer and the man who comes for him were raised as brothers; nobody in the book says
   any of it, and three planted facts (`canon §10`, the "Caleb audit") carry the whole arrangement without a
   single statement.

## Editing workflow

Draft in `manuscript/`, run `check.py`, then update `canon/canon-v1.md` in the same commit if the scene
that works on the page disagrees with a bible. When the canon and a bible conflict, **the canon wins**.
When a bible's rule is a linter rule, edit the bible (`docs/bibles/vocabulary-tone-bible.md` §7) — the
linter reads its own rules from there, so the check and the prose never drift apart.

`OPEN` questions are listed in `canon/canon-v1.md` §9 and are being answered **one at a time by the
author**, in that order; each answer becomes a numbered ruling in §1 with the tag `AUTHOR`.

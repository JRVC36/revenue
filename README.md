# REVENUE

**A novel. Western North Carolina, 1878–1881.** The whiskey tax at ninety cents on the proof gallon, and
the law that takes the land underneath the still. A railroad is coming the whole time and never shows up.

Status: **drafting Act One (`01-the-water-is-right.md` through `04-what-a-no-costs.md` complete; detailed scene blueprint for Chapters 1–8 in `docs/act-1-beat-sheet.md`).** Working title `REVENUE` per the author's own outline; the subtitle is working.

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
  act-1-beat-sheet.md             detailed scene-by-scene blueprint for Act One (Chapters 1–8)
  author-style-guide.md           standing craft rules (verbatim from Drive; repo copy wins)
  outline-v1-verbatim.md          the outline as written in Drive, unaltered, with line numbers
  research-gaps-and-questions.md  the research asks handed back to the author (21 asks, 23 questions)
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
  drive_stage.py                  dist/drive/{chapters,docs}/*.html staged for Google Docs sync
  drive-manifest.json             Google Drive folder & Doc IDs mirrored under Drive/Books/Revenue
  sample/                         the fixture the tools are tested against (deliberately dirty)
dist/                             compiled outputs — gitignored (mirrored to Drive/Books/Revenue)
google_drive/                     raw text exports of the four Drive docs — gitignored, not editable
```

## Commands

```bash
python3 tools/check.py                      # lint manuscript/ — a BAN exits 1 and blocks all builds
python3 tools/check.py --stats              # Pass-4 audit: the tic count, dash and filter budgets
python3 tools/check.py --all                # sweep the outline and the gap list too (bibles excluded)
python3 tools/readability.py                # per-chapter rhythm report (dialogue is not scored)
python3 tools/compile.py                    # build dist/ (md + typeset html + TTS script)
python3 tools/drive_stage.py                # stage individual chapters & docs HTML for Drive sync
python3 tools/compile.py --src tools/sample --out /tmp/dist   # dry run against the fixture
```

No third-party packages, Python 3.9 standard library only. **Git remains canonical** (`canon/`, `docs/`, `manuscript/`); after every committed change, staged HTML and compiled outputs are mirrored in place to `Drive/Books/Revenue` (`Manuscript Chapters`, `Canon & Docs`, and top-level `REVENUE — Manuscript (Compiled)`) using the persistent IDs in `tools/drive-manifest.json`, followed by the Google Docs `Georgia` font and reverse-order `[[PAGE_BREAK]]` passes.

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
   far side of a ridge, or a report of a date; a whistle would be an anachronism (Hampton, 15.5 air miles
   behind Doe River Gorge, was the rail head in October–November 1881) and a picture would be a symbol, and
   both are refused on purpose.
6. **R-6 — Joshua is the elder brother and the owner in fee.** He inherited the farm and mortgaged it, so
   the forfeiture reaches his deed as well as his brother's wife's; an owner in fee is presumed to know, so
   the man whose whole function is not-knowing is the one man who cannot plead it. Jacob 45, Joshua 50.
7. **R-7 — Margaret owns the forty acres the still stands on**, as a married woman's separate estate under
   the 1868 constitution. That is why Jacob put the still there — it is the only ground his creditors cannot
   reach — and why the trial is about her knowledge rather than his debt. It also corrected R-6: the barn is
   on her freehold, adjoining Joshua's mortgaged farm, and the government's second move is to argue that
   those two places are one place.
8. **R-8 — Caleb is Joshua's firstborn**, given to Jacob's house in 1862 when Joshua enlisted and the boy's
   mother died. The informer and the man who comes for him were raised as brothers; nobody in the book says
   any of it, and three planted facts (`canon §10`, the "Caleb audit") carry the whole arrangement without a
   single statement.
9. **R-9 — What Parrish pays is an audit of himself.** The Department asks him why a barn the United States
   had a claim on was burned; both honest answers end him, he writes the second one in his fair hand, and the
   complaint closes without adverse finding. Because R-4 keeps us out of his head, his whole cost is carried
   in paperwork — and the last thing he does in the book is shut a file.
10. **R-10 — Matthew asks for three things: the store debt, the day of the raid, a written appointment.**
    Granted, granted, refused — and the day he picked gets a fifteen-year-old shot behind Harper's barn, which
    is the first of this book's two deaths and the reason the cove's later restraint is restraint. He is "paid"
    by a Treasury order returned uncashed, marked *person unknown*.
11. **R-11 — Hoss Tyler is a creditor, not a Judas, and Harper is the man who said *don't*.** The day book
    is taken, not bought, and Tyler's own protest authenticates it; the barn burned in Act Two belongs to the
    one neighbor who was right in Act One. Being right is not a defense in this book, only a forecast.
12. **R-12 — The book ends in typography.** Three documents after the last human scene: the agent's 1882
    report (with the boy's name spelled right), a county history with the year wrong by two, and the title page
    of a dime novel about Caleb. No author's note, no apology for accuracy — the verification record stays in
    this repo, where it does its work.
13. **R-13 — The court is real, and so are its dates.** The Circuit Court for the Western District of North
    Carolina sat at **Statesville** on the third Monday in April and October, in rented rooms — there was no
    federal courthouse in Asheville until 1892. Jacob is convicted at the term that opened **21 April 1879**
    and released on the two years **21 April 1881**; Caleb is tried at the term that opened **17 October 1881**;
    the book ends in **November 1881**, seven months before the rails reach Elk Park. Judge Robert Paine Dick is
    named in the docket and never given an invented word. This ruling rebuilt the chapter map as v1 (**28
    chapters**) and moved *The Return* ahead of *The Surrender*.
14. **R-14 — "The Whistlers" is the enemy's word.** The name is kept as owned invention and appears only in
    print *about* the cove — the Bureau's papers, the county paper, the dime novel that ends the book — because
    naming the meeting is the evidence the hollow has spent the whole book not having. It also shares a word
    with the sound the book refuses to describe (R-5), and the overlap is never explained. "The Regulators" was
    rejected: it imports 1768–71 and reads as a borrowed thesis.
15. **R-15 — Above Cranberry Forge and Elk Park: Mitchell County on the docket, Burke and Watauga in the deed
    box.** In 1878–1881 Cranberry and Elk Park sit in **`Cranberry Township, Mitchell County`** (seat
    **Bakersville**; formed 16 Feb 1861), *not* Burke — though that same ground was Burke before 1833 and
    Watauga 1849–61, and both older courthouses (Morganton 1865, Boone 1873) burned before Act One opens, making
    Margaret's folded deeds the only copies left. Putting the hollow at the railroad's exact destination also
    makes the 1880–81 blasting across State Line Gap genuinely audible while Doe River Gorge still blocks any
    whistle from Hampton. `Newland` (1911–12) joins `Avery County` (1911) on the `BAN` list.
16. **R-16 — 1861–1876 is bone structure, never a speech.** Joshua walked over State Line Gap into the Union
    army in summer **1862** (the same summer Congress enacted the July 1, 1862 distilled-spirits tax to pay his
    army) and mustered out at **Knoxville in 1865** (unit kept unnamed on the page), so the government coming
    for his deed is his own side; Jacob stayed on the mountain 1862–65 dodging Home Guard sweeps and raising
    Caleb (locking R-8); and the **1868 NC Constitution** sits in the room solely as paperwork — both the
    feared township tax-sale regime and the `Art. X §6` clause that shields Margaret's forty acres (R-7). No
    Klan subplot, no party speeches.
17. **R-17 — `Blockader` on the mountain, `moonshiner` in outside print only (closes §9 Q-1…Q-14).** Around
    their own tub the Brennans use work-verbs (*making*, *running*, *a run*, *the whiskey*); when mountain or
    county-town speakers name the trade as a class, the word is **`blockader` / `blockading` / `blockade
    whiskey`** (wartime blockade carryover, never explained); Parrish speaks the statute (*illicit distiller*);
    and **`moonshiner` / `moonshine` belong strictly to outside print** (newspapers, *E2*, *E3*), never to
    narration or dialogue.
18. **R-18 — *The Missing Page* (Ch. 15): Parrish puts the *Stowell* "connected premises" trap to Joshua over
    Tyler's day-book exhibit, and Joshua spots Matthew's omitted folio.** After Harper's barn burns (Ch. 14) —
    with Jacob already serving his two years from the April 1879 Statesville term (R-13) — Parrish turns the
    civil *in rem* libel onto Joshua's mortgaged farm (`Parcel A`: mill, water race, cart road) as *"premises
    connected therewith"* and examines Joshua over a clerk's certified exhibit schedule copied from Hoss
    Tyler's seized day book (R-11). While answering carefully enough not to hand Parrish a forfeiture
    admission, Joshua — who knows Tyler's foliation from fifteen years of settling mill-toll balances — sees
    the skipped folio number where Matthew's settled store account (`"by order of the agent"`, R-10) was left
    out of the public exhibit copy. Neither man speaks Matthew's name.
19. **R-19 — *The Deposition* (Ch. 23) & *The Burning* (Ch. 14): Parrish's hired possemen lit Harper's barn
    without orders, and Margaret trades her double-edged fire affidavit for `Elisha Councill`'s name in *E1*.**
    Reconciles Ch. 14 with R-9 and the outline: Caleb's network stores whiskey under William Harper's barn
    floor over his Act One *don't* (R-11), and Parrish's hired raid party staves in the kegs and fires the barn
    without Parrish's order. In *The Deposition* (Ch. 23), Margaret requires Parrish to strike `"a boy"` and
    write **`Elisha Councill`** in his Commissioner's report (*E1*, R-10/R-12), then swears one strictly true
    sentence — Parrish stood in the road calling his hired men off and did not order the fire, which caught in
    the split kegs of blockade whiskey stored on Harper's floor — saving Parrish's career with Washington while
    putting sworn proof of stored spirits into the federal record against the cove.
20. **R-20 — *Did She Know?* (Ch. 26): Margaret's unburned Watauga deed and the absence of any certified privy
    examination stall `Parcel B` into `"the tract remains in contest"` (*E1*).** At the October 1881 Statesville
    sitting (Judge Robert P. Dick named, never voiced, R-13), Margaret produces her folded pre-1861 Watauga
    root deed (the sole copy left after the 23 March 1873 Boone courthouse fire, R-15) and stands on `NC Const.
    1868 Art. X §6`, N.C. Laws 1848–49 ch. 41, and *Scott v. Battle*, 85 N.C. 184 (1881): no clerk's
    privy-examination certificate exists anywhere giving Jacob or any man a lease or estate in her barn, and a
    married woman cannot lose her separate realty by estoppel without one. In her single spoken sentence on
    knowledge she refuses to clear `Parcel B` by naming Caleb or Joshua — holding `Parcel B` over on exceptions
    (`"the tract remains in contest"` in Parrish's 1882 report, R-12), while mortgage and defense costs force
    Joshua to sell the mill (`Parcel A`) in Ch. 27 (*The Mill Sold*). **Closes all three `canon §12` scene
    proposals.**

## Editing workflow

Draft in `manuscript/`, run `check.py`, then update `canon/canon-v1.md` in the same commit if the scene
that works on the page disagrees with a bible. When the canon and a bible conflict, **the canon wins**.
When a bible's rule is a linter rule, edit the bible (`docs/bibles/vocabulary-tone-bible.md` §7) — the
linter reads its own rules from there, so the check and the prose never drift apart.

`OPEN` questions are listed in `canon/canon-v1.md` §9 and are being answered **one at a time by the
author**, in that order; each answer becomes a numbered ruling in §1 with the tag `AUTHOR`.

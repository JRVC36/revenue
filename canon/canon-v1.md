# CANON — *REVENUE* — v1

Single source of truth for *REVENUE*: timeline, cast, technical and legal mechanics, voice rules,
and continuity rulings. **When an earlier outline or bible conflicts with a choice that works on the
page, update this file to match the manuscript** (Style Guide §6.1, Precedence Rule).

Status tags used below:

| Tag | Meaning |
|---|---|
| `AUTHOR` | Ruled by Kevin. Binding. Not a research question. |
| `USER` | Supplied by Kevin from archival or primary work. Highest confidence. |
| `LEAD` | Verified against secondary/web sources by the agent on 2026-10-26. **Direction-finding only — needs primary confirmation before it reaches the page.** |
| `OPEN` | Unresolved. Blocks drafting. Listed in §9 in question order. |
| `INVENT` | Deliberate fiction. Logged here so it is never mistaken for a source. |

Nothing tagged `LEAD` may appear in the manuscript as settled fact until it is re-tagged `USER` or
resolved in `docs/period-audit.md`.

---

## 1. Locked rulings

**R-1 `AUTHOR` (2026-10-26) — *REVENUE* is a prose novel.** Not a play, not a screenplay, not a
three-act stage drama. The `OUTLINE: REVENUE` document's stage idiom ("Opening image," "Final image
of Act One," "the play can go a few directions here," "In a voiceover," "Titles or voiceover") is
**vocabulary to be translated, not honored.** Every "image" becomes a scene; every "voiceover"
becomes close-third interiority inside a permitted POV; the epilogue titles become either an
author's note or diegetic print (newspaper, dime novel, pension file, land record) — see Q-11.
Act structure survives as *The Bound Tree* uses it: three named Acts grouped in Contents, chapters
numbered continuously across the book.

Consequences:
- The Style Guide applies in full, including §2 (POV/interiority) and §4 (five-pass revision).
- Chapter architecture, not scene-blocks, is the drafting unit. `manuscript/NN-slug.md`.
- "A Three-Act Drama, 1878–1881" on the outline's title page is superseded. Working subtitle for the
  title page: **A Novel · Western North Carolina · 1878–1881** (set by R-5; R-2 had proposed 1882, and the
  ruling that the train is never seen pulled the date back in).

**R-2 `AUTHOR` (2026-10-26) — the railroad moves into the book.** The ET&WNC narrow gauge is not
background; it is the second engine and the measure of everything the cove loses. Handling:
- **Acts One and Two: audible, not visible.** Steel arrives as sound and object before it arrives as
  fact — grading powder heard off the ridges at night (the "blast" a child mistakes for thunder with
  no cloud), a surveyor's transit and flagmen on a neighboring ridge, imported nails and window glass
  at the store, a man who quits the hollow to work the grade.
- **The survey party is the second front.** Parrish works with a chain and a book; the railroad works
  with a chain and a book. This is the direct bridge to *The Bound Tree*'s machinery and the reason a
  reader who has read that book will recognize the world. *Deliberate echo, do not over-explain it.*
- **Do not put a running train in 1878–1881.** Track reaches Hampton, TN, 22 Aug 1881; mid-June 1882
  Elk Park; 3 July 1882 Cranberry `LEAD`. Any earlier locomotive in the cove is an anachronism.
- **Structural consequence — Q-2.** Closed by **R-5**: the present tense ends in 1881 and the train is
  never seen by anybody, anywhere, in this book.

**R-3 `AUTHOR` (2026-10-26) — the plot engine is forfeiture of the land, not the tax.** The statute
forfeits the still, the apparatus, **the lot or tract of land**, and the interest of anyone who
knowingly suffered, permitted, or connived at distilling there. `LEAD` (Act of July 20, 1868, 15 Stat.
125; Rev. Stat. §§ 3258, 3281; Act of Feb. 8, 1875 § 16, 18 Stat. 310; *United States v. Stowell*,
133 U.S. 1 [1890]; *Dobbins' Distillery v. United States*, 96 U.S. 395 [1878]).

Reversal this forces on the outline: the burden of proof is not "does Jacob owe ninety cents a gallon."
It is **"did Harper know."** A man's own deed is what is actually in jeopardy, and a neighbor's
knowledge — not his loyalty — is the legal question. Practical effects now binding on structure:
- Parrish's leverage is administrative before it is violent. He builds a *knowledge case*. His
  questions at the courthouse and in the store are evidence-gathering against third parties.
- Joshua's refusal to inform is not a posture. It is a mortgage payment: an encumbered owner in fee
  could not have a distiller's bond approved at all, so his title is the thing on the table. `LEAD`
- Margaret's exposure is real and unglamorous — dower, curtesy, homestead, and a widow's standing to
  contest a libel. **Currently absent from the outline; see Q-4.**
- The barn fire is a crime *against the government's own interest*, which is why Act Two turns on it
  and why Parrish does not order it in writing. The outline already has it "not on Parrish's orders
  explicitly" — keep, and make the missing order the thing Joshua reads.

---

**R-4 `AUTHOR` (2026-10-26) — Joshua Brennan is the spine (~80%), Margaret Brennan the secondary
POV (~20%).** The split itself was already house law (Style Guide §2.1); this names who fills it.

Why the ruling is right for this book, recorded so the reason survives the drafting: Joshua is the only
character whose every scene is a decision with a price; he can stand in the cove and in the office; and he
is the one who *keeps the books*, which is the novel's form (measured, counted, understated). Jacob is the
man things happen to — his POV would make a victim's book — and Caleb's would make a bildungsroman in the
wrong direction.

Consequences, binding:
- **Two heads only.** No scene is written inside Jacob, Caleb, Matthew, Harper, or Parrish. Their feelings
  are inferred from gesture, withheld answers, and what their hands do — the interiority rule (§2.3) turned
  into a POV law. `tools/check.py` has a FLAG row for it.
- **Parrish is never inside.** The outline says "Parrish is alarmed and energized," "Parrish understands
  the situation." In the book we get what he writes, what he does not write (the missing order — R-3), and
  the empty chair. His turn, if a reader is to feel it, must be legible in a fair hand on paper.
- **The barn fire and the ambush are witnessed or reported, never inhabited.** Caleb's organizing arrives
  as objects and hearsay — a rope, a nail, a note passed at the store. This is a *gain*: the cove's
  resistance stays opaque to the reader exactly as it stays opaque to Parrish.
- **The opening image survives, the eye changes.** The outline opens on Jacob at the still "placed the way
  you'd place a garden." In the book that image is **Joshua weighing the corn that becomes the whiskey** —
  the still is seen working because Joshua knows its numbers. Jacob's hands are in the chapter; his head is
  not, and that absence is one of the things the book is about.
- **Margaret's 20% is legal, not decorative.** She gets the chapters where the *paper* decides something —
  the notices, the search, the standing to contest. She is not given the grief chapters.
- **Map.** The POV-tagged chapter map is §12, drafted against this ruling.

---

**R-5 `AUTHOR` (2026-10-26) — the book ends in autumn 1881, and the railroad is heard about, never
seen.** Of the three ways to close a novel that has spent four acts on an approaching engine, the author
chose the one that refuses the picture: **no train on the page, at any point.** The last movement is
Joshua leaving — the mill sold, walking up toward the gap on the far side of which the grade is being
made — and the book stops on what reaches him from the wrong side of a ridge.

**The acoustic constraint, because it will otherwise be drafted wrong.** In October 1881 the nearest
steel is at **Hampton, Tennessee**, reached 22 August 1881; the rails do not lie within thirty air miles
of a Watauga hollow, and a locomotive's whistle does not carry thirty miles over that ground `LEAD`.
So the closing sound may **not** be an engine. What is legal, and better:
- a **blast** — the powder the grade crews use, which is the same sound the book planted in Act One
  (R-2), now returned to him with its meaning changed; or
- a **local, ambiguous sound** he can name and refuses to walk to: iron on stone, a hammer at the new
  turnpike work, a saw at the mill that is no longer his — with the sentence being that he knows the
  difference and does not care to check; and
- **report** rather than sense: a man who quit the hollow for the grade in Act One comes back for the
  winter with the news that the rails will be at Elk Park "come spring." Joshua hears the date the way he
  hears a price.

**What the ruling buys, stated so it is not lost later:** the reward for four acts of approach is
*withheld*, which keeps the mountain out of the symbol business (vocabulary-tone bible §10.5) and keeps
Joshua the man who measures everything **declining to measure this** — the one refusal in the book that
costs him nothing and therefore tells us everything. It also protects R-2 from the temptation to
"earn" the train.

**Consequences, binding:**
- Subtitle becomes **A Novel · Western North Carolina · 1878–1881**. If Q-9 adopts a printed epilogue
  reaching 1882 or later, the date on the title page reverts to 1882 — the fiction ends in 1881 either
  way, and only a document may cross the date.
- `tools/check.py` now FLAGs `locomotive|engine|whistle|depot|train|railroad|the cars` in narration for
  adjudication. The railroad may be *spoken of* (the company, the grade, the location); nothing may be
  *seen* doing it. Every hit is a decision, not an error.
- The map (§12) loses its proposed "The Train" chapter and keeps 26 chapters; chapter 26 is now the
  closing movement.
- The Act One / Act Three rhyme (powder heard at night, powder heard at the end) is the book's
  architectural spine. Nothing may explain it.
- **Research dependency created:** what civil road, bridge, or quarry work was actually under way within
  hearing of the cove in autumn 1881 (ask **R-13** in `docs/research-gaps-and-questions.md`). Until that
  is answered the final sound stays generic — "a blast off the ridge" is safe; "the railroad bridge at
  Watauga Creek" is not.

---

*R-6 `AUTHOR` (2026-10-26) — Joshua is the elder brother.** Joshua b. ~1828 (50 in 1878), Jacob
b. ~1833 (45 in 1878). The outline's contradiction is resolved in favor of "older brother," not in favor
of Jacob's number, because the birth order is load-bearing and the number is not.

What the ruling actually bought, and why it is not a cosmetic fix:
- **The elder inherited and mortgaged.** Joshua holds the farm in fee, encumbered; Jacob has no land of his
  own to put a still on, so the still goes in **Joshua's** barn, on **Joshua's** acreage. The forfeiture
  that R-3 aims at now lands on the spine POV's own deed. Joshua is not the man watching the law come for
  his brother; he is the man the law comes for while it is there.
- **The knowledge question gets a better target.** *Stowell*: the owner's land is forfeit if he "knowingly
  has suffered or permitted" the distilling or connived at it. A neighbor's ignorance is plausible; **an
  owner's is not**, and the owner is the man who keeps every account in the cove. Parrish's sharpest move
  in Act Two is therefore to stop asking Jacob anything and start asking Joshua what his brother was doing
  on his ground. `LEAD` on the doctrine; the scene is proposed at §12 (ch. 14), awaiting the author.
- **The cove's central technique becomes illegal for exactly one man.** "Not knowing" is what the hollow
  survives on, and it is a legal position — except for an owner in fee with a mortgage, who is *presumed* to
  know what happens in his own barn. R-4 plus R-6 puts the whole book's thesis inside the POV character's
  chest, which is what a spine ruling is for.
- **The bond refusal, stated precisely, once, in Act One.** Distillers had to be owners in fee "free from
  any mortgage, judgment, debt or lien whatsoever," and where a lien existed, **the written consent of every
  lienholder** was required (Act of July 27, 1868, 15 Stat. 125, §8; `LEAD`, already at §5). So the lawful
  path Jacob was shut out of was: *ask the creditor's signature for permission to make whiskey on your own
  family's land.* Joshua says it flatly, in the mill, and the book never explains it again.
- **Jacob's bible hook moves.** He is no longer the man who "stands on dirt he can prove." He is the man
  standing on dirt his **brother** can prove — which is why he can be calm in Act One, and why the sentence
  costs him nothing he personally owns, until it costs his brother everything.
- **Margaret's standing is now genuinely open, not merely unaddressed.** She cannot hold dower in a farm her
  husband never owned. Q-4 must answer either (i) she is joined in Joshua's deed or holds a debt against it,
  (ii) her exposure and her power are both the **homestead exemption** rather than dower, or (iii) she acts
  through the children. Q-4 is the next question.
- **Ages fixed once, everywhere:** Joshua 50 (1878), Jacob 45, Margaret 40s, Matthew 19, Caleb 21, Parrish
  35–40, Harper 60 (1879). `tools/check.py`'s age table carries these; the outline's "45–50" for Jacob is
  closed.

---

## 12. Chapter map v0 — POV-tagged (drafted against R-4)

Twenty outline beats in, twenty-seven chapters out. A beat that needs two chapters gets two; a beat that
is really one decision gets one and stops there (Pass 5). "J" = Joshua, "M" = Margaret.

| # | Chapter (working object-title) | POV | Beat it comes from | What changes practically |
|---|---|---|---|---|
| — | **ACT ONE: THE THRESHOLD** · summer 1878 – spring 1879 | | | |
| 1 | The Water Is Right | J | The World Before | The cove's economy is established in weights and a jug carried to Tyler's. The still seen from the outside, working. |
| 2 | Powder on the Ridge | J | (new, R-2) | Grading heard at night; a federal transit on the next ridge. The second chain-and-book front is planted before the first one is. |
| 3 | The Office | J | The Arrival of the Excise | Parrish opens; he calls on the judge, the sheriff, the leading men — a meeting **Joshua attends and Harper attends** (Q-8). |
| 4 | What a No Costs | J | The Recruitment of Joshua | Parrish asks for names; Joshua refuses. Under R-6 the last page is not about principle at all: it is his own mortgage, and the fact that the still sits in *his* barn. |
| 5 | Keep Making It | J | Jacob Understands + the cove's choice | The cove decides to continue and to not-know. Shown as a technique with rules, not as a mood. |
| 6 | Gauger's Work | J | The Standoff Begins | Parrish measures the farm as legally as the still: a still in a barn makes the *land* the case (R-3). |
| 7 | The Store Debt | J (Matthew in dialogue only) | The Temptation | Tyler's book, what Matthew owes, and what the informer law now actually promises (Q-7). |
| 8 | The Notice | **M** ←was J | End of Act One | The libel names the property, not the man — and it is addressed in part to her interest. R-4/R-5 put the paper in Margaret's hands here so that Act Two's dower chapters have a root. Act One ends on the notice, unanswered. |
| — | **ACT TWO: THE WEIGHT OF IT** · 1879–1880 (retitled; "THE RECKONING" goes to Act Three) | | | |
| 9 | The Empty Year | J | The Empty Year | Harvest without a distiller; the term list; two years of arithmetic started. |
| 10 | Margaret's Book | **M** | (new, R-3/R-4) | She reads the posted notices because they name an interest that is hers — under what, Q-4 has to say since R-6 took the dower for granted. Her accounts become evidence. |
| 11 | The Name | J | The Name | The cove learns who informed; Joshua is told; he does not say it. |
| 12 | Johnson City | J | The Fall's aftermath | Matthew's injuries arrive as objects and a doctor's sentence; no interiority for him, ever. |
| 13 | The Burning | J | The Burning | A barn the government would have had to litigate for is destroyed. Parrish did not order it. |
| 14 | The Missing Page | J | The Network Spreads | Joshua reads what is not in the file: Parrish's unsigned order. **Proposed addition, awaiting ruling:** Parrish stops questioning Jacob and puts the knowledge question to *Joshua as owner in fee* — what was your brother doing under your roof — which is R-6's payoff and the book's legal center. `OPEN` |
| 15 | First Blood | J | The First Blood | A deputy is killed. The cove's war becomes the crime the Bureau was built to answer. |
| 16 | The Letters | J | Jacob's Letters + End of Act Two | Prison correspondence in two hands; Joshua's arrangement closes; the sentence's length is fixed. |
| — | **ACT THREE: THE RECKONING** · 1880–1881 (ends autumn 1881 per R-5; no train) | | | |
| 17 | "We End It." | J | The Plan / Caleb's line | Caleb organizes; Joshua watches and does not stop him. |
| 18 | The Warning | J | The Network Spreads | The nod as policy. Joshua is now complicit in something he can price. |
| 19 | The Ambush | J | The Ambush (partial) | Parrish is hit. Long sentence for the mountain, then four-word declaratives. Wound and side pinned in §10. |
| 20 | The Search | **M** | The Manhunt | The house is searched. Margaret asserts standing the searchers must answer to. |
| 21 | The Surrender | J | The Capture | Joshua decides what Caleb is worth to the cove, and says so (he tells the name). |
| 22 | The Term | J | (new, Q-10) | Statesville, third Monday in April; a rented courtroom; the schedule of a circuit. |
| 23 | Did He Know? | **M** | The Broader Tragedy / the trial | The government's real question, aimed at Harper: knowledge and permission. Margaret's testimony is the hinge. |
| 24 | The Return | J | Jacob's Release and Return | Two years out; the farm gone or halved (Q-4); the law is not cruel, it is complete. |
| 25 | The Mill Sold | J | Joshua's End | He sells, he leaves; the only Brennan who dies where the streets have names. |
| 26 | The Far Side of the Ridge | J | (new, R-5) | The mill sold, the walk up, a blast from the wrong side of a ridge — and he does not go and look. The book stops there. No engine, no rails, no lesson. |
| — | *Print* (optional epilogue) | — | Epilogue (Q-9) | If kept: paper only — a county history, a campaign pamphlet, or a dime-novel chapter titled for Caleb. Under R-5 this is the **only** place a date past 1881 may be printed, and the title page date follows it. `OPEN` |

**Accounting (26 chapters):** Joshua 22 whole chapters plus the interior of the shared ones; Margaret 4
whole (8, 10, 20, 23) — about 15% by count, which lands near the ruled ~20% by words only if her chapters
run long, which they should: hers carry the paperwork. Measured by words at Pass 4, not by count. If it
reads 85/15, give her the search of the house in Act One; do not take a chapter back from Joshua.

**Movement this map invites:** ~~Q-2~~ decided 26 (R-5); Q-4 decides 8, 10 and 23; Q-8 decides whether 3 holds two old
men; Q-9 decides 27; Q-10 decides 22. Nothing else here is contingent on an unanswered question, so Act
One can be drafted now.

---

## 2. Timeline

Real dates are what the fiction is measured against. Everything in the right column is fiction.

| Date | World (real, `LEAD` unless noted) | *REVENUE* |
|---|---|---|
| Jul 1 1862 | First federal tax on distilled spirits, 20¢/proof gal | — |
| Jul 20 1868 | Act barring stills in or near dwellings; distiller's bond and owner-in-fee rules; forfeiture regime `LEAD` | The law Jacob has never obeyed |
| Jun 4 1872 | NC split into Eastern/Western Districts; Robert P. Dick appointed WDNC judge `LEAD` | Dick sits on Jacob's case |
| Aug 1872 | Informer moieties repealed; shares become discretionary payments of the Commissioner `LEAD` | The machinery that decides whether Matthew is paid |
| May 1875 | Whiskey Ring broken (Bristow); distillery raids 10–13 May `LEAD` | Why Washington now wants a man in the mountains who is *not* on the take |
| Mar 3 1875 | Rate fixed at 90¢/proof gal (until Aug 27 1894) `LEAD` | The exact number in every assessment |
| Aug 1876 | Green B. Raum Commissioner of Internal Revenue `LEAD` | Parrish's mandate |
| Summer 1878 | The cove; Jacob's still; barter at Hoss Tyler's | **Act One opens** |
| Autumn 1878 | Raum-era crackdown in western NC ("moonshine war") `LEAD` | Parrish arrives in the town below the gap |
| Winter 1878–79 | Raids on unconnected stills; two arrests | The standoff; the boy on the ridge |
| Spring 1879 | — | Parrish turns to Matthew; the raids; Jacob arrested |
| Summer–Fall 1879 | U.S. District Court term, WDNC `OPEN` (where, what month — see R-Q3 in audit) | Jacob sentenced: 2 years, U.S. v. Brennan |
| Late 1879 / early 1880 | — | Harper's barn burned |
| Sept 1880 | ET&WNC construction under way in earnest `LEAD`, dates contested | Blasting heard from the cove; men leave for the grade |
| Early 1880 | — | The deputy ambushed on the road ("First Blood") |
| Mid 1880 | — | Joshua tells Caleb the informant's name |
| Late 1880 | — | The ride to Johnson City; Matthew beaten, exiled; Act Two closes on the ridge |
| 1880–81 | Grant dies 27 Jul 1885 (far ahead); Garfield assassinated 2 Jul 1881 `LEAD` | Act Three: the ambush on Parrish; the manhunt |
| Aug 25 1881 | Redmond tried in Charlotte (8 liquor counts, 2 conspiracy counts; 10 yrs Auburn; $2,600) `LEAD` | The template for Caleb's case — see §6 |
| 22 Aug 1881 | Track to Hampton, TN complete `LEAD` | The steel is now a day's walk away |
| Late 1880–early 1881 | — | Jacob released; returns to a broken cove |
| Mid-June 1882 | ET&WNC reaches Elk Park `LEAD` | **Outside the fiction's present tense. Under R-5 the train never appears; this date may only be reached by a printed document (Q-9), or spoken of as a rumor of spring.** |
| 3 Jul 1882 | Line opens to Cranberry; iron moves; company town begins | The world the tax could not reach is reached anyway |
| 1895 | — | `INVENT` Jacob dies, never having distilled again |

---

## 3. Geography & jurisdiction

- **Country.** High coves of the Blue Ridge, northwestern NC, near the Tennessee line. Banner Elk /
  Elk Park / Cranberry district. Elevation ~3,200 ft. `USER` (Drive research doc)
- **County in 1878: WATAUGA.** Seat Boone. Watauga formed 1849 from Ashe, Caldwell, Wilkes, Yancey.
  **Avery County does not exist until 1911** — it is cut from Watauga, Caldwell, and Mitchell
  `LEAD`. Cranberry itself lay in **Mitchell** (from 1861) `LEAD`, so any record trail crosses county
  lines. **Q-12: which county is the cove in — it decides the courthouse, the militia memory, and the
  deed books.** `OPEN`
- **Fictional place names.** `INVENT` The cove is called **Elk Cove**; the hollow above the still is
  **North Fork Hollow**; the store is **Hoss Tyler's** at the junction road; the town below the gap is
  left unnamed in the outline and should be pinned — candidates Newland, Lincolnton, or a renamed
  Lenoir. `OPEN`
- **Distances (set these now and never vary them).** Still to Margaret's cabin: ___ ; cove to
  Tyler's store: ___ ; store to the town with Parrish's office: ___ ; town to the railroad grade at
  its nearest: ___ ; cove to the federal courthouse: ___ days on horse. `OPEN` (audit A-4)
- **Travel reality.** No railroad in the cove in the 1870s. Wagon over the mountains to Morganton or
  Elizabethton `USER`. The Yellow Mountain Turnpike is the route through the area `USER`.

---

## 4. Cast

Ages are **as of the year the outline first sets them**, and are fixed by **R-6** (2026-10-26): the
outline's contradiction — Joshua 45 but "older brother" of a Jacob aged "45–50" — resolved in favor of the
birth order. **Joshua is the elder: b. ~1828, 50 in 1878. Jacob b. ~1833, 45 in 1878.**

**JACOB BRENNAN** — b. ~1833, so **45** in 1878 (R-6). Younger brother. Distiller on his elder brother's
ground, which is the whole of his legal exposure and none of his self-image. Not a criminal in his own eyes
and not a political animal. Competence shown only through the still: water, drainage, the placing of a
garden. Engine consequence: the apparatus and his body are the libel's subject matter; **the land is
Joshua's**, so the forfeiture falls on the family's oldest bond rather than on a deed in Jacob's name.
`INVENT` the year of his father's death (see inheritance ask R-14); `INVENT` whether he fought for the
Union or hid. `OPEN` Q-5.

**MARGARET (Brennan, née ___)** — 40s in 1878. Wife, mother of the informer. **Currently the outline's
greatest deficiency: 6 mentions against Parrish's 39.** Under R-3 she has an independent legal
interest (dower/homestead) and therefore independent leverage no man in the book can exercise for
her. Proposed: she is the only character who can *convey* — sign away, or refuse to. `OPEN` Q-4.

**MATTHEW BRENNAN** — 19 in 1878. Jacob's son. Informs for Parrish; exiled; beaten to broken ribs and
a broken arm in Johnson City; never returns. Motive is **thin in the outline** ("ambitious,"
"not entirely convinced"). Three richer options and the 1872 moiety repeal as the instrument of his
ruin: he may inform to *pre-empt* worse for his father; he may be in debt at Tyler's store; he may
find Parrish's offer of a wage honest and take it. **Q-7: what does he do with the money, given that
Washington decides whether he is paid at all?** `OPEN`

**CALEB BRENNAN** — 21 in 1878. Jacob's nephew, and calls him "Father" in the prison scene. **Whose
son is he?** The outline never says. This is the best unwritten backstory in the file: it is why a
21-year-old has more at stake than the man whose name is on the still. `OPEN` Q-6.
Arc: hothead → organizer of the warning system → the man who decides the barn's burning is a line
crossed → ambush → fugitive → conviction.

**JOSHUA BRENNAN** — b. ~1828, so **50** in 1878 (R-6). Elder brother, heir to the farm, and the mortgagor
of it: the fee the government can reach is his (R-3 + R-6). Miller and trader. Refuses to inform in
Act One, refuses Caleb's intelligence request in Act Two, tells Caleb the informant's name anyway,
shelters the fugitive, sells out and leaves. **The only man standing in both worlds and the only
character who knows the informant's name and must decide whether to say it.** **Spine POV, ~80% — ruled
Q-1 → R-4.**

**WILLIAM PARRISH** — 35–40 in 1878. Federal revenue agent. Rifle, badge, orders. Courteous and
reasonable within his institution (Style Guide §1.3) — **which the outline honors in Act One and
abandons afterward.** Post-Whiskey-Ring Treasury wants clean convictions, not moieties; his promotion
in the third act option is a man given a bigger territory and no authority to buy a single neighbor.
Needs his own cost. `OPEN` Q-8.

**OLD HOSS TYLER** — storekeeper. Appears exactly once in the outline, yet runs the closed circuit the
book is about to break: the place where a jug becomes flour, salt, tobacco, cloth, and therefore where
a *price* — and therefore a tax — first becomes real. Obvious first man Parrish buys. **Q-9: promote
or cut.** `OPEN`

**WILLIAM HARPER** — 60 in 1879. Owns the barn; not a distiller; part of the network. Under R-3 he is
no longer a bit player: the entire moral turn of Act Two rests on whether **Harper knew**. One mention
in 3,300 words is not enough to burn a man's life work. Proposed fix: put him in the Act One barn
meeting as the old man who says *don't* and is outvoted. `OPEN` Q-9.

**THE COVE.** `INVENT` ~12 distilling families; the boy on the ridge (name? — candidate: **Elisha "Lish"
Councill**, 12); no Black families (contested — see §7 and Q-13); Baptist and Methodist meeting houses
`USER`; extended-family naming: use real Watauga surnames (Henson, Avery, Banner, Dugger, Calloway,
Brown) for the secondary cast so the census reads true `USER`.

**Honored real persons (do not fictionalize their acts):** Lewis R. Redmond (Transylvania/Swain; killed
Dep. U.S. Marshal Alfred Duckworth 1 Mar 1876; captured 7 Apr 1881; tried 25 Aug 1881 on **eight
liquor counts and two conspiracy counts, not for the killing**; 10 years at Auburn, N.Y., $2,600 fine;
pardoned by Arthur 1884; d. 1906 Walhalla, S.C.) `LEAD`; Judge Robert P. Dick `LEAD`; Commissioner
Green B. Raum `LEAD`; Dep. U.S. Marshal **Burns**, WDNC, shot in the back from ambush 13 Apr 1874
`LEAD`. Use in a `docs/` note, never as on-page dialogue.

---

## 5. Technical & legal mechanics (the plot engines)

Each must survive a reader with a calculator. All `LEAD` until primary confirmation.

**5.1 The tax.** 90¢ per proof gallon, fixed 3 Mar 1875, unchanged until 27 Aug 1894. History:
20¢ (1862) → 60¢ (Mar 1864) → $1.50 (Jul 1864) → $2.00 (Jan 1865) → 50¢ (Jul 1868) → 70¢ (Jun 1872)
→ 90¢ (Mar 1875). Proof gallon = one gallon at 100 proof. A run at 120 proof pays 1.2× the gallons.
- The arithmetic that makes the book true: a bushel of corn marketed at ~25¢ yields ~2.5 gallons of
  whiskey worth ~$1.25. **The tax is roughly the whole value of the whiskey.** `LEAD`
  Never state this as argument. State it as a man counting.

**5.2 Registration is not a formality — it is a property test.** No distiller's bond approved unless
he is owner in fee **unencumbered by mortgage, judgment, or other lien** of the land, or files the
written consent of the fee owner and every lienholder stipulating the United States's lien has
**priority**; sureties must own unencumbered real estate in the district equal to the appraised value.
`LEAD` Consequence: a mountain farmer with a deed of trust cannot go legal. This is the whole book in
one clause.

**5.3 Location of the still is itself the offense.** Act of July 20, 1868: no still, boiler, or vessel
for distilling in a dwelling-house, or in any shed, yard, or enclosure connected with one. `LEAD`
Therefore Jacob's placement "the way you'd place a garden" is a **legal choice, not a temperament.**
It is either a crime of the statute or a declaration of war. Author's ruling needed once, on the page.

**5.4 Forfeiture.** Still, apparatus, liquor, personal property on the premises, the distiller's
interest in the land, **and** the interest of any person who knowingly suffered, permitted, or connived
at the business. Seizure is in rem — **the libel names the property, not the man.** `LEAD`

**5.5 Informer pay.** Moieties repealed eff. 1 Aug 1872; shares thereafter at the discretion of the
Commissioner with the Secretary's approval, capped by regulation (not exceeding one moiety, nor more
than $5,000 in any case). `LEAD` **Matthew's betrayal is paid, if at all, by a letter from
Washington.** Do not let Parrish promise him a percentage.

**5.6 Penalties.** Distilling without bond / with intent to defraud: fine $1,000–$5,000 and
imprisonment 6 months–2 years (Rev. Stat. § 3281; Act of 1875 § 16: up to $5,000 and 2 years;
forged or fraudulent bond: 1–5 years). `LEAD` **Check Q-5 of the audit:** whether a 2-year sentence is
attainable in the Western District in 1879 for a first conviction, or whether Jacob needs two counts.

**5.7 Enforcement machinery.** Commissioner of Internal Revenue (Raum, from Aug 1876); supervisors
(per district; abolished 1883 by the Pendleton Civil Service Act `LEAD`); inspectors; gaugers;
deputy marshals, hired by the marshal and paid per prisoner — the reason a posse looks like
mercenaries `LEAD`. Removal of state prosecutions to federal court, and *Tennessee v. Davis* (1879),
a moonshine seizure pulled into federal court `LEAD`. Whether troops could be called: see
"The Army and Moonshiners in the Mountainous South" (Leavenworth thesis, ADA284658) `LEAD`.

**5.8 The trade, on the page.** Corn meal kneaded to a stiff dough, soured in the barrel; fermented
mash ("beer") run off; copper kettle, worm, wooden cooler; the **thump/dunkin' keg** — claimed
earliest in western NC in the 1870s `LEAD`, contested, and if it holds it is a gift. Proof tested by
the bead in a vial. Yield ~2.5 gal per bushel. Jugs, not bottles. `LEAD`/`USER` (Appalachian State
ethnography). **The Guide's rule applies: render this step by step and cut every ornamental simile.**

---

## 6. The cove's enemy, in institution terms

- **Washington's actual motive is revenue, not morals.** In 1870 liquor and tobacco produced roughly
  $55.6M of federal revenue against $18.7M in 1868 `LEAD`. The Whiskey Ring (broken May 1875; 238
  indicted, 110 convicted, ~$3M recovered; supervisors' transfers blocked by Grant before the ring
  fell) `LEAD` is why a 1878 agent can be sincere *and* be the reform: the Bureau had to be seen
  collecting somewhere it could. Parrish's intransigence is institutional, not personal.
- **The violence, sized honestly.** ~25 revenue agents killed 1876–80 in the mountain South (~6/yr),
  against ~20/yr for deputy marshals in the West; national coverage blew the mountain killings out of
  proportion `LEAD`. **This is the epilogue's real subject: not that the cove was violent, but that
  it was made legible as violent.** See Q-11.
- **Redmond as foil for Caleb.** Same years, same mountains, one man made into fiction while the facts
  were still warm (a Charleston reporter's interview in June 1878; a dime novel in 1879; a rival
  pamphlet in 1881) — and **no one hanged him for Duckworth.** His plea deal is the shape of Caleb's
  Act Three. `LEAD`

---

## 7. What the outline deleted, and must now answer

**Reconstruction is absent.** No Black presence, no church politics, no party named, no war memory — in
1878 North Carolina. `Rough Research` supplies the alibi (near-absent slaveholding in the high coves;
Burke County voting against secession; Unionist mountains) `USER`, and it is a defensible alibi for
*that* hollow. But "revenue" was not a neutral word in these counties: the postwar tax sales of
delinquent farms, the 1868 constitution and its schools, the Kirk–Holden war, and the railroad-debt
readjustment fight were all revenue fights. **Q-13: is the cove politically naive (unbelievable) or
politically shaped by what it lived through (a page and a half, and the whole book gets deeper)?**
`OPEN`

---

## 8. Voice rules for *REVENUE* (additions to the Style Guide; the Guide still governs)

1. **No eye dialect.** Cadence, grammar, economy, concrete nouns (Style Guide §5.3). Already house
   law; restated because this book invites the opposite.
2. **"Not X — it's Y" is at zero.** The outline commits the banned construction 7 times in 3,345
   words (28 total "not"s, 47 em-dashes, 8 "just"s). Facts carry the contrast; then stop one beat
   early (Pass 2).
3. **Interiority: only when alone.** The outline currently names feelings in scene ("Joshua is
   heartsick," "Parrish is alarmed and energized," "He's trapped," "Something crystallizes in Caleb,"
   "Matthew is tempted"). Every one is a rewrite to gesture, withheld answer, and hands.
4. **Day versus night is the music.** The trade is nocturnal; §3.3's bimodal rhythm maps onto it free.
   Long periodic sentences for the mountain and the wait; 4–12-word declaratives for the run, the
   blast, the fire, the shot. The outline already has four night set pieces — earn them all.
5. **Do they say "moonshiner"?** In NC these men were earlier **blockaders**, their product **blockade
   whiskey**; "moonshiner" becomes common in the 1870s `LEAD`. Proposed ruling (Q-14): the cove has no
   name for itself — they *run*, they *make* — and **"moonshiner" is always somebody else's word**,
   in print. That makes the naming a theme instead of a glossary. `OPEN`
6. **"Revenuer" is the derogatory.** Parrish objects to it once, out loud, and is corrected by a
   subordinate, not by a mountaineer.
7. **Numbers are spoken, not argued.** No character explains the tax rate. Somebody counts dollars.

---

## 9. Open questions — one at a time, in this order

Kevin rules each in chat. Each ruling moves from here to §1 as `AUTHOR` and out of the blocking list.

| # | Question | Blocks |
|---|---|---|
| Q-1 | **Whose spine?** | ✅ RULED 2026-10-26 → **R-4**: Joshua ~80%, Margaret ~20%. Chapter map is §12 |
| Q-2 | Does Act Three extend to June 1882 so the first train is a final **image**, or does it arrive as **coda**? | ✅ RULED 2026-10-26 → **R-5**: neither — ends autumn 1881, train heard about, never seen. Subtitle date 1878–1881 |
| Q-3 | Ages: is Jacob older than Joshua (b. 1831/1829) or is "older brother" wrong? | ✅ RULED 2026-10-26 → **R-6**: Joshua is the elder (50), Jacob 45; the forfeitable fee is Joshua's; Margaret's standing reopens as Q-4 |
| Q-4 | Does Margaret hold title, or dower, or nothing? Who can sign away the hollow? | Act Two, Act Three |
| Q-5 | Whose son is Caleb, and why does he call Jacob "Father"? | Whole book's engine |
| Q-6 | What does Parrish pay for, and what does it cost him? (Post-Ring Treasury; no moiety to promise) | Act One recruitment, ending |
| Q-7 | Matthew's motive, concretely — and does he ever get paid? | Act One turn |
| Q-8 | Promote Hoss Tyler and put Harper in the Act One meeting? | Act One scene list |
| Q-9 | Frame or no frame for the epilogue (author's note / fake print / ironic dime-novel voice)? | Last 10 pages |
| Q-10 | Which federal court sits where, on what term date, in 1879? | Trial chapter |
| Q-11 | Is "Whistlers" sourced or invented-and-owned? | Act Two network |
| Q-12 | Which county is the cove — Watauga, Mitchell, or Caldwell? | Records, deed trail |
| Q-13 | Reconstruction in or out? | Everything under the surface |
| Q-14 | "Blockader" vs. "moonshiner" — who says which word? | Vocabulary bible, linter |

---

## 10. Continuity anchors (linter-enforced; `tools/check.py`)

- **Ages (R-6).** Joshua 50 (1878) · Jacob 45 · Margaret 40s · Matthew 19 · Caleb 21 · Parrish 35–40 ·
  Harper 60 (1879). `tools/check.py` compares any parenthetical age in the manuscript against this list.
- **Injury sides.** Matthew: broken ribs — *which side*; broken arm — *which*. Once set, never vary.
- **Seasons elapsed.** Act One summer 1878 → autumn 1878 → winter 1878–79 → spring 1879. Act Two
  "empty year" 1879–80. Act Three 1880–**1881** (R-5: the present tense stops in autumn 1881; 1882 is
  reachable only by report or by a printed epilogue).
- **Distances** from §3, once set.
- **Sentence arithmetic.** Jacob: 2 years from the 1879 term. Any "about a year left in late 1880" must
  reconcile with the actual sentencing month **and** with credit — the outline's arithmetic does not
  currently close. Fix after Q-10.
- **Parrish's wound.** Hit in arm or leg (outline undecided) — pin side and limb; he is on the page
  afterward holding things differently.
- **Two ambushes.** Act Two's deputy and Act Three's Parrish must differ in texture or one goes.
- **POV ledger (R-4).** Every scene belongs to Joshua or Margaret. A scene that needs a fact only Jacob,
  Caleb, Matthew, Harper or Parrish could supply must get it from an object, a report, or a silence — and
  the linter's `lex:other-heads-interiority` row will flag the draft when the discipline slips.
- **Banned-from-this-book list:** "Whiskey Rebellion" applied to 1878–81 (belongs to 1791–94); **any
  train seen on the page at any date** (R-5 — the earlier rule "no locomotive before mid-1882" is now
  stricter: there is no locomotive, only the powder and the report of it); Avery County before 1911.
- **Closing sound (R-5).** The final beat's noise is a blast or a local hammer — never a whistle, never
  an engine, because Hampton was the rail head in October 1881. Pending ask R-13.

---

## 11. Change log

- **v1 (2026-10-26).** Canon opened from `OUTLINE: REVENUE` plus `docs/research-gaps-and-questions.md`.
  Rulings R-1 (novel), R-2 (railroad into the book), R-3 (land-forfeiture engine) recorded as binding.
  Four bibles stubbed in `docs/bibles/`; `tools/` ported from house architecture. 14 blocking questions
  in §9.

| 2026-10-26 | **Q-1 ruled → R-4** (Joshua spine ~80% / Margaret secondary ~20%). Added §12 chapter map
  v0, the POV-ledger continuity anchor, and the linter row for other heads' interiority. Also normalized
  the line endings of `docs/outline-v1-verbatim.md` (CRLF→LF, content untouched) so the linter's anchored
  patterns behave. | agent |

| 2026-10-26 | **Q-2 ruled → R-5** (ends autumn 1881; the railroad is heard about, never seen; subtitle
  1878–1881). Closed R-2's structural consequence, rewrote map ch. 26, moved ch. 8 to Margaret so the
  dower chapters have an Act One root, tightened §10 (a whistle is now banned outright — acoustic distance
  to the 1881 rail head), and added research ask **R-13**. | agent |

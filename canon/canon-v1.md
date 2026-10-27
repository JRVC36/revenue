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

**The acoustic constraint, because it will otherwise be drafted wrong.** Under **R-15**, the cove sits
above **Cranberry Forge and Elk Park** (`Cranberry Township, Mitchell County`), which is the exact
destination Ario Pardee's railroad is blasting toward. In October–November 1881 the nearest laid steel is
at **Hampton, Tennessee**, reached 22 August 1881 — **15.5 air miles** (~19.9 rail miles) northwest, locked
behind the 1,500-foot rock walls of **Doe River Gorge** and **State Line Gap**, so a locomotive's whistle
at Hampton still cannot carry into the cove `LEAD`. Meanwhile the grading and black-powder crews working up
Doe River Gorge, Roan Mountain (6.7 air miles), and Shell Creek toward State Line Gap in 1880–81 *are*
within genuine earshot across the state-line ridge. So the closing sound may **not** be an engine. What is
legal, and better:
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
  own at all. ~~so the still goes in **Joshua's** barn~~ **corrected by R-7: the still goes in the barn on
  Margaret's freehold, adjoining Joshua's ground.** The forfeiture now lands partly on the spine POV's deed
  (via "connected therewith") and partly on Margaret's — and Joshua is not the man watching the law come
  for his brother; he is the man the law comes for while it is there.
- **The knowledge question gets a better target.** *Stowell*: the owner's land is forfeit if he "knowingly
  has suffered or permitted" the distilling or connived at it. A neighbor's ignorance is plausible; **an
  owner's is not**, and the owner is the man who keeps every account in the cove. Parrish's sharpest move
  in Act Two is therefore to stop chasing stills (Jacob is already in federal prison from the April 1879
  Statesville term, R-13) and put the *Stowell* / "premises connected therewith" question directly to Joshua
  over Hoss Tyler's seized day-book exhibit (**RULED → R-18**, *The Missing Page*).
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

*R-7 `AUTHOR` (2026-10-26) — Margaret holds her father's tract in fee, as a married woman's separate
estate, and the still stands on it.** Under the North Carolina Constitution of 1868, Art. X §6, real
property a woman owned before marriage "shall be and remain the sole and separate estate and property of
such female, and shall not be liable for any debts, obligations, or engagements of her husband," and she may
devise or convey it "as if she were unmarried" `LEAD` (quoted in *Perry v. Stancil*, 237 N.C. 442 (1953),
reciting the 1868 text). Dower, meanwhile, had been *restored* in 1868 to the old common-law measure — land
the husband owned at any time during the marriage — after being limited to land owned at death since 1784
`LEAD` (legal-genealogy survey of NC dower statutes; needs the session-law cite).

Why this is the right instrument and not a convenience: **Jacob put the still there on purpose.** It is the
one piece of ground in the hollow his creditors cannot reach, the one deed no storekeeper's bond touches,
the only dirt in the cove whose encumbrances are not his. "The water is right" is the reason he gives;
this is the reason.

Consequences, binding:
- **R-6's barn moves.** Where R-6 said *the still sits in Joshua's barn*, read: **the still sits in the
  barn on Margaret's tract**, and Joshua's farm is the adjoining ground — the mill, the corn, the wagon
  road. (This correction is logged in §11; the two rulings are compatible, and the geography is now
  explicit rather than assumed.)
- **The libel names two tracts and the fight is the word "connected."** The 1868 act forfeits the lot or
  tract of land "connected therewith." Margaret's is the parcel with the still on it. Joshua's is one
  ridge over, joined to it by a water race, a cart road, and the fact that the mash is ground at his mill —
  so Parrish's second move, and the one that makes him dangerous rather than merely correct, is to argue
  **the two places are one premise**. `LEAD` on the statutory phrase; the argument's strength is `INVENT`
  and must be built out of what an 1878 appraiser could actually walk.
- **Knowledge is now aimed at the woman, and she is the one character who can answer it.** Under *Stowell*,
  an owner's land is forfeit where he "knowingly has suffered or permitted" the distilling; under
  *Dobbins*, **an owner forfeits even when the tenant's fraud was unknown to him**; and under *Two Barrels
  Whisky*, the interest-holder who genuinely did not know is protected. Margaret is the only Brennan whose
  innocence is legally *worth something* — and the only one whose admission is legally worth everything.
  Her Act Three scene is not testimony about her husband. It is the decision of whether to say a sentence
  that saves her land by damning her family or loses her land by saving nothing.
- **She can convey.** The separate-estate clause makes her the only person in the book who can sign away
  ground of her own — and NC required a **privy examination**, the wife's assent taken apart from her
  husband and certified by the officer, for any conveyance or husband's lease of a wife's land to be valid
  at all `LEAD` (N.C. Laws 1848–49, ch. 41; N.C. Const. 1868, Art. X §6; *Towles v. Fisher*, 77 N.C. 443
  [1877]; *Scott v. Battle*, 85 N.C. 184 [1881] — holding a *feme covert* cannot divest or charge her
  separate realty even by estoppel without written spousal assent and certified privy examination). **RULED
  → R-20 (*Did She Know?*, Ch. 26):** Margaret lays down her folded pre-1861 Watauga deed (sole copy after
  the 1873 Boone courthouse fire, R-15) and stands on the total absence of any certified privy examination,
  stalling the *in rem* decree against `Parcel B` into *E1*'s `"the tract remains in contest"` (R-12).
- **Old Councill's and Harper's parcels stay as the outline has them.** The cove's meeting in Act One is at
  **Joshua's mill** (his barn, his hospitality — the record of his not-knowing is a record of who he fed).
  The burned barn in Act Two is **Harper's** — storage, not distilling, which is why the burning is a crime
  against the government's own interest: it destroys the seizure, punishes the one man the forfeiture would
  have reached hardest, and leaves the United States with less to take. `USER`/outline.
- **The household goods are hers.** The outline's seizure of "the still, the worm, the tubs, a quantity of
  corn, the tools, and the barn itself" is now an inventory taken on a woman's freehold, and Style Guide
  §7.3 already demands the appraisement list of household goods that mean more than their price. That
  scene belongs to Margaret, in her own POV, item by item. `LEAD` on the appraisal mechanic (§5).
- **What this costs the marriage, stated once:** Jacob is calm in Act One because he owns nothing the law
  can take. He has spent twenty years being protected by his wife's inheritance, and the book does not let
  him say so, and does not let her either.

---

*R-8 `AUTHOR` (2026-10-26) — Caleb is Joshua's firstborn, raised in Jacob's house.** He is not a
nephew by courtesy: he is the elder brother's son, given to the younger. Every outline label survives
literally — he is a Brennan, he is Jacob's nephew, he calls Jacob "Father."

**The arrangement, in the order the family would give it and the order the cove gives it.** Joshua married
in 1856; Caleb was born in 1857; his mother died in the spring of 1862, in childbed with a second child that
did not live either — **that is why there are no other children, and it is why there was one to give.**
Joshua enlisted that summer, a man with nowhere to be, and left the boy with the only household he trusted,
his brother's. When the war ended and Joshua inherited the farm he had mortgaged before it, the boy stayed
where he was, and the cove retold the reason: *the elder has the land and the younger has the son.* Both
accounts are true, and the book should let them contradict. `INVENT` (the dates are arithmetic against the
outline's ages, not a claim about the world; nothing here may be printed as history).

Consequences, binding:
- **Matthew and Caleb were raised as brothers, two years apart.** The informer and the man who hunts him
  down are the same household. Act Two's beating in Johnson City stops being punishment for a crime and
  becomes a brother's job, which is why the outline's "beaten by his own family" line is the best sentence
  it has. Caleb does not beat Matthew because the cove ordered it. He does it because he was in the room and
  they were both Brennans.
- **Joshua's refusal in *What a No Costs* is now two facts that must never be joined in one sentence.** He refuses to
  inform, and the page of the ledger he turns to is the one with the boy's keeping-money on it. The
  narration must not connect them. The reader does it, in the second act, and feels like the first person to
  notice — which is the pleasure this book should be built out of.
- **Nobody says it. Not the narrator, not a hint, not once.** The relation is reconstructible from three
  planted facts and no statement (see §10, "the Caleb audit"). If a draft ever has a character explain it,
  the explanation goes.
- **Margaret raised him.** Under R-7 the woman whose freehold the libel is aimed at is also the woman who
  weaned the fugitive whose violence gave the government its reason to come. Her chapter-23 decision now
  has two costs and only one of them is legal: testifying to save her father's land damns the boy she
  fed. This is why "Did She Know?" is the right title for the trial chapter.
- **Caleb's stake becomes literal.** He is heir to both properties and to neither — his father's mortgaged
  farm, his mother-by-raising's freehold — which is what the outline means and does not know it means, in
  "a 21-year-old with more at stake than the man whose name is on the still."
- **The ending, which is what the ruling was really for.** Joshua sells the mill and leaves: a father
  walking out on the son he raised as his brother's, into a town where streets have names. Do not let him
  look back at the cove on the last page of *The Mill Sold*, and do not let Caleb learn where he went. The book's
  one mercy is that the two of them never say it in the same room.
- **Names, so the record is clear:** `INVENT` the mother as **Elsie Brennan (née Byrd)**, d. spring 1862,
  dead before the book opens, given one object and no scene (a shawl in a cedar chest that the appraisers
  list at forty cents in *The Cold Still* — the outline's seizure list already has to pass through that room; that is
  where a mother belongs in this book). Joshua does not remarry. `OPEN`: whether Elsie's name is ever
  printed at all (recommend: once, by Old Councill, in the wrong year, and nobody corrects him).

---

*R-9 `AUTHOR` (2026-10-26) — Parrish's cost is an audit: his victory is a complaint he has to answer.**
After the ambush the Department writes to him. Not to congratulate him — to ask, in the flat language of a
bureau that spent 1875–76 cleaning out the Whiskey Ring and had abolished the offending supervisors'
patronage power in 1883, why a raid was fought with hired local men, and why a barn was burned that the
United States had a claim on. `LEAD` on the reform context (§5, audit §3).

Why this is the right cost and not a subplot: under R-4 we are never inside him, so a cost that is
*experienced* is unavailable to us; a cost that is **corresponded about** is the only kind this book can
carry. His file is the one place the reader is allowed to read him.

Consequences, binding:
- **The unsigned order is now load-bearing in two directions.** It is the page the cove cannot produce *and*
  the hole in his own defense. He has two ways to answer the Department and both cost him: write that the
  burning was not ordered, and admit his deputies acted beyond instruction, which is the end of his
  authority in this district; or write that it was necessary, and admit in ink that the government destroyed
  property it was in the process of seizing. He writes the second one. `INVENT` the letter; the audit's row
  is what the letter has to be technically consistent with.
- **A scene the outline does not have: the deposition (RULED → R-19, *The Deposition*).** To answer
  Washington, Parrish needs affidavits, and the one affidavit that saves him is Margaret's — that he stood in
  the road calling his hired men off and did not order the fire, which caught in the split kegs of blockade
  whiskey stored on Harper's floor. So the man taking her land has to ask her to protect his career, in a
  room, with a clerk. She exacts `Elisha Councill`'s real name in his Commissioner's report first, then gives
  him one strictly true sentence that saves him with Washington and puts sworn proof of stored spirits into
  the federal record against the cove.
- **The book's paper survives because of the audit.** His compelled report is the reason a written record of
  this hollow exists at all, which is the single best source available to the epilogue if Q-9 chooses
  diegetic print: a county history or a Commissioner's report that quotes a man trying to defend himself.
  The irony is the book's thesis — the cove's only monument is an agent's exculpatory filing.
- **His ending, then, is a closing line.** The complaint is "closed without adverse finding." He keeps the
  office. He does not get the wound as a gift, and he does not get transferred out of the book's reach: the
  last we see of him is the file shutting, and the handwriting the reader has been able to read since
  chapter 3 unchanged, which is the cruelest thing available. `USER` (adapting the outline's Option 3, with
  the promotion demoted from victory to footnote).
- **Deputy naming, so a real man's death is not misattributed:** do **not** name our killed deputy
  **Burns** — W. Burns was a real WDNC deputy murdered in ambush, 13 Apr 1874 `LEAD`. Name ours something
  else and let Parrish *cite* Burns, the way a man cites the only precedent he has: **Burns's file was
  thinner than mine will be.** That line is his whole interiority under R-4, so it goes in once.

---

*R-10 `AUTHOR` (2026-10-26) — Matthew wants three things, in this order, and gets two of them.** He goes
to Parrish about a debt at the junction store; he asks that the raid be set on a day he chooses; he asks for
a paper with his name on it — a clerk's place, a deputy's start, anything. **Granted, granted, refused.**

- **The store (granted, and not to him).** The debt is real and small — half a mule, a doctor's visit for his
  mother in the winter of 1877, a plow blade on the book. Parrish settles it with Tyler directly. Matthew
  never holds a dollar. The **only trace is a line in the store's day book: "by order of the agent."** That
  line is now the most important object in Act One, because it is the document that proves *who knew what* —
  Tyler's book, not a confession. **This pre-decides half of Q-8: Hoss Tyler is promoted and his day book is
  the exhibit.**
- **The day (granted, and it kills somebody).** He trades the name of a day for the guarantee that the still
  will be cold and the men will be home. The guarantee fails at the edge of the plan: **Elisha "Lish"
  Councill, 15**, a widow's boy from North Fork carrying a jug he was not making, is shot behind Harper's
  barn by a deputy the book never names — only numbers. The cove's later patience with the government rests
  on that shot, and so does Matthew's silence.
- **The paper (refused).** Nineteen, landless, and the only person in the hollow who has read a notice all
  the way through, he wants to be on the winning side of paper. The Bureau does not commission mountaineer
  boys, and Parrish — by then building the file that will be audited (R-9) — will not put a promise in
  writing at all. The refusal is *courteous*, and it is the only kindness in the book that costs somebody
  everything.
- **Whether he is ever paid:** the discretionary allowance is fixed months after the exile, under the rules
  that replaced moieties in 1872 — an amount the Commissioner chooses with the Secretary's approval. It
  arrives as a Treasury order at the office in town. **It is never cashed.** It goes back to Washington with
  the clerk's notation **"person unknown,"** which is the book's last word on what his father was worth on the
  open market. It appears once, in a document, after Matthew has left the novel. `LEAD` on the mechanism
  (audit §3), `INVENT` on the returned order (ask **R-19**).
- **What R-4 costs here, and why it is worth paying:** Matthew gets **no interiority at any point**. So the
  three asks must be legible as three *objects*: a line in a day book, a date spoken once and kept, and a
  letter of appointment that is never written. If a draft needs more, the fix is a different object, not a
  thought.
- **The exchange this opens between Margaret and Parrish (RULED → R-19, *The Deposition*):** her affidavit
  about the fire has a price, and it is not money. She signs that Parrish stood in the road and did not order
  the burning only after the boy's name goes into the Commissioner's report **right** — the file calls him
  `"a boy"`, the cove calls him Lish, and *E1* prints **`Elisha Councill`** because she made him spell it.
  That is the moral trade of this book, and it is a spelling.

---

*R-11 `AUTHOR` (2026-10-26) — both minor men are promoted, and Tyler is neither bought nor a traitor:
he is a creditor.** The store's day book records the cove because a creditor's book always does. When Parrish
needs it, nobody betrays anybody: the book is taken in a seizure, **Tyler protests the taking in writing, and
his own protest is the instrument that puts the entries before the court** — the exhibit is authenticated by
the man who wants it back. `OPEN` on the mechanism (ask **R-20**: how a day book was compelled or captured in
a WDNC revenue matter, 1879–82, and whether a merchant's book was evidence of its own contents in a North
Carolina court then).

Consequences, binding:
- **The only man in the hollow who profits twice on the same boy.** Parrish settles Matthew's debt with Tyler
  at par, in coin, on the agent's order — so the storekeeper collects what no farmer can collect and keeps the
  rest of the cove's accounts open. He is not corrupt; he is paid. That is the book's argument about paper,
  delivered by a man who never does anything.
- **He keeps his book honest on purpose.** An entry made in ink the day it happens is the difference between
  a debt and a grudge, and Tyler knows it. Two lines of his are load-bearing later: the "by order of the
  agent" line, and an entry the reader can price — a pair of boys' shoes, in a year Jacob had one child
  (R-8's second planted fact, now housed in the store rather than in Margaret's book, which is better: the
  cove's arithmetic is kept by the man who sells arithmetic).
- **Harper goes into the Act One meeting as the man who says *don't*.** The outline has him in three mentions
  and does not have him in the barn; R-11 puts him there, outvoted, saying one sentence short enough to be
  quoted back at him in Act Two. Then the raid that kills Lish Councill happens on his ground, and the
  burning that turns the cove from evaders into murderers is done to **the one neighbor who was right in Act
  One** — which is how this book says what it has to say about being right: it is not a defense, it is only a
  forecast.
- **Harper's knowledge is the forfeiture's second target and the easier case (reconciled R-19).** He is not
  the man with the separate estate; he is the neighbor whose floor Caleb's network used to store blockade
  whiskey over his Act One *don't*, which under *Stowell* is "suffered and permitted." When Parrish raids that
  storage barn with hired local possemen (*The Burning*, Ch. 14), his hired men stave in the kegs and set the
  barn afire without Parrish's order — burning property on which the United States already held a claim, and
  triggering Caleb's lethal answer in *First Blood* (Ch. 16).
- **The punishment lands on the wrong person and the book refuses to point this out.** Caleb's arc (R-8) is a
  boy defending a household; Harper's is a man losing the barn he raised for having warned them. No speech for
  Harper. A doorway in *The Burning*, standing, with his sons — and one line in Act Four only if the pacing survives
  it.
- **Cast arithmetic, so nobody is invented twice:** Hoss Tyler **63** (b. ~1815), widower, one son in
  Tennessee (`INVENT`, unused unless a letter is needed); William Harper **60** (b. ~1819), four sons, no
  still, one barn at the junction road with a proper floor for storing. Both names come from the outline, and
  neither is moved off its outline function — only onto the page.

---

*R-12 `AUTHOR` (2026-10-26) — the ending is diegetic print and nothing else: no author's note, no
narrator's future tense.** After the last chapter (which stops in 1881, per R-5), the book carries the reader past the
date in **three documents only**, each in the voice of the institution that wrote it. This is the ruling that
makes the epilogue's form the book's argument: the cove has no monument except an agent's filing.

**The three artifacts, in this order, and nothing between them:**

1. **The report.** William Parrish to the Commissioner of Internal Revenue, dated **Washington, D.C., or
   Asheville?** — see the open item — but signed from the district, **1882**, on the subject of the western
   district's 1881 operations. In it: the stills seized, the convictions, the burning "not ordered by me and
   not prevented," the informer's allowance returned uncashed with the notation *person unknown* (R-10),
   and **Elisha Councill, killed while carrying whiskey he did not make**, spelled right. One sentence of his
   own, and no more than one: that the people of these mountains are not disaffected so much as
   unaccounted for, which is the truest thing anybody in the book says and it is said in the language of a
   man asking for a raise.
2. **The county history.** A paragraph from an 1880s–1890s county history — the type every western NC county
   got — that narrates the same affair in the register of improvement: the revenue law "was enforced with
   spirit," a party of desperadoes, and **one date wrong by exactly two years** (the raid placed at 1877,
   before the agent arrived). Caleb is named, wrongly, as the leader of nothing in particular. This is where
   the book's other half lives: the mountain's own story, told by the people who bought the press.
3. **The title page of a dime novel.** Not an excerpt, not a passage — **a cover and a chapter list**, set
   as front matter was set: `CALEB BRENNAN, THE BOY BANDIT OF THE BLUE RIDGE; or, The Whiskey War in the
   Mountains.` Four chapters, no more, and the last title is the lie the whole book was written to make
   audible: `CHAP. IV.—HOW HE SAVED HIS BROTHER, AND THE GOLD OF THE GOVERNMENT.` Nothing in the cove is
   named correctly in it, and it sells.

**Why the third artifact is a title page and not prose:** the outline's epilogue options were "titles or
voiceover," and R-1 translated voiceover into interiority. A title page is the one form that lets the book
finish in **typography** rather than in a voice — it is the only ending available to a novel whose rule is
that nobody explains anything. (It also copies the real thing exactly: Redmond's own 1879–81 pamphlet-and-
dime-novel afterlife is documented, and that is what this is for.)

**Binding handling rules:**
- **No author's note, no acknowledgement of accuracy, inside the book.** The verification record stays in
  `docs/period-audit.md`, which is where it does its work. If a reader wants to know what is true, that is a
  question for the back matter of a *second* printing, and the author can decide that when there is one.
- **The artifacts are never quoted back.** No character reads the report aloud, no one mentions the county
  history, and nobody in the cove ever hears of the dime novel. The distance between the three documents and
  the last human scene **is** the ending.
- **Aftermath, apportioned:** everything the outline wanted to say in its optional epilogue scenes goes into
  these three documents and nowhere else — Jacob's 1895 death **does not appear** (the book has no right to
  it; if it must exist, it belongs in the county history's next sentence, in the past perfect, about a man
  nobody there remembers the name of), Margaret's fate is a line in the report ("the tract remains in
  contest"), and Caleb's is the dime novel's existence. Joshua gets nothing. He is the one the documents
  cannot reach.
- **`INVENT` register discipline:** the report must not be *literary*. Sentences with subjects like "the
  operations," verbs like "resulted in," and no adjectives at all. The county history may be literary in the
  worst way. The dime novel may be the only ecstatic prose in the book, and it is a list.
- **Title page date stays 1878–1881** (R-5). The epilogue's documents may carry later dates *within*
  themselves; the frame does not move. This is the rule that makes R-12 legal, so it is written twice on
  purpose.

---

### R-13 · Where and when the cases are heard: **Statesville, on the real term dates, with the real judge named and never voiced**

`AUTHOR` (2026-10-26), answering **Q-10** (Statesville with real term dates / an invented town / Statesville
but the book skips it / a special commission sitting in the mountains).

- **Statesville, and the book goes there.** The Circuit Court for the Western District of North Carolina sat
  at Statesville on the **third Monday in April and the third Monday in October**, and it was the only
  courthouse the district had: the United States did not build one in Asheville until **1892**. So every
  federal case in these mountains was a trip of three days down the mountain, heard in a rented room, on a
  day fixed by statute years ahead. `LEAD` (term calendar from the NC Reports front matter; NC History Journal
  on the district); the term-openers below are computed from that rule, not read off a printed calendar.
- **The dates, now fixed for the whole book.** The spring term **opened Monday 21 April 1879** — that is
  Jacob's conviction, two years, which is the statutory maximum for keeping a still without a bond, so his
  **release is 21 April 1881**. The autumn term **opened Monday 17 October 1881** — Caleb's trial. The closing
  chapters run to **November 1881** and the epilogue's documents to 1882, which puts the last page about
  **seven months** before the rails reach Elk Park (mid-June 1882): "come spring" in *The Mill Sold* is
  exactly right, and the train stays out by a margin small enough to feel like timing rather than authorship.
- **What the calendar bought, in order.** (i) The term list becomes the cove's almanac: a mountain household
  plans a wedding, a crop loan and a flight around the days court sits. (ii) The sentencing arithmetic closes
  to the day, so the outline's "about a year left" can be fixed instead of fudged. (iii) It moved a chapter:
  because Jacob is out in **April** 1881 and Caleb is tried in **October**, *The Return* now precedes
  *The Surrender* — he comes home to a house that has become the site of a second case and to a wife who has
  been running it, and then watches his nephew's trial from the gallery of a man who has already sat in that
  room. The outline put the release after the capture; the statute said otherwise, and the statute wins.
- **The one line in the outline to fix.** "He has about a year left in prison" → **"a year and more"** if the
  chapter sits in the winter of 1879–80, or **"not half a year out"** if it sits in late 1880. Pin the
  chapter's month first, then write the line. Do not write "about a year" and hope.
- **Judge Robert Paine Dick is named, seated, and never given an invented word.** He held that bench from 1872
  to 1898: a Unionist who left the bench when the war came, sat in the Confederates' legislature afterward, was
  barred from the 1870 general assembly by the ironclad oath, and was put on the federal bench by Grant — the
  living proof of the claim Act One is about. He is in the book the way the rest of the machinery is: **in the
  docket heading, in the walk to the hotel, in what the cove says the court will and will not do.** No invented
  line of dialogue in his mouth; no invented holding on his name. Anything the court rules is attributed to
  "the court," and the wording is marked `INVENT` in `docs/period-audit.md`.
- **Why not the alternatives.** An invented town would cost the audit trail and the whole R-4 premise — the
  reader must be able to check this — and there is no plausible county seat to invent within a day's ride of a
  Mitchell hollow, because the county seats are all real. Skipping the court would hide the law's face at the
  moment this book exists to show it, and would leave the sentences unanchored. A commission sitting in the
  mountains is unconstitutional for a revenue case and reads as alternate history.
- **The cost of the trip is a fact, not scenery.** Statesville is three days each way, with a hotel and a
  horse to feed: in a cove that counts in cents, **someone has already priced going to court before anyone is
  asked to go.** Put that arithmetic in the ledger, not in a speech.

---

### R-14 · **"The Whistlers" is kept, invented and owned — and only outsiders ever say it**

`AUTHOR` (2026-10-26), answering **Q-11** (own it / cut it / swap to "the Regulators" / both layers).

- **The ruling.** The name stays, marked `INVENT`, and it is **never** a name the hollow uses for itself. It
  exists only in print that is written *about* the cove: Parrish's reports and the libel's marginalia, the
  Charlotte paper, and finally the dime novel in *E3*. Inside the hollow the company has no name, because
  naming a meeting is evidence and the men's whole technique is that there was no meeting (R-3's
  not-knowing, expressed as vocabulary). `tools/check.py` flags every occurrence so the speaker is checked.
- **The outline already conceded this, and the ruling takes it seriously.** The source line says *"a group
  called 'the Whistlers' **or some other name**, though historians aren't entirely sure how organized they
  were."* So the book does not invent a fact; it invents **the record of a fact**, which is the same move the
  source makes and the same move the Whiskey Ring and the 1878 pardon narrative make in Washington papers.
  The Bibb County, Alabama "Regulator" revenge killing of February 1879 stays in `docs/period-audit.md` as
  the *structural* echo — a revenue-war story where the press named the men — not as a citation.
- **Why not "the Regulators."** In North Carolina it imports 1768–71 and the Tryon County regulators, which is
  a real mountain precedent for "we correct the officers" and therefore a temptation a reader will read as a
  thesis. The book already has one argument; it does not need a borrowed name with a two-hundred-year
  bibliography. (If the author ever wants the precedent, it belongs in Old Councill's speech as a story about
  somebody else's great-grandfather, not on the band.)
- **The word does double duty, and the double duty is not explained.** A whistle is the signal on the ridge —
  which is why the papers call them Whistlers — and a whistle is also the sound the book refuses to give the
  reader (R-5: no engine, no rails, one blast off a ridge on each side of the novel). The overlap is
  **allowed to be coincidental**: never annotated, never drawn out, never in the same paragraph as the grade
  work. If a draft puts the locomotive and the signal in one sentence, cut the sentence; the reader will make
  the connection alone, which is the only way it is worth anything.
- **What it changes in the mechanics.** (i) Act Two's organizing chapters have **no banner**: no oath, no
  title, no minutes — the only "minutes" that exist are the revenue agent's. (ii) The best small scene in Act
  Three is a clerk writing the word and a man in the room not correcting him. (iii) *E3*'s title page is where
  the name finally becomes true: by 1882 the invented label is the only thing anybody remembers, which is the
  epilogue's argument (R-12) in one noun. (iv) `docs/research-gaps-and-questions.md` ask **R10** closes as
  owned-invention: no archive will settle it and none needs to.

---

### R-15 · Where the hollow sits: **near Cranberry Forge and Elk Park — in Mitchell County (1861–1911), not Burke, with Burke and Watauga in the deed box**

`AUTHOR` (2026-10-26), answering **Q-12** ("The setting is near Cranberry or Elk Park, NC. At this time I
believe them to be part of Burke county").

- **The place is locked (`AUTHOR`); the county name on the 1878 docket is corrected to the record (`LEAD`).**
  The cove sits in the high Elk River / Cranberry Creek country (~3,200–3,500 ft) between **Cranberry Forge**
  and **Elk Park**, under the Tennessee line. In **1878–1881**, both Cranberry and Elk Park lie in
  **`Cranberry Township, Mitchell County`** (county seat: **Bakersville**, est. 1868; 1880 township pop. 1,174
  including Elk Park village), *not* Burke County.
- **Why "Burke County" was in the Drive notes, and why that succession is a gift to the plot.** Without a
  boundary stone moving in the creek, that single valley sat under **five county names in eighty-five years**:
  1. **Burke County** (1777–1833; seat **Morganton**) — where the 1780s–1820s state land grants and the 1826
     Cranberry iron-forge entries were recorded (`Rough Research` collapsed 1833–61 into "Burke," which is how
     the misimpression arose; Burke ceded its last northern sliver at Linville Falls when Mitchell was created
     in February 1861).
  2. **Yancey County** (1833–1849; seat **Burnsville**).
  3. **Watauga County** (1849–16 Feb 1861; seat **Boone**) — e.g., the 1852 Hardin bill of sale at Cranberry
     Forge is registered in Watauga; Banner's Elk, 5.4 air miles east over the ridge, *stayed* in Watauga.
  4. **Mitchell County** (**16 Feb 1861 – 23 Feb 1911**; seat Childsville/Calhoun, then **Bakersville**).
  5. **Avery County** (**23 Feb 1911–present**; temporary seat **Elk Park** 1911–12, then **Newland** — both
     `BAN` as county/seat names in 1878–81).
- **What the four-courthouse trail buys for R-3, R-6, and R-7.** A family holding ground above Cranberry Forge
  in 1878 carries three courthouses in one cedar box: a grandfather's grant headed **Burke** (whose courthouse
  records at Morganton were burned in Stoneman's Raid, April **1865**), an antebellum deed or inheritance
  headed **Watauga** (whose courthouse at Boone **burned 23 March 1873**, five years before Act One opens,
  destroying the county's deed books), and the postwar instruments — **Margaret's 1866–68 separate-estate
  deed** and **Joshua's mortgage** — recorded in **Mitchell County** at **Bakersville**. For any pre-1861
  link in the chain of title, **the clerk's book is ash and the folded sheet in Margaret's box is the only
  copy in the world.** **RULED → R-20:** in *Did She Know?* (Ch. 26), Margaret produces that unburned
  pre-1861 Watauga deed and stands on the absence of any certified privy examination in Bakersville, which is
  no longer an author's contrivance; it is how Toe River titles worked after 1873.
- **What it changes for R-2 and R-5 (the railroad).** Placing the hollow near Cranberry and Elk Park puts it
  at **the exact target of the railroad**: Ario Pardee's Cranberry Iron & Coal Company is driving the 3-foot
  ET&WNC narrow gauge up from Johnson City specifically to haul Cranberry magnetite, crossing State Line Gap
  to **Elk Park** in mid-June 1882 and terminating one mile south at **Cranberry** on 3 July 1882. That
  sharpens R-5's acoustic rule: the August 1881 railhead at **Hampton, TN** is **15.5 air miles** (~19.9 rail
  miles) away behind the 1,500-foot rock canyon of **Doe River Gorge**, so a locomotive whistle still cannot
  reach the cove, while the 1880–81 black-powder blasting crews in Doe River Gorge, Roan Mountain (6.7 air
  miles), and Shell Creek are genuinely audible off the state-line ridge, and "at Elk Park come spring" in
  *The Mill Sold* is news about a clearing three miles from Joshua's wheel.
- **Period state of the real settlements (anachronism guard):**
  - **Cranberry Forge** is the official post-office name through **24 April 1884** (est. 1840/1850, reopened
    Nov 1868; shortened to *Cranberry* in 1884). Speech may say "Cranberry" or "the Forge"; **do not** put
    Pardee's post-July-1882 company hotel, company housing rows, or mine scrip in 1878–1881 — before the rails,
    the ore pits and old bloomery are worked intermittently and hauled out by wagon.
  - **Elk Park** in 1878–1881 is an unincorporated border meadow and crossroads on the Elk River inside
    Cranberry Township, one mile north of the Forge at the Carter County, TN line. **No post office (May 1883),
    no town charter (1885), no depot or boarding-house boomtown** until the rails arrive after the book ends.
  - **Newland** does not exist until **1911–12**; in 1878 that meadow ten miles south is called **Old Fields
    of Toe** (`BAN` on `Newland` in `tools/check.py`).
- **Courthouse & travel arithmetic, now fixed across §3 and §10:** local county seat = **Bakersville** (14.1
  air / ~22 road miles down the North Toe, **one full day on horseback**; sheriff, register of deeds, posted
  notices, and Parrish's county office days); eastern wagon market = **Morganton** in Burke County (~45 wagon
  miles down Yellow Mountain Turnpike, two days); western market = **Elizabethton / Johnson City, TN** (~20 /
  ~34 miles down the Doe River, one day to a day and a half — Matthew's exile and Caleb's ride); federal court
  = **Statesville** in Iredell County (~90 road miles across Burke and Catawba or Caldwell and Alexander —
  **three county lines crossed, three days each way on horseback**, matching R-13 to the hour).

---

### R-16 · 1861–1876 in the hollow: **in as bone structure — the Union coat, the 1862 war tax, and the 1868 deed, carried in objects with zero speeches**

`AUTHOR` (2026-10-26), answering **Q-13** (bone structure in objects / 1862–65 war split only / sealed cove /
onstage party politics).

- **The ruling.** The war and Reconstruction are **in**, never as a speech or a party argument, and carried
  entirely in **two ironies made of paper and cloth**:
  1. **The Union coat and the 1862 liquor tax.** Northern Mitchell County along the Tennessee line was strongly
     Unionist (`LEAD`: 84 Union enlistments from tiny Mitchell Co., chiefly into the `13th Tennessee Cavalry
     (U.S.)` and `3rd North Carolina Mounted Infantry (U.S.)`, after 1862 scout crossings over State Line Gap).
     When Elsie died in spring **1862** (R-8), **Joshua walked over the Tennessee line and enlisted for the
     United States**, mustering out at **Knoxville in late summer 1865**. Congress enacted the federal tax on
     distilled spirits (**Act of July 1, 1862**) that same summer to pay for the war he fought. Seventeen years
     later, **the government coming for Joshua's mortgaged deed is his own army, collecting on the statute that
     fed him.** Nobody in the book ever says this. It sits in one drawer in *What a No Costs*: a folded 1865
     Knoxville discharge beside the mortgage receipt and the keeping-money ledger. *(Guard: do **not** print an
     invented company letter or regiment number on the page — because the formal NC/TN Union regiments mustered
     1863–64 after 1862 pilot/scout service, "went over the line in sixty-two, discharged at Knoxville in
     sixty-five" is period-proof without risking a muster-roll anachronism.)*
  2. **1868 lives in the room as paper, not politics.** The **1868 North Carolina Constitution** — the
     Reconstruction charter that replaced the old county court with townships (`Cranberry Township`), raised
     property levies, and set off the delinquent-land **tax sales** that taught mountain households to distrust
     every posted notice — is **the exact instrument (`Art. X §6`) that makes Margaret's forty acres a married
     woman's separate estate** (R-7). Every Brennan owes their only shield against creditors to the settlement
     the cove resents. Again, never argued: it is visible in the year `1868` on Margaret's deed and in the
     courthouse's township books at Bakersville.
- **Jacob's 1862–65 record is closed, and it locks R-8 shut.** At twenty-nine in 1862, **Jacob stayed on the
  mountain**: cutting wood and hauling around Cranberry Forge enough to stay off the early conscript lists,
  lying out in the laurel when the Home Guard swept the creek, and **keeping five-year-old Caleb for the three
  years Joshua was gone**. That three-year absence — not a family speech — is **how Caleb came to call Jacob
  "Father,"** and why Joshua rode home from Knoxville in August 1865 to a son who belonged to another table.
  `INVENT` grounded in `LEAD`.
- **What stays strictly OUT.**
  - **No Klan subplot.** Western NC's 1868–72 Klan-and-revenue violence centered down the escarpment in
    Rutherford, McDowell, and Polk counties, not in Unionist Cranberry Township `LEAD`; importing night-rider
    oaths would also violate R-14 (the cove's resistance has no banner, oath, or minutes).
  - **No party stump speeches** — no debates over Vance, Holden, Greenbackers, or "Reconstruction" (which as a
    period noun never enters mountain speech; characters say *"since sixty-eight"* or *"in the war"*).
  - **Honest demographic baseline, zero fictionalized real persons.** Mitchell County's 1862 tax list recorded
    only **65 enslaved people** countywide `LEAD`, so the side hollow's twelve distilling households are white
    yeoman farmers as outlined — while three miles down at **Cranberry Forge**, real freedpeople held Mitchell
    County deeds (Peter and Charity Hardin are logged in `docs/period-audit.md` as verification only; per house
    rule, real persons are never voiced or fictionalized).

---

### R-17 · What the trade is called: **`blockader` and `blockade whiskey` on the mountain; `moonshiner` and `moonshine` in outside print only**

`AUTHOR` (2026-10-26), answering **Q-14** ("Blockader"). **Closes the §9 blocking queue (Q-1 … Q-14).**

- **The ruling.** In North Carolina mountain and county-town speech, the noun for an untaxed distiller is
  **`blockader`**, the verb is **`blockading`**, and the untaxed liquor (when distinguished from stamped store
  spirits) is **`blockade whiskey`** or simply **`blockade`**. **"Moonshiner" and "moonshine" are barred from
  narration and from every mountain mouth** — they belong exclusively to **outsiders' print** (northern and
  Piedmont newspapers, *E2*'s county history, or *E3*'s dime novel), on the exact same principle as **R-14**
  ("the Whistlers").
- **Why *blockader* is both period-true and structurally loaded (`LEAD` + R-16).** In western North Carolina and
  east Tennessee, *blockader* / *blockade whiskey* came straight out of the **1861–65 blockade** (`LEAD`: Horace
  Kephart, *Our Southern Highlanders*, ch. VI; Dan Pierce, *Corn from a Jar* / *Our State*; the Dec. 1879
  Montgomery Co., TN raid account): running untaxed jugs past Confederate grain-distilling cordons and then past
  federal revenue lines took the wartime name of running a port blockade, whereas *moonshiner* arrived in the
  mountains from national press dispatches during Raum's late-1870s raids. Under **R-16**, that etymology carries
  the brothers' war split inside one word without a syllable of explanation: Joshua wore the coat of the
  government that enforced the blockade; Jacob stayed in the laurel running past guard posts and kept the word.
  **Never explain the word's origin on the page.**
- **Four-way register split, enforced across the manuscript:**
  1. **Inside the family and the mill (Brennan to Brennan):** plain verbs and work-nouns first — *making*, *a
     run*, *running*, *the whiskey*, *the copper*, *the still*. A man standing at his own tub does not call
     himself a title; he names the chore.
  2. **Across the counter or the road (mountain/store/courthouse-town speech — Tyler, Harper, county men, local
     deputies):** **`blockader`**, **`blockading`**, **`blockade whiskey`**. When someone in Bakersville or at
     Tyler's junction store names the trade as a class of men or distinguishes untaxed jugs from stamped barrel
     goods, *blockader* is the word.
  3. **In the Bureau's mouth and paper (Parrish, the U.S. Attorney, *E1*):** statutory and administrative terms
     only — *illicit distiller*, *unregistered still*, *distilling without bond*, *untaxed spirits*. Parrish
     does not say *moonshiner* either; he speaks the Revised Statutes.
  4. **In outside print (*E2*, *E3*, Charlotte/northern newspapers):** **`moonshiner`** and **`moonshine`** —
     the press's picturesque word, paired with **"the Whistlers"** (R-14) to turn mountain debtors into outlaw
     copy.
- **Linter enforcement (`tools/check.py` via `vocabulary-tone-bible.md` §7):** `\bmoonshiners?\b` and
  `\bmoonshine\b` stay `FLAG` (not `BAN` solely so *E2*/*E3* or a quoted newspaper line can compile after eye
  check; **zero hits allowed in narration or dialogue**), and `\bblockad(?:ers?|ing|e whiskey)\b` gains a `NOTE`
  row so every use is checked against the four-way register rule above.

---

### R-18 · *The Missing Page* (Ch. 15): Parrish puts the *Stowell* "connected premises" trap to Joshua over Tyler's day-book exhibit, and Joshua spots Matthew's omitted folio

`AUTHOR` (2026-10-26), locking Scene Proposal 1 of 3 (`canon §12`, Ch. 15 *The Missing Page*).

- **The scene's legal engine (`R-3` + `R-6` + `R-7` + `R-13`).** By Chapter 15 (after *The Burning* in Ch. 14),
  Jacob has already been convicted at the April 1879 Statesville term and sent away for his statutory two years
  (R-13). What remains open on the docket is the **civil *in rem* libel against the real estate**. Having just
  watched Harper's storage barn burn, Parrish stops chasing copper in the laurel and amends his case toward
  **Joshua's adjoining mortgaged farm (`Parcel A`)** as *"all that lot or tract of land … and premises
  connected therewith"* (Act of 20 July 1868, 15 Stat. 125; *Stowell*, "knowingly has suffered or permitted"):
  the gristmill that ground the meal, the water race, and the cart road running down onto Margaret's forty
  acres (`Parcel B`). Parrish summons Joshua and puts the knowledge question directly to the owner in fee of
  `Parcel A`.
- **Why the chapter is called *The Missing Page* (`R-9` + `R-10` + `R-11`).** Hoss Tyler's bound day book is
  honest and unaltered (R-11: Tyler wrote `"by order of the agent"` in his own hand the day Parrish settled
  Matthew's store debt in *The Store Debt*). What sits open on Parrish's desk during Joshua's examination is
  the clerk's **certified exhibit schedule** copied out of Tyler's seized ledger to prove toll-corn, meal, and
  jug haulage across Joshua's mill and road. Joshua — who has checked mill-toll balances against Tyler's folio
  numbers for fifteen years — sees two things at once while measuring every word so he gives Parrish neither an
  admission nor a perjury trap:
  1. Parrish is building a paper bridge across the property line from Margaret's barn (`Parcel B`) to Joshua's
     mortgaged mill (`Parcel A`);
  2. **One folio number is skipped in Parrish's copied exhibit schedule** — the exact page carrying Matthew's
     settled store account (`"by order of the agent"`) has been withheld from the public forfeiture transcript
     so Parrish's pre-allowance settlement with an informant never enters the court file (and never reaches
     Washington's eyes before R-9's audit).
- **Silence rule:** Neither Joshua nor Parrish says Matthew's name in the room. Joshua reads the gap in the
  folio sequence the way a miller reads a short weight, and walks out knowing both what his nephew cost and
  what the agent is hiding from his own Department.

---

### R-19 · *The Deposition* (Ch. 23) & *The Burning* (Ch. 14): Parrish's hired possemen lit Harper's barn without orders, and Margaret trades her double-edged fire affidavit for `Elisha Councill`'s name in *E1*

`AUTHOR` (2026-10-26), locking Scene Proposal 2 of 3 (`canon §12`, Ch. 23 *The Deposition* and harmonizing Ch. 14 *The Burning*).

- **Harmonizing *The Burning* (Ch. 14) with R-9, R-11, and the outline.** Caleb's network stores untaxed whiskey
  under William Harper's barn floor over Harper's Act One *"don't"* (R-11). When Parrish raids Harper's storage
  barn in Act Two with hired local possemen, his men stave in the barrels and **set fire to the barn without
  Parrish's order** (outline line 234; R-9). Harper loses the landmark barn he raised because the cove refused
  his warning, Parrish inherits a Washington inquiry over why property under federal seizure claim burned on his
  raid, and Caleb crosses into lethal retaliation in *First Blood* (Ch. 16). *(Replaces the stray summary phrase
  "burned by the cove" that had entered §12 Ch. 14.)*
- **Margaret's trade in *The Deposition* (Ch. 23, Margaret POV).** Between Jacob's release (21 April 1881) and
  the October 1881 Statesville term, Parrish must answer the Bureau's audit (R-9) with an affidavit Washington
  cannot dismiss as a deputy covering a superior. Sitting across from Margaret with a clerk, the man libeling
  her forty acres has to ask her to save his appointment. Before signing a word, Margaret exacts one price:
  Parrish must strike **`"a boy"`** from his compelled report to the Commissioner and enter **`Elisha
  Councill`** (R-10, producing *E1*'s exact spelling in R-12).
- **The double-edged truth.** Margaret then swears one strictly true sentence: **Parrish stood in the road
  calling his hired men back and did not order the fire, which caught in the split kegs of blockade whiskey
  stored on Harper's floor.** That single sentence exonerates Parrish from willful destruction with Washington
  (`"closed without adverse finding"`, R-9) and simultaneously puts sworn proof of stored untaxed spirits on
  Harper's connected premises into the federal record against the cove. Neither of them calls it a favor.

---

### R-20 · *Did She Know?* (Ch. 26): Margaret's unburned Watauga deed and the absence of any certified privy examination stall `Parcel B` into `"the tract remains in contest"` (*E1*)

`AUTHOR` (2026-10-26), locking Scene Proposal 3 of 3 (`canon §12`, Ch. 26 *Did She Know?*). **Closes all three
contingent scene proposals in `canon §12`.**

- **The legal collision at the October 1881 Statesville term (`R-7` + `R-12` + `R-13` + `R-15` + `R-18`).** In
  the rented Statesville courtroom (Judge Robert Paine Dick named on the docket, never voiced per R-13), the
  U.S. Attorney presses the civil *in rem* libel against **Margaret's forty-acre separate estate (`Parcel B`)**
  under *Dobbins* and *Stowell* ("knowingly has suffered or permitted"), while arguing **Joshua's adjoining
  mortgaged mill tract (`Parcel A`)** in as *"premises connected therewith"* (R-18).
- **The burned-courthouse deed and the missing privy examination (`LEAD`: NC statutes & Supreme Court).** Under
  **N.C. Laws 1848–49, ch. 41** (quoted in *Perry v. Stancil*, 237 N.C. 442), a husband could not lease his
  wife's real estate even for a term of years *"except by and with the consent of his wife ... ascertained and
  effectuated by privy examination"*; and under **N.C. Const. 1868, Art. X §6**, ***Towles v. Fisher*, 77 N.C.
  443 (1877)**, and ***Scott v. Battle*, 85 N.C. 184 (1881)**, a married woman could not divest or charge her
  separate real estate — **even by estoppel or implied consent** — without written spousal assent and a
  clerk's/justice's **privy examination** taken separately and apart from her husband and duly certified.
  Margaret lays down her folded pre-1861 Watauga root deed (the sole copy in the world after the **23 March
  1873 Boone courthouse fire**, R-15) and stands on the total absence of any certified privy examination in
  Bakersville giving Jacob or any man a lease, license, or estate in her barn.
- **Her single spoken sentence — and why `Parcel B` *"remains in contest"* while Joshua still sells (`R-8` +
  `R-12`).** When the U.S. Attorney asks the *Stowell* knowledge question directly (*forty paces from your
  kitchen door*), Margaret could clear `Parcel B` outright by testifying that Joshua and Caleb ran the cart road
  and used the barn without her leave — damning the boy she raised (R-8) and sealing `Parcel A`. She refuses.
  She answers in **one narrow sentence** — that her husband owned no inch of her father's ground and she never
  went before any clerk to give any man leave upon it — and names nobody. That answer forces a federal-supremacy
  vs. NC-coverture question of law (`whether federal in rem forfeiture can divest a NC feme covert's separate
  realty by implied consent without privy examination`) onto exceptions, holding `Parcel B` over past the term
  and producing Parrish's exact 1882 line in *E1*: **`"the tract remains in contest"`** (R-12) — while private
  mortgage pressure and defense costs leave Joshua no room left on `Parcel A`, forcing Ch. 27 (*The Mill Sold*).

---

## 12. Chapter map v1 — POV-tagged and dated (R-4, R-5, R-13)

Twenty outline beats in, **28 chapters** out, numbered continuously across the book. Renumbered
2026-10-26 when R-13 fixed the two term dates and moved *The Return* ahead of the surrender: Jacob is out
of prison six months before his nephew walks into court, and the book is better with him home for it.
"J" = Joshua, "M" = Margaret. **Cross-references in this file are by title from now on, not by number, so
this table can be reordered without breaking them.**

**ACT ONE: THE THRESHOLD** · summer 1878 – February 1879

| # | Chapter | POV | Beat | What changes practically |
|---|---|---|---|---|
| 1 | The Water Is Right | J | The World Before | The cove's economy in weights and a jug carried to Tyler's. The still seen working, from outside. R-4: we open on the corn, not on Jacob's hands. |
| 2 | Powder on the Ridge | J | (new, R-2) | Grading/prospect powder heard at night; Pardee's narrow-gauge/ore transit & 100-ft steel chain on the State Line Gap divide above Elk Park clearing. The second chain-and-book front planted before the first one is (`docs/act-1-beat-sheet.md`). |
| 3 | The Office | J | The Arrival of the Excise | Parrish opens; calls on the judge, the sheriff, the leading men. Joshua and **Harper both attend** (R-11). |
| 4 | What a No Costs | J | The Recruitment of Joshua | Parrish asks for names; Joshua refuses; the last page is his own mortgage and the cart road down onto his brother's wife's ground (R-6/R-7). In the same drawer: the keeping-money ledger line (R-8) and his 1865 Knoxville Union discharge paper (R-16), neither explained. |
| 5 | Keep Making It | J | Jacob Understands + the cove's choice | The cove decides to continue and to not-know, at Joshua's mill. **Harper says *don't*** and is outvoted (R-11). |
| 6 | Gauger's Work | J | The Standoff Begins | A still in a barn makes the *land* the case (R-3). **Tyler's day book is taken**; the written protest is what will make it evidence (R-11). |
| 7 | The Store Debt | J | The Temptation | **R-10's three asks in one chapter:** the day-book line, the date, the appointment not given. |
| 8 | The Cold Still | M | End of Act One | The raid runs on Matthew's day; the still is cold; **Lish Councill is shot behind Harper's barn**; then the notice, naming the property and her interest (R-10/R-7). Ends unanswered. |

**ACT TWO: THE WEIGHT OF IT** · March 1879 – December 1880

| # | Chapter | POV | Beat | What changes practically |
|---|---|---|---|---|
| 9 | The Term, 1879 | J | (new, R-13) | **Statesville, term opened Monday 21 April 1879.** Jacob convicted; the statutory two years; the still sold for less than the iron was worth. A rented room — the United States had no courthouse in Asheville until 1892. Joshua watches the arithmetic be done in a language he half reads. |
| 10 | The Empty Year | J | The Empty Year | Harvest without a distiller; the term list as the cove's almanac. "A year and more," never "about a year" (R-13). |
| 11 | Margaret's Book | M | (new, R-3/R-7) | She reads the posted notices because the libel is against *her* tract. Her father's deed in the same box as her accounts. |
| 12 | The Name | J | The Name | The cove learns who informed; Joshua is told; he does not say it. |
| 13 | Johnson City | J | The Fall's aftermath | Matthew's injuries as objects and a doctor's sentence. The beating was Caleb's work too; Joshua looks at both boys and prices neither (R-8/R-10). |
| 14 | The Burning | J | The Burning | **Harper's** barn — where Caleb's network stored blockade whiskey over the objection of the man who said *don't* (R-11) — raided by Parrish's hired possemen, who stave in the kegs and set the barn afire without Parrish's order, burning property under federal seizure claim (R-9/R-19). |
| 15 | The Missing Page | J | The Network Spreads | **RULED (R-18):** With Jacob in prison from the April 1879 term, Parrish turns the civil *in rem* libel onto Joshua's mortgaged farm (`Parcel A`: mill, water race, cart road) as *"premises connected therewith"* and examines Joshua over a certified exhibit transcript of Tyler's seized day book — where Joshua spots the skipped folio number omitting Matthew's settled store account (`"by order of the agent"`, R-10/R-11). |
| 16 | First Blood | J | The First Blood | The deputy is killed. The cove's war becomes the crime the Bureau was built to answer. |
| 17 | The Letters | J | Jacob's Letters + end of Act Two | Prison correspondence in two hands; the months counted in the ledger, not in thought. |

**ACT THREE: THE RECKONING** · January 1881 – November 1881

| # | Chapter | POV | Beat | What changes practically |
|---|---|---|---|---|
| 18 | "We End It." | J | The Plan / Caleb's line | Caleb organizes; Joshua watches and does not stop him. |
| 19 | The Warning | J | The Network Spreads | The nod as policy — and no banner, no oath, no minutes: the only minutes that exist are the agent's (R-14). Joshua is complicit in something he can price. |
| 20 | The Return | J | Jacob's Release and Return | **Released 21 April 1881** on the two years counted from the April 1879 term. He comes home to a house that has become the site of a second case, and to a wife who has been running it. The law is not cruel; it is complete. |
| 21 | The Ambush | J | The Ambush (partial) | *Best small scene available anywhere in the act:* a clerk writes "Whistlers" into a deposition and nobody in the room corrects him (R-14). | Parrish is hit; the horse goes down; the deputies return fire. Long sentence for the mountain, then four-word declaratives. The wound and the side are pinned. His reward is a letter, two chapters later. |
| 22 | The Search | M | The Manhunt | The house on her freehold is searched; she asserts a standing the searchers must answer to. Offstage: the Department's first letter, seen as an envelope. |
| 23 | The Deposition | M | (new, R-9 / **RULED R-19**) | **Parrish must ask Margaret to save him.** Before signing, she requires him to strike `"a boy"` and enter **`Elisha Councill`** in his Commissioner's report (*E1*); then she swears one true sentence — Parrish stood in the road calling his hired men off when the fire caught in the split kegs stored on Harper's floor — saving Parrish with Washington and putting sworn proof of stored spirits into the federal record against the cove. |
| 24 | The Surrender | J | The Capture | Joshua says the name he has kept unspoken, out loud, as a piece of information. Caleb gives himself to the court, not to the agent. |
| 25 | The Term, 1881 | J | (new, R-13) | **Statesville, term opened Monday 17 October 1881.** The circuit, the hotel rooms, the marshal's fees, and the fact that a trial in this district is a schedule before it is a judgment. |
| 26 | Did She Know? | M | The Broader Tragedy / the trial | **RULED (R-20):** In Statesville (Judge Dick named, never voiced), Margaret lays down her folded pre-1861 Watauga deed (sole copy after the 1873 Boone fire, R-15) and stands on `Art. X §6`, N.C. Laws 1848–49 ch. 41, and *Scott v. Battle*, 85 N.C. 184 (1881) — no certified privy examination exists giving Jacob or any man an interest in her barn. In her one spoken sentence on knowledge she refuses to clear `Parcel B` by naming Caleb or Joshua, stalling the decree into *E1*'s `"the tract remains in contest"` (R-12) while mortgage and defense costs force Joshua to sell `Parcel A` in Ch. 27. |
| 27 | The Mill Sold | J | Joshua's End | He sells and leaves; a father leaving the son he raised as his brother's, and neither of them says so (R-8). The only Brennan who dies where the streets have names. |
| 28 | The Far Side of the Ridge | J | (new, R-5) | November 1881. A blast from the wrong side of a ridge, and he does not go and look. No engine, no rails, no lesson. |

**THE EPILOGUE (R-12)** — documents only, no voice: *E1* the agent's 1882 report to the Commissioner ·
*E2* a county history with the year wrong by two · *E3* a dime-novel title page, **whose title is where the name
"the Whistlers" finally becomes true** (R-14: the invented label outlives the men it was written about). The fiction's present tense
never crosses 1881, and the title page dates the war **1878–1881**.

**Accounting (28 chapters):** Joshua 23 whole chapters; Margaret 5 (*The Cold Still*, *Margaret's Book*,
*The Search*, *The Deposition*, *Did She Know?*) = 18% by count, which lands on the ruled ~20% of **words**
because her chapters carry the paperwork and run long. Measured at Pass 4, never by count. If it reads
85/15 in words, the fix is to lengthen *The Deposition*, not to take a chapter from Joshua.

**Word math for the pitch:** 28 chapters × 3,200–3,500 = 89,600–98,000 words — inside the 85,000–100,000
target with no filler owed.

**Scene-level status (ALL THREE SCENE PROPOSALS RULED):** *The Missing Page* (**R-18**), *The Deposition*
(**R-19**), and *Did She Know?* (**R-20**) are all **RULED**, alongside *The Term, 1879* and *The Term,
1881* (**R-13**). **All 28 chapters in Acts One, Two, and Three plus *E1–E3* now have locked structural beats.**


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
| **21 Apr 1879** | WDNC term **opens at Statesville** (3rd Monday in April) → R-13 | **Jacob convicted, two years:** U.S. v. Brennan. His release date is fixed now — 21 Apr 1881. |
| Late 1879 / early 1880 | — | Harper's barn burned |
| Sept 1880 | ET&WNC construction under way in earnest `LEAD`, dates contested | Blasting heard from the cove; men leave for the grade |
| Early 1880 | — | The deputy ambushed on the road ("First Blood") |
| Mid 1880 | — | Joshua tells Caleb the informant's name |
| Late 1880 | — | The ride to Johnson City; Matthew beaten, exiled; Act Two closes on the ridge |
| 1880–81 | Garfield assassinated 2 Jul 1881; Arthur succeeds `LEAD` | Act Three: the ambush on Parrish (summer 1881), the manhunt, the deposition |
| Aug 25 1881 | Redmond tried in Charlotte (8 liquor counts, 2 conspiracy counts; 10 yrs Auburn; $2,600) `LEAD` | The template for Caleb's case — see §6 |
| 22 Aug 1881 | Track to Hampton, TN complete `LEAD` | The steel is now a day's walk away |
| **17 Oct 1881** | WDNC autumn term opens at Statesville (R-13) | **Caleb tried** on the liquor counts, as Redmond was tried in August; convicted, two years, fine |
| **Nov 1881** | — | The mill sold; Joshua leaves; a blast from the far side of the ridge. **End of the fiction's present tense (R-5).** |
| **21 Apr 1881** | Two years, counted to the day (R-13) | **Jacob released.** He comes home mid-ambush, to a cove that kept on without him and a wife who has run the place |
| Mid-June 1882 | ET&WNC reaches Elk Park `LEAD` | **Outside the fiction's present tense. Under R-5 the train never appears; this date may only be reached by a printed document (Q-9), or spoken of as a rumor of spring.** |
| 3 Jul 1882 | Line opens to Cranberry; iron moves; company town begins | The world the tax could not reach is reached anyway |
| 1895 | — | `INVENT` Jacob dies, never having distilled again |

---

## 3. Geography & jurisdiction

- **Country (RULED → R-15).** High coves of the Blue Ridge, northwestern NC, right under the Tennessee line,
  between **Cranberry Forge** and **Elk Park** in the Elk River / Cranberry Creek drainage (~3,200–3,500 ft).
  `AUTHOR` / `USER`
- **County in 1878–1881: MITCHELL (`Cranberry Township`), seat BAKERSVILLE.** **RULED Q-12 → R-15.**
  Mitchell County was formed **16 Feb 1861** from Yancey, Watauga, Caldwell, Burke, and McDowell; its seat is
  **Bakersville** (est. 1868; *not* Burnsville, which is Yancey). **Avery County does not exist until 23 Feb
  1911** (`BAN`). **Burke County** is where the valley's root grants were entered before 1833 (seat Morganton;
  courthouse records burned April **1865**), and **Watauga County** held Cranberry Forge from 1849 to 1861
  (seat Boone; courthouse burned **23 March 1873**), while Banner's Elk (5.4 air miles east over the ridge)
  remained in Watauga `LEAD`. That succession puts three courthouses — two of them burned — in Margaret's
  deed box (R-7, R-15).
- **Real & fictional place names.** `INVENT` The cove is **Elk Cove**; the side hollow above it is **North Fork
  Hollow**; the junction store on the Yellow Mountain Turnpike above the Forge is **Hoss Tyler's**. Real border
  points: **Cranberry Forge** (official post-office name until 24 Apr 1884; speech says "Cranberry" or "the
  Forge"; no company hotel or scrip until after July 1882), **Elk Park** (unincorporated border clearing one
  mile north of the Forge at State Line Gap; no post office until May 1883, no town charter until 1885), and
  **Bakersville** (county courthouse, sheriff, register of deeds, and Parrish's county office days). **Newland**
  is `BAN` (named 1911–12; in 1878 say **Old Fields of Toe**).
- **The three parcels (R-6 + R-7; this is the book's map and it does not change).**
  1. **Margaret's tract** — hers in fee as a separate estate, inherited from her father: the cabin, the
     garden, the barn the still stands in. The forfeiture's first target; the only ground in the hollow
     beyond Jacob's creditors.
  2. **Joshua's farm** — the elder brother's inheritance, mortgaged to the merchant: the mill, the corn,
     the wagon road, the barn where the cove meets. His land is what the government tries to reach by
     arguing *connection*, and what the lien-consent rule made unregistrable.
  3. **Harper's ground** — old, at the junction, where whiskey is stored before shipment. Burned in Act
     Two by the raid party, not by the statute.
  Between them: a water race from Joshua's hill down onto Margaret's flat, and one cart road that serves
  both. That road is the whole legal argument (R-7).
- **Distances (RULED → R-15; fixed and never varied).**
  - Still to Margaret's cabin: **same place, forty paces** (R-7).
  - Cove to **Hoss Tyler's** junction store: **two miles** (`INVENT`).
  - Tyler's store to **Cranberry Forge** (post office, ore pits): **three miles**; **Elk Park** border
    clearing: **one mile north of the Forge** (`LEAD`).
  - Cove across the eastern ridge to the **Watauga County** line (toward Banner's Elk): **five to six miles**
    (`LEAD`).
  - Cove to **Bakersville** (Mitchell County seat / sheriff / register / Parrish's local office): **~22 road
    miles (14.1 air) down the North Toe — one full day on horseback** (`LEAD`).
  - Cove to the **ET&WNC railhead at Hampton, TN** (22 Aug 1881): **15.5 air / ~19.9 rail miles** through
    **Doe River Gorge**; active 1880–81 black-powder grading on Roan Mountain / Shell Creek / State Line Gap:
    **4–7 miles across the state-line ridge, audible at night** (`LEAD`, R-2/R-5).
  - Cove to **Elizabethton / Johnson City, TN**: **~20 / ~34 miles — a day to a day and a half** (`LEAD`).
  - Cove to **Morganton** (Burke County seat, eastern wagon market): **~45 wagon miles — two days by wagon**
    (`LEAD`).
  - Cove to **Statesville** (Iredell County, WDNC federal court): **~90 road miles (65.4 air) across three
    county lines — three days each way on horseback** (`LEAD`, R-13).
- **Travel reality.** No railroad in the cove in 1878–1881. Wagon over the mountains to Morganton or
  Elizabethton `USER`. The Yellow Mountain Turnpike is the route through the area `USER`.

---

## 4. Cast

Ages are **as of the year the outline first sets them**, and are fixed by **R-6** (2026-10-26): the
outline's contradiction — Joshua 45 but "older brother" of a Jacob aged "45–50" — resolved in favor of the
birth order. **Joshua is the elder: b. ~1828, 50 in 1878. Jacob b. ~1833, 45 in 1878.**

**JACOB BRENNAN** — b. ~1833, so **45** in 1878 (R-6). Younger brother. Distiller on his elder brother's
ground, which is the whole of his legal exposure and none of his self-image. Not a criminal in his own eyes
and not a political animal. Competence shown only through the still: water, drainage, the placing of a
garden. Engine consequence: the apparatus and his body are the libel's subject matter, but **the land is his
wife's** (R-7) — the forfeiture falls on the one parcel that was always meant to be beyond him, which is
why his calm in Act One reads, in hindsight, as a man protected by a marriage he never thanks.
**RULED Q-13 → R-16 (`INVENT` grounded in `LEAD`):** stayed on the mountain in **1862–65** — cutting and
hauling around Cranberry Forge to stay off the early conscript lists and lying out in the laurel when the Home
Guard swept the creek — keeping the place and five-year-old Caleb while Joshua served in the Union army, which
is how the boy came to call him "Father" (R-8). `INVENT` the year of his father's death (see inheritance ask
R-14).

**MARGARET BRENNAN (née ___)** — 40s in 1878. Wife, mother of the informer, and **owner in fee of the
tract the still stands on** (R-7): her father's land, her separate estate under NC Const. 1868 Art. X §6,
not liable for her husband's debts. **RULED Q-4 → R-7; Ch. 26 RULED → R-20.** She is the only character who
can convey, and the only one whose knowledge is a legal question with an answer worth money — which makes her
the person the trial is about. `INVENT` her father's name and the postwar Mitchell deed date (suggest 1866–68,
resting on her father's folded pre-1861 Watauga root deed — the sole copy left after the 23 March 1873 Boone
courthouse fire, R-15). **RULED → R-20:** in *Did She Know?* (Ch. 26), she lays down that unburned deed and
stands on the total absence of any certified privy examination giving Jacob or any man an interest in her barn
(N.C. Laws 1848–49 ch. 41; *Scott v. Battle*, 85 N.C. 184 [1881]), stalling `Parcel B` into *E1*'s `"the
tract remains in contest"` (R-12).

**MATTHEW BRENNAN** — 19 in 1878 (b. ~1859), Jacob's son, raised as Caleb's brother (R-8). Informs; is
exiled; is beaten to broken ribs and a broken arm in Johnson City; never returns. **RULED Q-7 → R-10: three
asks — the store debt (paid to Tyler, not to him), the day of the raid (a boy dies anyway), a written
appointment (refused, courteously).** He is "paid" months late by a Treasury order that goes back uncashed,
marked *person unknown*. No interiority, ever: his motive is three objects, not a thought.

**CALEB BRENNAN** — 21 in 1878 (b. ~1857). **RULED Q-5 → R-8: Joshua's firstborn, raised as Jacob's
son**, which keeps every outline label literally true — a Brennan, a nephew, "Father." Heir to his father's
mortgaged farm and to Margaret's freehold, and to neither. Arc: hothead → organizer of the warning system →
the man who decides that the burning of Harper's barn is a line crossed → the beating at Johnson City (his
brother's work, and his) → ambush → fugitive → conviction → the mountain's own celebrity, which arrives
through print (see the Redmond template, §5). Never told, never told twice: see §10's Caleb audit.

**JOSHUA BRENNAN** — b. ~1828, so **50** in 1878 (R-6). Elder brother, heir to the farm, and the mortgagor
of it: the fee the government can reach is his (R-3 + R-6). Miller and trader. Refuses to inform in
Act One, refuses Caleb's intelligence request in Act Two, tells Caleb the informant's name anyway,
shelters the fugitive, sells out and leaves. **The only man standing in both worlds and the only
character who knows the informant's name and must decide whether to say it.** **Spine POV, ~80% — ruled
Q-1 → R-4.** Under **R-8**, the father of the boy in his brother's house — the one fact about Joshua the book
must make legible without ever once stating it. And under **R-16**, a **Union veteran (1862–65)** who walked
over State Line Gap the summer Elsie died and mustered out at Knoxville (unit unnamed on the page): the United
States taking his deed is the army he fought for, enforcing the July 1, 1862 war tax enacted the month he put
on the coat — carried solely by his 1865 discharge paper in the drawer, never spoken.

**WILLIAM PARRISH** — 35–40 in 1878. Federal revenue agent. Rifle, badge, orders, and — from Act Three on,
a file with his own name in it. Courteous and reasonable within his institution (Style Guide §1.3) —
**which the outline honors in Act One and abandons afterward; R-9 restores it by making the Department
distrust him.** Post-Whiskey-Ring Treasury wants clean convictions, not moieties, so he cannot buy anyone
and cannot be bought either. **His cost is ruled (Q-6 → R-9): the audit.** Never inside a head, so his cost
is carried entirely in correspondence and in handwriting that does not change.

**OLD HOSS TYLER** — **63 in 1878** (b. ~1815), storekeeper at the junction. **RULED Q-8 → R-11: promoted,
and neither bought nor a traitor — a creditor.** His day book is Act One's most important object and Act
Three's exhibit, and he authenticates it by protesting its seizure. He is the only man in the hollow paid in
coin by the agent's order, on the same boy's account, twice. Runs the closed circuit the book breaks: where a
jug becomes flour, salt, tobacco, cloth — and where a price, and so a tax, first becomes real. He does not
betray the cove. He keeps a book.

**WILLIAM HARPER** — **60 in 1879** (b. ~1819), four sons, no still, one barn with a good floor at the
junction road. **RULED Q-8 → R-11: he attends the Act One meeting and says *don't*, and is outvoted** — so
the Act Two burning is done to the one neighbor who was right, and Lish Councill is killed on his ground. His
knowledge is the forfeiture's easier case (*Stowell*: suffered and permitted; *Dobbins*: knowledge not
required), and the cove cannot answer a man who was right except with fire. He gets no speech. He gets a
doorway and his sons standing in it.

**THE COVE.** `INVENT` ~12 distilling families; **Lish (Elisha) Councill, 15**, of North Fork, killed in the
Act One raid (R-10); white yeoman households in the side hollow itself (Mitchell County's 1862 tax list counted
65 enslaved persons countywide, while real freedpeople landowners held deeds three miles down at Cranberry
Forge — **RULED Q-13 → R-16**, §7); Baptist and Methodist meeting houses `USER`; extended-family
naming: use attested **Cranberry Township (Mitchell) and Watauga-ridge surnames** (Winters, Buchanan, Wiseman,
Pritchard, Burleson, Gouge, Dugger, Banner, Avery, Henson, Calloway, Brown, Councill) for the secondary cast so
the 1880 census reads true `USER`/`LEAD` (R-15).

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

**5.7 Enforcement machinery.** Commissioner of Internal Revenue (Raum, from Aug 1876); supervisors of
internal revenue (**abolished 15 Aug 1876, 19 Stat. 152**, transferring `Rev. Stat. § 3163` book-examination
and summons powers directly to **internal revenue agents** employed by the Commissioner under **`Rev. Stat.
§ 3152`** `VERIFIED`); Sixth Collection District of NC collector at Statesville (**Dr. John James Mott**,
1872–82; appoints deputy collectors under `§ 3148`, never voiced); gaugers; deputy marshals, hired by the
marshal and paid fees/mileage — the reason a posse looks like mercenaries `LEAD`. Removal of state prosecutions
to federal court, and *Tennessee v. Davis* (1879), a revenue killing pulled into federal court `LEAD`. Whether
troops could be called: see "The Army and Moonshiners in the Mountainous South" (Leavenworth thesis,
ADA284658) `LEAD`.

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

## 7. What the outline deleted — **RULED Q-13 → R-16 (bone structure in objects, zero speeches)**

The source outline had no war allegiance, no 1868 paper trail, and no Reconstruction memory in 1878 North
Carolina. **R-16** resolves this without adding a single political speech: (i) **Joshua's 1862–65 Union
service** (over State Line Gap into East Tennessee after Elsie's death, mustered out at Knoxville in 1865; unit
unnamed on the page) means the United States coming for his mortgaged farm is his own army enforcing the July 1,
1862 war liquor tax, while **Jacob stayed on the mountain in 1862–65** dodging Home Guard sweeps and raising
Caleb (locking R-8); (ii) **1868 lives in the room as paper** — the same 1868 NC Constitution whose township
tax rolls (`Cranberry Township`) and delinquent-land tax sales made clerks' notices feared in the hollows is
the exact clause (`Art. X §6`) that shields Margaret's separate estate (R-7). **Strictly excluded:** Klan
subplots (historically Rutherford/McDowell, not Cranberry Twp), party stump speeches, and the noun
"Reconstruction" in mountain mouths.

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
5. **Say `blockader` on the mountain, `moonshiner` in outside print only (RULED Q-14 → R-17).** Around their
   own mill and still the Brennans use work-verbs (*making*, *running*, *a run*, *the whiskey*); when a
   mountaineer, storekeeper, or county man names the trade or the untaxed liquor as a class, the word is
   **`blockader` / `blockading` / `blockade whiskey`** (`LEAD`: Kephart; Dan Pierce). Parrish speaks the statute
   (*illicit distiller*, *untaxed spirits*). **"Moonshiner" and "moonshine" appear only in outside print**
   (newspapers, *E2*, *E3*), never in narration or dialogue.
6. **"Revenuer" is the derogatory.** Parrish objects to it once, out loud, and is corrected by a
   subordinate, not by a mountaineer.
7. **Numbers are spoken, not argued.** No character explains the tax rate. Somebody counts dollars.
8. **First-Touch Physical Scale Rule (`AUTHOR`, 2026-10-27 — `in_scene_physical_scale`).** No glossary, front-matter chart, or authorial conversion note. Every period weight, measure, land/survey unit, proof term, and dollar sum must be anchored on its **first appearance** in plain physical scale: **body lift/weight** (`a 56-lb bushel; a two-man 112-lb two-bushel bag`), **household duration** (`a 7-lb half-peck poke = 3 days' cornbread for four people`), **visual physics** (`100 proof = half pure spirit, half water; 3-ft narrow gauge = rails one stride apart; Gunter's 66-ft chain = the breadth of a barn lot`), or **days of human sweat** (`75–90¢ for a 10-hour day swinging an axe, making $6 over a full week's labor and $24 a solid month's cash wages`).

---

## 9. Open questions — one at a time, in this order (**ALL 14 RULED**)

Kevin rules each in chat. Each ruling moves from here to §1 as `AUTHOR` and out of the blocking list.

| # | Question | Blocks |
|---|---|---|
| Q-1 | **Whose spine?** | ✅ RULED 2026-10-26 → **R-4**: Joshua ~80%, Margaret ~20%. Chapter map is §12 |
| Q-2 | Does Act Three extend to June 1882 so the first train is a final **image**, or does it arrive as **coda**? | ✅ RULED 2026-10-26 → **R-5**: neither — ends autumn 1881, train heard about, never seen. Subtitle date 1878–1881 |
| Q-3 | Ages: is Jacob older than Joshua (b. 1831/1829) or is "older brother" wrong? | ✅ RULED 2026-10-26 → **R-6**: Joshua is the elder (50), Jacob 45; the forfeitable fee is Joshua's; Margaret's standing reopens as Q-4 |
| Q-4 | Does Margaret hold title, or dower, or nothing? Who can sign away the hollow? | ✅ RULED 2026-10-26 → **R-7** (+ **R-20**): her father's tract, in fee, as a married woman's separate estate — and the still sits on it. Dower and the homestead exemption are off the table; in Ch. 26 (*Did She Know?*, R-20), her unburned Watauga deed and the absence of any certified privy examination stall `Parcel B` into *E1*'s `"the tract remains in contest"` |
| Q-5 | Whose son is Caleb, and why does he call Jacob "Father"? | ✅ RULED 2026-10-26 → **R-8**: Joshua's firstborn, given to Jacob's house in 1862 when Joshua enlisted; raised as Matthew's brother; never stated in the book |
| Q-6 | What does Parrish pay for, and what does it cost him? (Post-Ring Treasury; no moiety to promise) | ✅ RULED 2026-10-26 → **R-9**: the Bureau audits him; the unsigned order becomes an exhibit in his own defense; the complaint closes without finding and he keeps the office |
| Q-7 | Matthew's motive, concretely — and does he ever get paid? | ✅ RULED 2026-10-26 → **R-10**: the store, the day, the paper — granted, granted, refused; paid months late by an order returned "person unknown." It also pre-decides half of Q-8 (Tyler's day book is the exhibit) |
| Q-8 | Promote Hoss Tyler and put Harper in the Act One meeting? | ✅ RULED 2026-10-26 → **R-11**: both promoted; Tyler a creditor, not a Judas — his own protest authenticates the day book; Harper says *don't* at the cove meeting and loses his barn for having been right |
| Q-9 | Frame or no frame for the epilogue? | ✅ RULED 2026-10-26 → **R-12**: diegetic print only, three artifacts (report / county history / dime-novel title page), no author's note, no in-book accuracy apology; title-page date stays 1878–1881 |
| Q-10 | Which federal court sits where, on what term date, in 1879? | ✅ RULED 2026-10-26 → **R-13**: the Circuit Court at Statesville, terms the 3rd Monday in April and October — Jacob convicted 21 Apr 1879 (released 21 Apr 1881), Caleb tried 17 Oct 1881; Judge Dick named, seated, never voiced |
| Q-11 | Is "Whistlers" sourced or invented-and-owned? | ✅ RULED 2026-10-26 → **R-14**: owned as invention, and print-only — the Bureau, the county paper and the dime novel say it; the hollow never does |
| Q-12 | Which county is the cove — Watauga, Mitchell, or Caldwell? | ✅ RULED 2026-10-26 → **R-15**: near **Cranberry Forge / Elk Park** = **`Cranberry Township, Mitchell County`** in 1878–81 (seat **Bakersville**; *not* Burke, which lost this ground in 1833, though Burke and Watauga head the older burned-courthouse deeds in the family box) |
| Q-13 | Reconstruction in or out? | ✅ RULED 2026-10-26 → **R-16**: in as bone structure, objects only — Joshua fought for the Union (1862–65, Knoxville discharge; same summer as the 1862 liquor tax), Jacob stayed on the mountain raising Caleb, and the 1868 Constitution is both the feared tax-roll regime and Margaret's separate-estate shield; zero party speeches, no Klan subplot |
| Q-14 | "Blockader" vs. "moonshiner" — who says which word? | ✅ RULED 2026-10-26 → **R-17**: **`blockader` / `blockade whiskey`** in mountain and county speech (around their own still the Brennans use verbs: *making*, *running*, *a run*); *illicit distiller* in Bureau paper; **`moonshiner` / `moonshine` in outside print only** |

---

## 10. Continuity anchors (linter-enforced; `tools/check.py`)

- **Ages (R-6).** Joshua 50 (1878) · Jacob 45 · Margaret 40s · Matthew 19 · Caleb 21 · Parrish 35–40 ·
  Harper 60 (1879). `tools/check.py` compares any parenthetical age in the manuscript against this list.
- **Injury sides.** Matthew: broken ribs — *which side*; broken arm — *which*. Once set, never vary.
- **Seasons elapsed.** Act One summer 1878 → autumn 1878 → winter 1878–79 → spring 1879. Act Two
  "empty year" 1879–80. Act Three 1880–**1881** (R-5: the present tense stops in autumn 1881; 1882 is
  reachable only by report or by a printed epilogue).
- **Jurisdiction, deed trail, and distances — CLOSED (R-15).** In 1878–1881 the hollow sits in **`Cranberry
  Township, Mitchell County`** (seat **Bakersville**, one full day / ~22 road miles down the North Toe), above
  **Cranberry Forge** (3 mi from Tyler's store; PO named *Cranberry Forge* until 24 Apr 1884) and **Elk Park**
  (unincorporated border clearing 1 mi north of the Forge; no PO until May 1883, no town charter until 1885).
  Pre-1861 deeds in the family box carry **Burke** (pre-1833; Morganton records burned Apr 1865) or **Watauga**
  (1849–61; Boone deed books burned 23 Mar 1873); postwar filings (Margaret's 1866–68 separate-estate deed,
  Joshua's mortgage) sit at **Bakersville**. Statesville is ~90 road miles across three county lines (**three
  days each way on horseback**, R-13); Johnson City ~34 miles down the Doe River; Hampton railhead (22 Aug
  1881) **15.5 air / ~19.9 gorge miles** away, whistle blocked by Doe River Gorge, while 1880–81 black-powder
  blasting on Roan Mountain / Shell Creek / State Line Gap is 4–7 miles over the ridge.
- **Sentence arithmetic — CLOSED (R-13).** Convicted at the term that opened **21 April 1879**, two years,
  so released **21 April 1881**. At the end of 1880 he has **four months and ten days** left; in January 1880,
  fifteen. Any line about his time must match the month of its chapter (and see R-13's fix to the outline's
  "about a year").
- **The term calendar is load-bearing (R-13).** Terms opened at Statesville the third Monday in April and
  October. Fixed here: **21 Apr 1879** (Jacob convicted), **17 Oct 1881** (Caleb tried). No verdict, notice,
  deed or filing may be dated on a day the court was not sitting, and nothing in the cove's planning language
  may contradict the term list.
- **The trip is priced.** A sitting costs a mountain man three days each way, a hotel, and feed for the horse.
  Put that arithmetic in a ledger line in any chapter that asks someone to go.
- **Mill tolls and Joshua's mortgage arithmetic (Chs. 1–4).**
  NC statutory public-mill toll is **one-eighth** on bread meal (**7 lb** out of a 56-lb bushel) and
  **one-fourteenth** on coarse chop (**4 lb** out of 56 lb; *Rev. Code* 1854, c. 71, s. 6). Joshua's father
  set the white-oak mill frame in **`1848`**, Joshua hung the upper French millstone **after `1865`**, the
  waterwheel is **twelve feet** in diameter (one rusted iron rim-strap parts in Ch. 1 and is banded with an
  18-lb Cranberry flat-iron bar across Chs. 1, 2, and 4), and the **$400** mortgage to **Hosea "Hoss" Tyler**
  dates from rebuilding the dam after the **`1869`** flood.
  `Parcel A` stands entered in *Deed Book D* at Bakersville at **eighty-six acres** in fee (mill-seat, dam,
  six acres of late corn, cart road, and the **split-chestnut water trough propped on four forked locust
  stakes across the granite corner-stone** — laid by Joshua himself in Ch. 1 during the late-August drought at
  the cost of a `12-bushel / $6.00` cash bread-meal grinding for the Cranberry Forge wagon to save Jacob's
  `16-bushel` ripe mash run when Margaret's spring dropped warm, and left running past dark); Margaret's
  `Parcel B` is **forty acres** conveyed in **`1868`** as her separate estate out of her father's old Watauga
  grant; William Harper's junction farm is **two hundred acres** with a double-crib barn. Jacob's copper kettle in Margaret's lower
  barn (`40 paces` below her kitchen) is **eighty gallons**; Joshua rides a **claybank mare**, Harper rides a
  **heavy brown mare**, Parrish rides a clean-limbed **bay gelding**, Squire Wiseman (Three Mile) rides a
  **roan mare**, and Matthew's half-share mount is the **bay mule**. Joshua's mortgage on `Parcel A` (deed of
  trust held by **Hosea "Hoss" Tyler**, payable in lawful money) stands at **$400 principal** with **$24 annual
  interest (6%, N.C. Laws 1876–77, ch. 91) due 10 November** (Sunday in 1878; paid Saturday 9 Nov / Monday 11
  Nov out of an oilskin pouch holding **36 silver halves [$18], 4 quarters [$1], and one $5 U.S. note**);
  Matthew's open store page (**`Folio 114`**) carries **$12** remaining on the bay mule's half-share plus the
  December 1877 Bakersville doctor's ride and an April chilled plow point (**$19.40** settled in silver in Ch.
  7). In Ch. 2 (first week of Oct 1878), **Tom Burleson** (son of Elihu Burleson of North Fork) pulls a
  **100-ft steel chain** at **90¢/day** in cash silver for **Hendrick** (Mauch Chunk, PA engineer for Pardee's
  Cranberry / 3-ft location party). In Ch. 3 (**Thu 10 Oct 1878**), Harper and Joshua see young deputy clerk
  **McKinney** shelving *Deed Book C* and *Deed Book D* in the **1868 brick courthouse** on **Water Street**
  before Parrish (`38`, `Rev. Stat. § 3152`, citing Commissioner Raum's **20 Aug 1878** leniency cutoff, `Act
  of July 1868 §§ 8, 12, 44`, and `Rev. Stat. § 3163` ledger summons) sets the winter docket for **Monday, 21
  April 1879** at **Statesville** (`Collector Mott`). In Ch. 4 (**Sat 26 Oct 1878**), Joshua refuses Parrish's
  **$20/month** (`$100` Nov–Mar) detective-voucher offer and connected-premises warning (*Dobbins' Distillery*,
  Jan 1878; `Rev. Stat. §§ 3281, 5440`); inside Joshua's locked walnut table drawer beneath the `$24` pouch lie
  last autumn's `10 Nov 1877` Tyler receipt, the stitched **`1866`–`1869`** keeping-money sheet (*To Jacob's
  house*: Dec 4 yds gray jeans `$2.10`, Jan kip shoes `$1.60`, Sept slate/pencil/primer `40¢`, Nov cash keeping
  `$5.00` — **Caleb Clue #1**), and Joshua's thrice-folded **August 1865 Knoxville U.S. Army discharge** (unit
  folded inward).
- **Parrish's wound.** Hit in arm or leg (outline undecided) — pin side and limb; he is on the page
  afterward holding things differently.
- **Two ambushes.** Act Two's deputy and Act Three's Parrish must differ in texture or one goes. The killed
  deputy is **not** named Burns (real 1874 killing, WDNC — cite him, do not reuse him: R-9).
- **Parrish's correspondence (R-9).** Three documents, dated, in the same hand: the Department's letter of
  inquiry (Act Three, arriving offstage in ch. 20), his answer (ch. 22), and the closing note "without
  adverse finding" (1882, the world of the epilogue). The windows follow the term calendar (R-13): the
  inquiry no earlier than the summer of 1881, the answer filed between the April and October sittings.
- **The Caleb audit (R-8, updated R-11) — three planted facts, one per act, no statement.** (i) Act One, *What
  a No Costs*: the ledger page with the boy's keeping-money, entered in Joshua's hand under a year that
  predates the mortgage. (ii) Act Two (via Hoss Tyler's seized day book, R-11): Tyler's bound ledger lists a
  **pair of boys' shoes** in a year Jacob's house had only one child of his own. (iii) Act Three, *The Mill
  Sold*: the deed by which Joshua sells the mill reserves a right of way for "Caleb, my brother's son" — a
  phrase that means nothing to the clerk and everything to the reader. If a reader assembles it before *The
  Surrender*, the planting worked; if the narration ever explains it, cut the explanation, not the fact.
- **The epilogue's three errors are fixed, and they are the only errors allowed to persist** (R-12). The
  county history's wrong year is **1877**, always, in every draft; the report spells **Elisha Councill**;
  the dime novel's fourth chapter title is the sentence quoted in §1 and is never varied. If a revision
  "corrects" the county history, it has stopped being a county history.
- **The day book and its exhibit transcript (R-11, R-18).** Two entries in Hoss Tyler's bound day book and
  their dates are fixed for the whole book: **`"by order of the agent"`** (in Tyler's hand, the day Parrish
  settled Matthew's store debt in *The Store Debt*) and the **pair of boys' shoes** dated to a year Jacob had
  one child. In *The Missing Page* (Ch. 15, R-18), Parrish examines Joshua over a clerk's **certified exhibit
  transcript** copied from Tyler's seized ledger to join `Parcel A` as *"premises connected therewith,"* and
  Joshua spots the **skipped folio number** where Matthew's `"by order of the agent"` page was withheld from
  the public exhibit copy. Either entry moving in date, folio order, or wording shifts both Act Two and Act
  Three with it. Harper's *don't* is **one sentence, quoted back verbatim exactly once, in *The Burning*** —
  if a draft quotes it twice, cut the second.
- **Lish Councill (R-10, R-19).** Fifteen, of North Fork, shot behind Harper's barn on the day Matthew named.
  Always **Lish** in the cove's mouths, **"a boy"** in the government's paper until Margaret forces Parrish to
  strike `"a boy"` and spell **`Elisha Councill`** in his Commissioner's report (*E1*, R-12) in exchange for
  her sworn fire affidavit in *The Deposition* (Ch. 23, R-19); the deputy who fired is numbered, never named.
  One death per side in this book — his, then the deputy's — and his comes first, which is what makes Act
  Two's restraint read as restraint rather than as authorial cowardice.
- **War & 1868 bone structure — CLOSED (R-16).** Joshua enlisted Union in summer **1862** over State Line Gap
  and mustered out at **Knoxville in 1865** (do **not** invent a company letter or regiment number on the page;
  the real Mitchell County Unionist units organized 1863–64 after 1862 scout service). His discharge paper sits
  in the drawer in *What a No Costs*, never explained against the July 1, 1862 liquor tax. Jacob stayed on the
  mountain 1862–65 keeping the farm and Caleb (closing §4's open war item). The 1868 NC Constitution appears
  only through paperwork (`Cranberry Township` rolls, delinquent tax-sale memory, and `Art. X §6` on Margaret's
  deed) — **no Klan subplot, no party speeches, and never the noun "Reconstruction" in a character's mouth.**
- **Trade register — CLOSED (R-17).** Brennans at work use verbs (*making*, *running*, *a run*, *the whiskey*);
  mountain and county-town speech says **`blockader` / `blockading` / `blockade whiskey`**; Parrish and Bureau
  filings say *illicit distiller* / *untaxed spirits*; **`moonshiner` and `moonshine` appear in outside print
  only** (newspapers, *E2*, *E3* — zero hits in narration or dialogue).
- **POV ledger (R-4).** Every scene belongs to Joshua or Margaret. A scene that needs a fact only Jacob,
  Caleb, Matthew, Harper or Parrish could supply must get it from an object, a report, or a silence — and
  the linter's `lex:other-heads-interiority` row will flag the draft when the discipline slips.
- **Banned-from-this-book list:** "Whiskey Rebellion" applied to 1878–81 (belongs to 1791–94); **any
  train seen on the page at any date** (R-5 — the earlier rule "no locomotive before mid-1882" is now
  stricter: there is no locomotive, only the powder and the report of it); Avery County before 1911;
  **Newland** before 1911–12 (in 1878 say *Old Fields of Toe*, R-15); any depot, post office, or incorporated
  boomtown at **Elk Park** before 1882–85, or company-town scrip/hotel at **Cranberry** before July 1882 (R-15);
  **"moonshiner" / "moonshine" in narration or any mountain mouth** (outside print only, R-17).
- **Margaret's deed and the privy-examination stall (R-7, R-12, R-15, R-20).** In *Did She Know?* (Ch. 26,
  October 1881 Statesville term; Judge Robert P. Dick named, never voiced), Margaret lays down her folded
  pre-1861 Watauga root deed (sole copy after the 23 March 1873 Boone courthouse fire) and stands on `NC
  Const. 1868 Art. X §6`, N.C. Laws 1848–49 ch. 41, and *Scott v. Battle*, 85 N.C. 184 (1881): no clerk's
  privy-examination certificate exists giving Jacob or any man a lease or estate in her barn, and in her one
  spoken sentence on knowledge she refuses to clear `Parcel B` by naming Caleb or Joshua — holding `Parcel B`
  over on exceptions (`"the tract remains in contest"` in *E1*, R-12) while mortgage and defense costs force
  Joshua to sell `Parcel A` in Ch. 27 (*The Mill Sold*).
- **Closing sound (R-5, R-15).** The final beat's noise is a blast off the state-line ridge or a local hammer —
  never a whistle, never an engine, because Hampton (15.5 air / ~19.9 gorge miles down Doe River Gorge) was the
  rail head in October–November 1881. Pending ask R-13.

---

## 11. Change log

- **2026-10-26 — Scene Proposal 3 of 3 ruled → R-20 (*Did She Know?*, Ch. 26; all `canon §12` scene proposals
  CLOSED).** At the October 1881 Statesville term (Judge Dick named, never voiced), Margaret produces her
  folded pre-1861 Watauga root deed (sole copy after the 23 March 1873 Boone courthouse fire, R-15) and stands
  on `NC Const. 1868 Art. X §6`, N.C. Laws 1848–49 ch. 41, and *Scott v. Battle*, 85 N.C. 184 (1881) — no
  certified privy examination exists giving Jacob or any man an interest in her barn, and a married woman
  cannot lose her separate realty by estoppel without one. In her single spoken sentence on knowledge she
  refuses to clear `Parcel B` by naming Caleb or Joshua, stalling the federal decree into *E1*'s `"the tract
  remains in contest"` (R-12) while mortgage and defense costs force Joshua to sell `Parcel A` in Ch. 27 (*The
  Mill Sold*). **All 28 chapters in `canon §12` now have locked structural beats.**

- **2026-10-26 — Scene Proposal 2 of 3 ruled → R-19 (*The Deposition*, Ch. 23, and *The Burning*, Ch. 14).**
  Harmonized Ch. 14 across R-9, R-11, and the outline: Caleb's network stored blockade whiskey under William
  Harper's barn floor over his Act One *"don't"*, and Parrish's hired possemen staved in the kegs and set the
  barn afire without Parrish's order. Locked *The Deposition* (Ch. 23): Margaret requires Parrish to strike
  `"a boy"` and write **`Elisha Councill`** in his Commissioner's report (*E1*, R-10/R-12) before swearing one
  strictly true sentence — Parrish stood in the road calling his hired men off when the blaze caught in the
  split kegs stored on Harper's floor — saving Parrish's career with Washington while putting sworn proof of
  stored spirits into the federal record against the cove.

- **2026-10-26 — Scene Proposal 1 of 3 ruled → R-18 (*The Missing Page*, Ch. 15).** After *The Burning* (Ch.
  14) — with Jacob already serving his two years from the April 1879 Statesville term (R-13) — Parrish turns
  the civil *in rem* libel onto Joshua's mortgaged farm (`Parcel A`: mill, water race, cart road) as
  *"premises connected therewith"* and puts the *Stowell* knowledge question directly to Joshua over a
  certified exhibit transcript copied from Hoss Tyler's seized day book (R-11). Joshua spots the skipped folio
  number where Matthew's settled store account (`"by order of the agent"`, R-10) was omitted from the public
  exhibit copy. Cleaned up the pre-R-11 Caleb-audit shoe-entry cross-reference in §10 and Tyler's hand note in
  `character-bible.md`.

- **2026-10-26 — Q-14 ruled → R-17 (§9 blocking queue CLOSED).** Mountain and county-town speech says
  **`blockader` / `blockading` / `blockade whiskey`** (`LEAD`: Kephart; Dan Pierce — wartime blockade origin,
  never explained on the page), while around their own still the Brennans use work-verbs (*making*, *a run*,
  *the whiskey*); Parrish speaks the statute (*illicit distiller*); and **`moonshiner` / `moonshine` are
  restricted to outside print** (newspapers, *E2*, *E3*), matching R-14. `vocabulary-tone-bible.md` moves to
  v1.0 with updated `FLAG` and `NOTE` rows. **All 14 §9 questions are now ruled (`R-1` … `R-17`).**

- **2026-10-26 — Q-13 ruled → R-16.** War and Reconstruction enter **as bone structure in objects and
  paperwork, with zero speeches**: Joshua walked over State Line Gap into the Union army in summer **1862**
  (same summer Congress passed the July 1, 1862 distilled-spirits tax to fund his army) and mustered out at
  **Knoxville in 1865** (unit kept unnamed on the page so 1863–64 formal regiment muster dates are never
  violated); Jacob stayed on the mountain 1862–65 dodging Home Guard sweeps and raising Caleb (closing §4's
  open item and locking R-8); and the **1868 NC Constitution** sits in the room simultaneously as the township
  tax-sale regime the cove distrusts and as `Art. X §6` shielding Margaret's forty acres (R-7). Excluded: Klan
  subplots (Rutherford/McDowell, not Cranberry Twp), party speeches, and "Reconstruction" in dialogue. Only
  **Q-14** remains open in §9.

- **2026-10-26 — Q-12 ruled → R-15.** Setting locked near **Cranberry (`Cranberry Forge`) and Elk Park, NC**,
  and the 1878–81 county corrected from the Drive notes' "Burke" to **`Cranberry Township, Mitchell County`**
  (seat **Bakersville**; Mitchell formed 16 Feb 1861; Burke ended here in 1833, Yancey 1833–49, Watauga
  1849–61, Avery 1911). Kept Burke and Watauga where history puts them — on the older grants and antebellum
  deeds in Margaret's cedar box, whose courthouses at Morganton (1865) and Boone (1873) both burned before Act
  One opens. Closed all §3 distance blanks; tightened R-5's acoustic geometry (Hampton railhead 15.5 air miles
  behind Doe River Gorge; 1880–81 blasting crews 4–7 miles across State Line Gap); banned `Newland` (1911–12)
  in the lexicon and guarded `Elk Park` / `Cranberry Forge` against post-1882 boomtown anachronisms; fixed the
  `Burnsville` → **Bakersville** county-seat slip in `related-documents-bible.md` and
  `research-gaps-and-questions.md`; and moved R-13/R-14 up into §1 where they belong.

- **2026-10-26 — Q-11 ruled → R-14.** "The Whistlers" survives as **owned invention**, but only in the
  institutions' mouths: the Bureau's papers, the county paper, the dime novel. The hollow never names itself,
  which makes Act Two's network a set of decisions with no minutes but the enemy's, and gives the withheld
  train a shared word — a whistle is the signal on the ridge and the sound down the valley, and the book never
  says so in one sentence. "The Regulators" rejected (it imports 1768–71 and reads as a borrowed thesis). The
  lexicon gains a NOTE row so every occurrence gets its speaker checked.

- **2026-10-26 — Q-10 ruled → R-13.** Statesville and the real term calendar; 21 Apr 1879 / 21 Apr 1881 /
  17 Oct 1881 / November 1881 fixed; Judge Dick named and unmouthed; the outline's "about a year left"
  flagged for a one-line fix. **The chapter map was rebuilt as v1 with 28 chapters:** two added (*The Term,
  1879*; *The Deposition*), *The Return* moved ahead of *The Surrender* because the release date precedes it,
  the 8/8b split merged into one Margaret chapter, and every cross-reference in this file changed from a
  chapter number to a chapter title, so the map can be reordered again without breaking anything. Act One is
  now free to be drafted: none of its eight chapters depends on an unanswered question.

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

| 2026-10-26 | **Q-4 ruled → R-7** (Margaret owns the parcel the still stands on, as a separate estate).
  **Corrects R-6's "the still goes in Joshua's barn"** to the adjoining ground; adds the three-parcel map to
  §3; retitles map ch. 23 "Did She Know?" and reassigns ch. 13's fire to Harper's storage barn; adds the
  "connection" argument as Parrish's second move; §4 Margaret entry rewritten with the two `INVENT` items
  she still needs. New research asks R-15 (the deed and privy-examination record in the chosen county) and
  R-16 (NC homestead exemption amount 1868–1882, and whether a state exemption could be opposed to the
  United States at all) — the first is now load-bearing, the second is the fact a reviewer will look up. |
  agent |

| 2026-10-26 | **Q-5 ruled → R-8** (Caleb is Joshua's firstborn, given to Jacob's house in 1862). Rewrote
  §4's Caleb and Joshua entries, added the "Caleb audit" three-clue anchor to §10, re-pointed map ch. 12,
  21 and 25, and invented the mother (Elsie Brennan née Byrd, d. 1862 — one object, no scene). New research
  ask **R-17**: whether intra-family "giving" of a child is documented in these counties and what legal
  status a kept child had (guardianship dockets), because the book's central arrangement is now `INVENT`
  and I would rather it be `INVENT` about something that happened. | agent |

| 2026-10-26 | **Q-6 ruled → R-9** (Parrish's cost is a Bureau audit of his own conduct). Added the
  deposition proposal at ch. 22, the do-not-name-Burns rule and the three-document correspondence anchor to
  §10, rewrote §4's Parrish entry, and closed the outline's "vindicated promotion" ending by demoting the
  promotion to a footnote. New research ask **R-18**: the Commissioner's annual reports and the Department's
  practice on inquiring into agents' conduct 1876–1883, because the audit must be a real mechanism and not a
  mood. | agent |

| 2026-10-26 | **Q-7 ruled → R-10** (the store, the day, the paper). Repurposed the "boy on the ridge"
  candidate into **Lish Councill, 15**, whose death in the Act One raid is the load R-9's audit has to carry;
  renumbered map ch. 8 / 8b around the new sequence; promoted Tyler's day book to the exhibit proving
  knowledge (half of Q-8, pre-decided); proposed the ch. 22 name-for-affidavit trade, `OPEN`. Added the Lish
  anchor to §10 and fixed `docs/period-audit.md` §7, which had carried three character names imported from
  the sibling project — Asa, Eudy and Frank do not exist in this outline. New ask **R-19** (whether a
  discretionary informer allowance could be fixed and go uncashed, and how the order was drawn). | agent |

| 2026-10-26 | **Q-8 ruled → R-11** (both minor men promoted; Tyler a creditor, not a Judas). Moved R-8's
  second planted clue out of Margaret's accounts into Tyler's day book, which is where arithmetic is kept in
  this book; put Harper in ch. 5 and made ch. 13 the price of his being right; rewrote both cast entries with
  ages (`INVENT`: Tyler 63 b. ~1815, widower, one son in Tennessee; Harper 60 b. ~1819, four sons); added the
  day-book and single-quoted-*don't* anchors to §10. New ask **R-20**: how a merchant's day book reached
  evidence in a WDNC revenue matter, 1879–82, and whether NC law let a book speak for itself. | agent |

| 2026-10-26 | **Q-9 ruled → R-12** (diegetic print only: report, county history, dime-novel title page; no
  author's note). Wrote the three artifacts into §1 as a specification and into §12 as E1–E3, replacing the
  outline's optional epilogue scenes; assigned the fates (Jacob's 1895 death struck, Margaret one line,
  Caleb a title page, Joshua nothing); fixed the three deliberate errors in §10; confirmed the subtitle
  stays 1878–1881. `docs/bibles/related-documents-bible.md` gets a new §1b with the models to find, and
  period-audit gets ask **R-21** (a real WDNC agent's annual-report paragraph, one western-NC county history's
  actual sentence about the revenue law, and the 1879 Redmond novelty's title and publisher). | agent |

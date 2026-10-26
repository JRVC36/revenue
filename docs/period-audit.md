# Period Audit — *REVENUE*

**Status: v1 — audit of the OUTLINE, plus the ledger for every year the book will print.**
**Verdict: the 1878–1881 frame is sound and better than the author thought; the failures are not
anachronisms, they are an unlabeled war, one misnamed agency, a legal mechanism nobody wrote down, and
a railroad that has not arrived yet.**

Format is the house format from *The Bound Tree* `period-audit.md`: finding → severity → what to do.
Severity: `MAJOR` = breaks the book's authority if a reader knows the period · `MINOR` = fix in the
draft · `NOTE` = already resolved, recorded so it doesn't drift back.

---

## 1. Resolved by ruling (canon §1)

| # | Finding | Severity | Resolution |
|---|---|---|---|
| A-1 | The outline is a stage outline (SETTING/TIME/cast-with-ages), the author's standing ruling is prose. | MAJOR | **R-1.** Novel. Stage idiom is *translated*, not preserved: setting → weather, ground, labor; "they exit" → what the body does on the way out; the age list → facts shown through work and debt. Working subtitle: *A Novel · Western North Carolina · 1878–1881* (1878–1882 was proposed at R-2 and pulled back in by R-5). |
| A-2 | Zero railroading in a western-NC 1880s novel, and the author's instinct to add it. | MAJOR | **R-2.** ET&WNC is present as approach: grading powder, a federal surveyor's transit, men who leave for the grade. **No rails, no whistle, no train on the page before mid-1882.** Elk Park is not reached until June 1882; Boone not until 1919. |
| A-3 | The engine of the plot is "90 cents a gallon" treated as a moral abstraction. | MAJOR | **R-3.** The engine is **forfeiture of the land**. The triable question is not "does Jacob owe" but **did Harper know and permit**. Every downstream decision (POV, Margaret's standing, the barn fire, the trial, the pardon) is now driven by this. |

## 2. Fixed at the outline level

| # | Finding | Severity | What to do |
|---|---|---|---|
| B-1 | **"the Whiskey Rebellion"** used of 1878–81 (Act Three). | MAJOR | That name belongs to 1791–94 in western Pennsylvania and to nothing else. The 1877–1885 trouble was **the moonshine war**; a North Carolina paper in 1878 called it a **whiskey rebellion** in lower case, with no "the", and it did not stick. In narration: "the trouble on the liquor tax," "the moonshine war." `tools/check.py` BANs the capital-R phrase. |
| B-2 | Agents called the **IRS** and the "federal tax authority." | MAJOR | **Internal Revenue Service is post-1913.** Through 1882 the agency is the **Bureau of Internal Revenue**, in the Treasury Department; its men are *revenue agents*, *inspectors*, *gaugers*, *deputy collectors*; mountain speech says **revenuer** and mostly means a man with a badge and no money. `BAN`. |
| B-3 | Judge **Albert G. Walker**, "federal judge, Asheville." | MAJOR | Wrong man, wrong town. Walker sat in the Eastern District and was removed in 1872 over the Ku Klux Act. **Western District of North Carolina** was created 4 June 1872 and its only judge in 1878–82 was **Robert Paine Dick**, a Grant appointee and ex-Confederate legislator who had been barred from the bench by the ironclad oath and was later praised for "a kindly temper in administrating the internal revenue laws." **There was no federal courthouse building in Asheville until 1892**; terms were held in the county seats — for our district, Statesville sat on the **third Mondays of April and October**. This is the best fact in the audit: the judge is a reconstructed Confederate who enforces the law gently and precisely, and the court has to travel to a courthouse it rents. |
| B-4 | "Astill still hidden in the woods for six years." | MINOR | The cove has not had a war since April 1865; the 1878 men were not hidden from *war*, they were hidden from *the revenue*. If "six years" stays, the war being described is not the Civil War. Keep the line only if it means **the six years since the 1872 creation of the district** — which is a much better reading: the cove has had a federal office in its county for six years and has spent them not caring. |
| B-5 | Matthew: "He'd rather be anywhere else, doing **any other job**." | MINOR | A farm boy in 1878 Watauga has no employment market to be anywhere else in. Cut or convert: *he would take the grade work, the lumber yard, the mines in the next county* — which also seeds the railroad. |
| B-6 | Two acts both titled "THE RECKONING." | MINOR | Structural, not historical, but it is a real defect in the source: Act Two and Act Three collide. Act Three becomes **"THE RECKONING"** alone; Act Two is retitled (open choice — "THE INFORMER," "THE WEIGHT OF IT"). |
| B-7 | Act One says the "Whiskey Rebellion" is "simmering" in 1878 while Act Three calls 1881 the same war. | NOTE | Consistent with the real chronology (Raum's crackdown begins **August 1876**; the 1878 pardon fails; Redmond's gang is active 1878–81), so nothing to cut — only the name to fix (B-1). |

## 3. Verified facts the book may print as-is

| Fact | Print form | Source standing |
|---|---|---|
| Tax rate | **90 cents on the proof gallon**, in force 3 Mar 1875 – 27 Aug 1894 | `LEAD` (TTB historical rates; Duke's *Cyclopedia of Industrial Products*, 1881, "remains up to the date of the present writing"). Rate is the same in every year of the book — do not let a character say it went up. |
| Rate math | ~2.5 gal from a bushel of corn at ~25¢/bu → **the tax is roughly the whole value of the whiskey** | `LEAD`. Say it in corn and gallons, never in "the tax burden." |
| Forfeiture | **the still, the apparatus, and all the real estate and premises connected with it**; *U.S. v. Stowell*, 133 U.S. 1 (1890): land is reached as to the distiller and to anyone who "knowingly has suffered or permitted"; *Dobbins' Distillery v. U.S.*, 96 U.S. 395 (1878): **a landlord forfeits though his tenant's fraud was unknown to him**; *Two Barrels Whiskey*: an unknowing mortgagee is protected | `LEAD`, cases read in part. This is R-3's engine. The 1868 act's own words: "all real estate and premises connected herewith." |
| Registration was a property test | No distiller's bond unless the owner is **seised in fee simple, free from any mortgage, judgment, debt or lien whatsoever**, else **the written consent of every lienholder**, the United States' lien first (Act of 27 July 1868 §8, 15 Stat. 125) | `LEAD`. This answers the modern reader's "why not just register?" with a period answer that indicts the law: **a mortgaged mountain farm cannot legally be a lawful distillery, and the only lawful path needed the creditor's signature** (canon R-6: the creditor is the man who also grinds their corn). |
| Landlord's ignorance is no defense | *Dobbins' Distillery* (1878): the owner's land is forfeited even where the tenant's fraud was **unknown to him**; *Stowell* extends it to anyone who "knowingly has suffered or permitted … or has connived" | `LEAD`. Under R-6 this doctrine is aimed at the POV character himself, so the book must be scrupulous that a **presumption** is not a finding — the trial's drama is Joshua's status, not his secrets. |
| No still in a dwelling | §12 of the same act forbids a still in a dwelling house or any connected shed/yard/enclosure | `LEAD`. Jacob's barn is not just shelter for a still; it is the thing that makes the whole farm liable. |
| Bond and notice amounts | Distiller's bond $300; notice of intent to distill posted 10 days before, at the agent's office | `LEAD`, partial. Pin down the posted-notice form before printing the wording of a notice. |
| Penalties | Distilling without a bond / with intent to defraud: **$1,000–$5,000 and 6 months–2 years** (Rev. Stat. §3281, re-enacted Act of 8 Feb 1875 §16, 18 Stat. 310); the 1868 act: **$500–$5,000 and 6 months–2 years**, and **books not produced → the land is forfeit** | `LEAD`. Jacob's "two years" is the statutory maximum: the sentence is not a judge's mood, it is a schedule. |
| Informer money | **Moieties repealed** for claims accruing after 1 Aug 1872; payments thereafter were **discretionary** by the Commissioner with the Secretary of the Treasury's approval, capped at one moiety and $5,000 per case, and **no right vested until the money was fixed and paid** | `LEAD` (Syllabus by the Court; *United States v. Morris*, 26 F. Cas. 1323). This is why Matthew's "he wasn't paid" is period-correct — and it must be written as the *system's* lie, not as one white man's: the law changed six years before Matthew was born into it. |
| The pardon | A **blanket federal pardon** in 1878 for revenue offenses; many kept distilling anyway; *Tennessee v. Davis*, 100 U.S. 257 (1879) on federal enforcement jurisdiction | `LEAD`. Act One's "prohibition failed / the pardon failed" beat is real. |
| Violence scale | WDNC: **Deputy Marshal W. Burns shot in the back from ambush, 13 Apr 1874**; **C. B. Brockus killed 14 Feb 1893** in a prison rescue — that is the district's toll in a decade and a half. Nationally ~**25 agents killed 1876–80** (~6/yr) against ~20/yr deputy marshals dying in the West. | `LEAD` (US Marshals Service history; counts via secondary). **Used to deflate Act Three, not inflate it:** our book's murder is the *unusual* event, and the marshal's response is paperwork because paperwork is what the Bureau had. |
| Redmond | b. 1854 (so **24** at his killing of Dep. Marshal Alfred Duckworth, 1 Mar 1876, **Transylvania County**, not McDowell); captured 7 Apr 1881; tried from **25 Aug 1881 on eight counts of selling liquor and two of conspiracy — not for the killing**; sentenced to **10 years at Auburn and $2,600**; pardoned by Arthur, 1884; d. 1906 | `LEAD` (NC Dept. of Natural and Cultural Resources; ECU on the 1881 Cobb campaign pamphlet; *NC History* on the 1879 dime novel). Epilogue correction for Caleb: **the mountain's own outlaw celebrity is a print product** — the 1879–81 dime novel and campaign pamphlet exist; the cove's legend of Caleb must arrive the same way, through paper. |
| Moonshine vocabulary in NC | The men were first called **blockaders**, their product **blockade whiskey**; "moonshiner" only became common in the 1870s | `LEAD` (Dan Pierce, *Our State*). Basis for Q-14. |
| Rail head in the book's last year | **Hampton, TN, 22 Aug 1881** is the nearest steel to a Watauga hollow in Oct 1881; Elk Park is not reached until mid-June 1882. Consequence: **no whistle, no engine sound carries into the cove in 1881** — the closing beat must be powder or a local hammer (canon R-5) |
| Railroad chronology | chartered TN 24 May 1866 (5-ft gauge) → ~5 mi by Apr 1870 → abandoned 1874 → East Tennessee & Western North Carolina Railroad, **3-ft gauge, chartered 6 Mar 1879** → construction from **Sept 1880** → Johnson City–Hampton **22 Aug 1881** → **Elk Park mid-June 1882** → **Cranberry 3 July 1882** → Boone 1919; telegraph along the line 1883 | `LEAD` (ETSU archives corporate entity; American-Rails; local histories). The 3-ft gauge is why the line could be built by hand through that canyon, and why it could reach Elk Park before Boone. |
| Court calendar | WDNC terms at **Statesville, third Mondays of April and October** | `LEAD` (NC Reports front matter, contemporaneous). Constrains Act Two: the trial is at a sitting, and everyone in the mountains times travel by the term. |
| A married woman's land was her own | NC Const. 1868, Art. X §6: property owned before marriage "shall be and remain the sole and separate estate and property of such female, and shall not be liable for any debts, obligations, or engagements of her husband," devisable/conveyable "as if she were unmarried" (with the husband's written assent) | `LEAD` — quoted in *Perry v. Stancil*, 237 N.C. 442 (1953), which recites the 1868 text; **pull the constitution itself and the 1868–69 implementing act before printing a line of the clerk's dialogue.** This is the foundation of R-7. |
| A wife's conveyance required a privy examination | For a homestead deed, "no deed made by the owner of a homestead shall be valid without the voluntary signature and assent of his wife, signified on her private examination according to law" (NC Const. 1868, Art. X, homesteads and exemptions); a married woman's separate examination was the mechanism for barring dower as well | `LEAD` (1868 constitution as printed in the 1868 pamphlet; the rule survived until 1945 — G.S. 47‑14.1 repealed the privy examination for instruments after 7 Feb 1945, which confirms it was live in 1878). **Held in reserve as a plot device: a missing certificate.** |
| Dower was *restored* in 1868 | North Carolina limited dower to land the husband owned at his death from 1784; the 1868 constitution returned to the common-law measure (land owned at any time during the marriage), which is why relinquishment had to be pleaded and certified again | `LEAD` (secondary legal-genealogy survey; **needs the session-law cite before the word "dower" appears in the manuscript at all**) — R-7 makes dower unnecessary to the plot, so if the cite cannot be found, do not print it |
| State exemptions vs. the United States | The modern rule is categorical ("No provision of a State law may exempt property… from levy for the collection of any Federal tax"), and the 1880–81 Supreme Court holding behind it is generally cited for the proposition that a state homestead exemption cannot be set up against a federal judgment | `LEAD`/unverified for the 1878–81 form. **Q: does it belong in the book at all?** Under R-7 Margaret does not need an exemption argument — so keep this out of the trial chapter unless the citation is found (ask R-16) |
| Cask marks | heads and hoops branded "U.S."; "A" stamped on a tierce, "B" on a hogshead; rectifiers' and dealers' bonds $2,000; retail-dealer bond $100 | `LEAD`. Good texture; only print a mark we can say why a character notices it. |

## 4. `OPEN` — cannot be printed until researched

Full asks with "what I need back" in `docs/research-gaps-and-questions.md`; the load-bearing five:

1. **Redmond's trial record** (8/1881, which courthouse, verdict text) — sets the epilogue and Caleb's template. `MAJOR` if skipped.
2. **WDNC term docket / local paper 1878–82 for real revenue cases** — the trial chapter should be an adaptation of a real case, not invention. `MAJOR`.
3. **ET&WNC "Watauga Memorial" claim that the line reached Watauga Co. by 1879 and was halted by the 1880 financial crisis** — if true, a surveyor could legally stand in our cove in 1878–79 with federal money behind him, which is R-2's whole Act One. `MAJOR`.
4. **The 1880 U.S. Census schedules for the candidate county** — household size, corn and whiskey, illiteracy, mules, church membership: the numbers the book implies when it says "twelve families." `MINOR`.
5. **Whether any federal troops were called into western NC 1878–82, and by whose request.** Without this, Act Three's "the President sends troops" is an invention and must be softened; the Georgia precedent is unverified. `MAJOR`.

13. **What civil work was under way within hearing of the cove in autumn 1881** — the Buford/Irwin
    turnpike contracts, county road and bridge blasting, a quarry. Canon R-5 makes the book's final sound a
    grading blast or a hammer, and I will not print "a blast off the ridge" if there is a documented local
    sound that is *also* true. `MINOR` (safe generic available) — **but it is the last sentence of the
    novel.** *What I need back:* Watauga County court minutes 1879–1882 for road overseers/contract
    blasting, and any 1881–82 newspaper notice of ET&WNC work north of Elizabethton. `OPEN` **R-13**.

15. **The deed that made Margaret's forty acres hers.** R-7 rests the book's legal spine on a married
     woman's separate estate, so the record has to exist in the county we choose: the father's will or deed
     of 1866–68, the registration, and (if the plot uses it) the *absence* of a privy-examination
     certificate on any later dealing. `MAJOR` — this is the most load-bearing unverifiable object in the
     project. *What I need back:* Watauga (or Mitchell/Caldwell per Q-12) deed book index entries 1860–1872
     for a conveyance to or from a married woman, and one complete sample certificate of private examination
     so I can copy its wording rather than invent it. `OPEN` **R-15**.
16. **Whether a North Carolina homestead exemption could be pleaded against the United States in 1879–81,**
     and the exemption's dollar amount in those years. Now only a *defensive* fact — R-7 gave Margaret a
     fee, not an exemption — but a reviewer will look it up. `MINOR`. *What I need back:* N.C. Code §§ on
     exemptions as amended 1873–1879, and Watson v. Merrill / Cole v. Berry for the federal rule. `OPEN` **R-16**.

14. **Inheritance and deed practice in the candidate county, 1820–1865.** R-6 makes Joshua the elder who
     inherited the improved farm and mortgaged it, while the younger brother keeps no land. That pattern
     (eldest son takes the improved place, youngest moves to the side hollows, all of it arranged in the
     county court rather than by statute) is the shape I expect to be true, but I have not verified it in
     Watauga/Burke/McDowell deed books. `MINOR` for the fiction, `MAJOR` for the mortgage's date and the
     lienholder's identity — which is now the man the book turns on. *What I need back:* two or three
     probate/land transitions in the chosen county showing which son received the improved acres, and
     whatever the mortgage instrument actually looked like there (merchant's bond, bond for title, deed of
     trust). `OPEN` **R-14**.

Secondary items: Thav (Avery Co. Museum), a 17-year-old's 1879 diet, an 1870s Asheville lawyer's fees and circuit, and
the *Whiskey War in Alabama 1877–1885* (Bibb County) as structural comparison — including its "Regulator" revenge
killing in Feb 1879, which is the likeliest real source of the outline's "Whistlers."

## 5. `LEAD` → `USER` protocol

Every row in §3 and §4 is `LEAD` (secondary source or my reading) until it is confirmed from an archival
source, at which point the citation replaces the row's text. An invented object is `INVENT` and legal to
print **only if it is period-possible and carries no date claim**; the moment it carries a date, a law, or
a real person's act, it becomes a §3 row and needs a source. `tools/check.py` flags every printed year with
the note "needs a line here," so the ledger cannot fall behind the draft.

## 6. Language

Applied from `docs/bibles/vocabulary-tone-bible.md` and enforced by `tools/check.py` (BAN/FLAG/NOTE).
Two notes on the mechanism, so nobody is surprised twice:
- The lexicon is **read out of the bible file**, not hardcoded; editing §7 of that bible edits the linter.
- Bibles are excluded from the sweep by default (`--all` skips them; `--all --meta` checks them anyway),
  because a document that lists banned words in order to ban them is not a draft that used them.

## 7. Sensitivity

Same house standard as *The Bound Tree*:
- **Cherokee presence.** The cove's fields were cleared by people who were pushed out generations earlier.
  One line of *fact* — a townsite, a plum tree, a path too straight to be a cow trail — no mysticism, no
  speaking for, no relic-hunting by a white character.
- **Veteranhood without heroism.** Joshua, Asa, Eudy and Frank served; the book's interest is what the
  war left in the room, not the war.
- **Mountaineer speech without mockery.** No eye dialect, ever (`BAN` at the level of the whole project).
  Rhythm carries it: parataxis, refusal, concrete nouns, understatement.
- **Violence.** One death in the book (Act Two's deputy) and one attempted (Act Three's Parrish). Both are
  followed by *paperwork*, which is the actual horror of this system.
- **Addiction is not a mood.** Parrish "drinks to blunt what he has to do" is a stage line; in prose it must
  cost something specific and dated (laudanum and whiskey are both period; the cost is the ledger, not the
  feel).

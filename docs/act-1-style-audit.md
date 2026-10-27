# Act One Style Audit & Line-Edit Report (Chapters 1–8)

**Scope:** Complete prose-level line edit and historical-fiction style audit of Act One (`manuscript/01-the-water-is-right.md` through `manuscript/08-the-cold-still.md` — `31,878` total words; `23,966` narration words).

**Governing Constraints:** `canon/canon-v1.md` (`R-1…R-20`), `docs/author-style-guide.md`, `docs/bibles/vocabulary-tone-bible.md`, and standing house craft/ecology rules (plain visual English, concrete physical action early, cove ecology free of shaded-stream alder stands, in-scene physical scale on first touch, strict single-POV restraint with interiority only when alone, zero eye dialect).

---

## Corpus-Level Quantitative Summary

| Metric / Tic | Pre-Audit (Act 1) | Post-Audit (Act 1) | Notes |
|---|---:|---:|---|
| Total Act One words (`compile.py`) | `31,896` | `31,878` | Prose-level tightening only; zero plot or scene cuts |
| Linter (`tools/check.py --stats`) | `0 BAN, 0 FLAG` | `0 BAN, 0 FLAG` | `0.0` filter words/1k; `0.3` em-dashes/1k; `0` `"not X — it's Y"` |
| Narration median sentence (`readability.py`) | `11.62` | `11.75` | Every chapter `11` or `12`w (`0` dead-middle warnings; `0` sentences `> 48w`) |
| Audiobook digits (`dist/revenue-audiobook.txt`) | `0` | `0` | 100% TTS clean |
| `quietly` | `18` | `2` | Retained only Caleb tending the hurt mule (Ch. 1) & Parrish's `"Revenue officers"` correction (Ch. 6) |
| `evenly` | `12` | `0` | Cut all 12 dialogue-tag crutches (`said evenly`) |
| `flat` / `flatly` | `71` | `31` | Cut 40 mechanical placements (`laid flat`, `rested flat`, `said flatly`); preserved earned acoustic/material uses (`flat iron`, `frost-flat`, `flat metallic carbine crack`, `flat as cold anvil iron`) |
| `clean` / `cleanly` | `59` | `33` | Trimmed adverbial filler (`spat clean`, `poured clean`, `dismounted clean`) while keeping literal cleanliness/clear grain |
| `neat` / `neatly` | `27` | `3` | Removed recurring `pinned neat`, `tucked neat`, `crossed neat`, `neat brown ink` tics |
| `square` / `squarely` | `29` | `18` | Trimmed adverbial filler while preserving squared timbers, stones, and statute volumes |
| `rhododendron laurel` (double plant noun) | `6` | `0` | Replaced stacked synonym pair with `rhododendron` or `laurel` |
| `Not a muscle [in jaw / round mouth] moved` | `3` | `0` | Cut stock stoicism formula across Caleb, Parrish, and Joshua |
| Mannered VSO / OSV inversions | `21` | `0` | Restored natural SVO order (`Flat it shut`, `Neither ear did he pick up`, `Dry and bottom-up it went`) while keeping natural locative inversions |

---

## Per-Chapter Audit Logs

### Chapter 1 — *The Water Is Right* (`manuscript/01-the-water-is-right.md`)

#### Editorial Change Log
- **[Category K — Grammar / Dangling Modifier]** Fixed dangling participial modifier in the wheel-pit inspection:
  - *Before:* `Left unstrapped into frost, winter ice would tear the wheel apart.`
  - *After:* `Left unstrapped into frost, the rim would tear apart under winter ice.`
- **[Category A & K — Ecology / Redundancy]** Cut three instances of stacked double-naming `rhododendron laurel` (where mountain speech uses *laurel* for *Rhododendron maximum* or narrative uses *rhododendron*, not both glued together):
  - *Before:* `he ran down the rocky bank through the rhododendron laurel.` / `through the rhododendron laurel toward Jacob and Margaret’s clearing.` / `through the hemlocks and rhododendron laurel below Joshua’s dam.`
  - *After:* `...through the rhododendron.` / `...through the laurel...` / `...through the hemlocks and rhododendron thickets...`
- **[Category D & H — Dialogue Tags & Modifier Tics]** Removed six redundant tone-policing tags (`evenly`, `quietly`, `flatly`) where dialogue cadence and action already supplied the register (`Caleb went on evenly`, `Margaret said quietly`, `Jacob said flatly`, `Joshua said evenly`, `He set them quietly`). Retained Caleb walking `quietly` to the scraped bay mule in Scene 1, where physical quietness keeps a panicked animal from bolting.
- **[Category F — Emotional / Thematic Overstatement]** Cut editorial gloss after Margaret's line on the breezeway:
  - *Before:* `“Jacob won’t eat salt put on your mill book, Joshua,” Margaret said. Plain fact sat in her voice. “You know your brother.”`
  - *After:* `“Jacob won’t eat salt put on your mill book, Joshua,” Margaret said. “You know your brother.”`
- **[Category E — Sentence Rhythm & Consecutive Starters]** Merged choppy `He dropped... He jumped...` in the bridge rescue (`Dropping the brown mare’s rein, he jumped straight off the bank...`) and varied consecutive `Jacob` paragraph starters at the firebox (`Jacob looked round...` / `He did not stand up.`).
- **[Category D — Modifier Cleanup]** Trimmed `flat wood` → `level oak`, `tucked the strap end clean` → `tucked the strap end`, `pinned neat at the collar` → `pinned at the collar`, `Turning squarely on his heel` → `Turning on his heel`, `neat brown ink` → `brown ink`, and `wiped his steel pen clean` → `wiped his steel pen dry`.

#### Flagged Questions / Checkpoints
- None blocking. Preserved Ch. 1's pure "world before" structure (`cut_store_rumor_keep_pure_world_before`) and the four-stake split-chestnut trough choice across the white-oak boundary stone (`make_trough_choice_ch1_spine`). Kept the primary eight-bushel Jonas Ridge corn-to-whiskey freight arithmetic intact in Joshua's evening ledger reflection (`canon §8.8`), cutting its verbatim repetition in Chapter 5 instead.

#### Running Style Notes
- **Preserved:** Intentional parallel ledger structure at the end of Scene 4 (`On the left leaf stood...` / `On the back leaf stood...`) and tactile proof-vial bead physics (`Small round bubbles rose clean along the surface`).

---

### Chapter 2 — *Powder on the Ridge* (`manuscript/02-powder-on-the-ridge.md`)

#### Editorial Change Log
- **[Category K — Style Guide §1.2 Cast-Sheet Age Ban & Contradiction]** Replaced Hendrick's bare stage-direction age (`man of forty`) with weathered physical detail, and resolved an internal contradiction in the compass-box observation where the needle could not simultaneously "stand loose" and press "hard against the west pin":
  - *Before:* `Behind the tripod stood a lean, square-shouldered man of forty in laced calfskin ankle-boots and brown corduroy trousers tucked neat above the mud...`
  - *After:* `Behind the tripod stood a lean, weather-creased man with gray at his temples, wearing laced calfskin ankle-boots and brown corduroy trousers tucked high above the mud.`
  - *Before:* `Its blued needle stood loose. Hard against the west pin it quivered, nowhere near north.`
  - *After:* `Its blued needle had swung off center and hung trembling against the west brass pin, nowhere near north.`
- **[Category E — Mannered Inversions]** Restored natural word order in three inverted constructions:
  - *Before:* `Both went under the hickory withe on his pack-saddle...` → *After:* `Caleb turned the stakes over once, tapped the red clay off their tips against his boot heel, and shoved both stakes under the hickory withe on his pack-saddle...`
  - *Before:* `Flat across the black calluses lay a broad new silver dollar...` → *After:* `Across the black calluses lay a broad new silver dollar...`
  - *Before:* `Neither ear did he pick up.` → *After:* `He left both ears lying in the weeds.`
- **[Category G & D — Stock Stoicism Tic & Adverbs]** Cut `Not a muscle in his jaw hurried` (first of three near-identical jaw/mouth formulas in Act 1), `Caleb said evenly`, `cut clean into the dark rock` → `cut into the dark rock`, `folded neat` → `folded`, and `written clean` → `written`.
- **[Category A — Word Echo]** Varied consecutive `Joshua` starters in the opening blast scene (`The miller stood still...`) and cut `flat` in `flat slate sill` where `flat iron strap` followed two lines down.

#### Flagged Questions / Checkpoints
- None. Preserved `Elk Park` strictly as an unincorporated forty-acre border meadow (`R-15`) and kept the `100-ft` engineer's steel ribbon vs. `66-ft` Gunter's chain contrast and dipping-needle magnetite physics (`VERIFIED`, *E&MJ* Apr 1878).

#### Running Style Notes
- **Preserved:** Caleb's clipped spoken syntax (`“Cut a slot clean across the saddle above Sugar Fork”`) where `clean` belongs to mountain speech rather than narrator habit.

---

### Chapter 3 — *The Office* (`manuscript/03-the-office.md`)

#### Editorial Change Log
- **[Category K — Grammar / Dangling Participle & Double `flat`]** Fixed a dangling participial phrase where Parrish's eyes appeared to read aloud, while removing a double `flat` in fourteen words:
  - *Before:* `He opened the upper volume flat at the first slip. His gray eyes dropped to the fine print, reading at the flat, even pace of a clerk calling scale weights.`
  - *After:* `He opened the upper volume at the first slip. Then he read out the fine print in the dry, level cadence of a clerk calling scale weights.`
- **[Category K — Literal Logic & Cast-Sheet Age]** Fixed disembodied `His eyes... looked out` + `flat and expressionless` (`His gaze met Joshua’s once across the oak rail without expression. Then he turned toward the street glare.`) and replaced Parrish's bare cast-list age (`a man of thirty-eight`) with observable physical bearing (`a spare, dark-haired man shy of forty`), eliminating three consecutive `His` sentence openings.
- **[Category F & H — Over-Explained Register Gloss (`R-17`)]** Trimmed narrator explanation after Parrish's `illicit distiller` reply so the lexical collision against the sheriff's `blockade whiskey` lands without editorial coaching:
  - *Before:* `“Then no illicit distiller fires a furnace on Cranberry waters,” Parrish said quietly — neither sneering nor pressing, only setting the government’s two words square on the walnut board where the sheriff had laid the mountain word.`
  - *After:* `“Then no illicit distiller fires a furnace on Cranberry waters,” Parrish said, setting the government’s two words down without heat where the sheriff had laid the mountain word.`
- **[Category A, D & E — Echoes, Modifiers & Starters]** Fixed `Not a line moved round his mouth... wrote two neat lines` (`His mouth did not stir. Dipping one steel pen shallow in the pewter stand, he wrote two short lines...`); cut `Harper asked quietly`, `Parrish said evenly`, `spat clean over` (`spat past`), `stacked neat` (`stacked dry`), `sending the warm smell... clean across`, `rested flat`, `clean blotter` (`white blotter`), and smoothed the closing `He` chain in the mill-lot stable beat.

#### Flagged Questions / Checkpoints
- None. Preserved all statutory citations (`Rev. Stat. §§ 3152, 3163, 3258, 3262, 3266, 3281`, `19 Stat. 152` abolition of Supervisors, `20 Aug 1878` Raum cutoff, `21 Apr 1879` Statesville docket, and Collector Mott / Judge Dick on paper/title only per `R-13`).

#### Running Style Notes
- **Preserved:** Squire Wiseman's mid-stream epigram (`“Hard thing to hide a bottom meadow under laurel.”`) and Harper's understated twenty-year neighbor code on Ledger hill.

---

### Chapter 4 — *What a No Costs* (`manuscript/04-what-a-no-costs.md`)

#### Editorial Change Log
- **[Category I & Canon `R-8` Guardrail — Paternity Hint Removal]** Removed an explicit narrator comparison linking twenty-one-year-old Caleb's axe-stroke directly to Joshua's own wrist-snap immediately after the `1866–69` keeping-money drawer scene (`R-8`: Caleb's parentage must **never be stated, confirmed, or hinted at in the prose** beyond the three planted documentary/object clues):
  - *Before:* `His broad wrists dropped square on the helve with the exact unhurried snap Joshua brought down on an ash wedge at the millstone hoist. Every bolt split clean through the heart at one blow.`
  - *After:* `His broad wrists dropped on the helve without hurry, splitting every bolt through the heart at a single blow.`
- **[Category I — POV Restraint]** Cut omniscient glimpse into Parrish's future intent after Joshua's refusal:
  - *Before:* `Once he inclined his head, taking a price he would not ask twice.`
  - *After:* `Once he inclined his head.`
- **[Category A, D & F — Double `quietly` & Simile Tail]** Fixed back-to-back `Quietly he let it settle... “More than that,” he said quietly` within twelve words; trimmed redundant explanatory tail `wholly free of heat, stating a rule of measure as a surveyor reads a needle` to `without heat`; cut `Parrish answered evenly`.
- **[Category E & K — Diction & Syntax]** Changed `Steep black ink crossed the slip` → `Upright black ink crossed the slip`; replaced clipped absolute `Key hung back behind the clock, he unbolted his door` → `After hanging the key back behind the clock, he unbolted his door`; smoothed `Across the sill blew a dry yellow leaf` → `A dry yellow leaf blew across the sill` and consecutive `Joshua / He / He` chains at the walnut table; trimmed six mechanical uses of `flat`, `square`, and `clean`.

#### Flagged Questions / Checkpoints
- None. Preserved **Clue #1** (`1866–69` keeping-money foolscap *To Jacob's house* alongside the `10 Nov` `$24` receipt and folded `Aug 1865` Knoxville Union discharge) intact word for word.

#### Running Style Notes
- **Preserved:** Single-word dialogue architecture (`“No,” Joshua said.`) and the physical inventory of the twenty-four dollars (`36` half-dollars, `4` quarters, `$5` greenback) earned four pounds at a grinding.

---

### Chapter 5 — *Keep Making It* (`manuscript/05-keep-making-it.md`)

#### Editorial Change Log
- **[Category J — Repeated Exposition]** Cut the fourth repetition of the Jonas Ridge shelled-corn freight arithmetic from Jacob's rain-barrel speech, replacing it with a compact mountain-freight clause that keeps Jacob's argument sharp without re-explaining Chapter 1's math:
  - *Before:* `Jacob’s jaw set square. “Eight bushels of shelled corn hauled two days over Jonas Ridge brings two dollars when valley men feel charitable. Four mouths in that house eat salt...”`
  - *After:* `Jacob looked down at his callused knuckles. “Valley wagons don’t pay mule-feed on shelled corn, Joshua. Four mouths in that house eat salt...”`
- **[Category I — POV Inference]** Removed Joshua-POV mind-reading of William Harper's motive during the barn silence:
  - *Before:* `He stood looking straight at Jacob five breaths longer, waiting to see if one other voice under the rafters would stand beside him.`
  - *After:* `He stood looking straight at Jacob five breaths longer around the silent circle.`
- **[Category A, D, E & H — Repetitions, Inversions & Tags]** Cut `flat as calling scale weight` (which repeated Ch. 3's exact phrase); replaced `In stepped old Amos Councill... patched neat at both elbows` with natural SVO order (`old Amos Councill from North Fork stepped inside, past seventy... patched at both elbows`); fixed double `clean` inside Jacob's Beech Knob speech (`two miles clear down Yellow Mountain Turnpike`); fixed `rhododendron laurel` → `laurel`; cut `Joshua said evenly`, `Jacob asked quietly`, `Caleb said quietly`, `set his damp wool hat square`, and `swept... clean off`.

#### Flagged Questions / Checkpoints
- None. Preserved William Harper's canonical warning verbatim (`“Don’t fire another kettle this winter, Jacob, or that man will take the roofs off men that never made a gallon.”` — `canon §10`) and referred to Lish's turkey-wing bone strictly as `bone` / `blasts` (zero banned railroad-lexicon words).

#### Running Style Notes
- **Preserved:** The single italic `*Click.*` of Caleb's `.44` hammer drawn to half-cock and Joshua sweeping Rafe Winters's tobacco quid off his mortgaged mill-barn planks after the neighbors leave.

---

### Chapter 6 — *Gauger's Work* (`manuscript/06-gaugers-work.md`)

#### Editorial Change Log
- **[Category K — Arithmetic / Continuity Fix (`112 lbs` vs. `224 lbs`)]** Fixed a concrete load-weight error between Scene 1 and Scene 4: in Scene 1 Joshua packs **two** two-bushel bags (`112 lbs` net white bread meal per bag = `224 lbs` total; `six bushels` delivered across the morning/week order) and carries the first bag inside in Scene 2; in Scene 4 when Tyler tells him to bring the second sack in and Joshua empties **both** bags into the chest, Tyler previously offered to chalk only `hundred and twelve pounds` (one bag's weight):
  - *Before:* `Inside the doorway Hoss Tyler spoke flatly. “Bring your other sack in off the mare, Joshua. I’ll chalk your hundred and twelve pounds on the bin lid till the twenty-eighth.”`
  - *After:* `Inside the doorway Hoss Tyler spoke without inflection. “Bring your other sack in off the mare, Joshua. I’ll chalk your two hundred and twenty-four pounds on the bin lid till the twenty-eighth.”`
- **[Category D & K — Mismatched Adverb & Cast-Sheet Age]** Replaced incongruous `Gently he looked up at the bare pine boards` (applied to Parrish inspecting Tyler's wall for a missing `$25` tax stamp) with `Parrish stepped straight before Hoss Tyler’s slant-top desk and glanced up at the bare pine boards`; replaced Kerr's bare age + double `neatly` (`damp riding gloves tucked neatly... fifty-year-old stranger with neatly trimmed gray side-whiskers`) with `damp riding gloves tucked through his belt. Beside him worked a gray-whiskered stranger past fifty in gold-wired spectacles`.
- **[Category F & G — Over-Explanation & Jaw Tic]** Trimmed legal over-explanation and the second occurrence of `Not a muscle round Parrish's mouth moved` after Tyler hands over his witnessed protest:
  - *Before:* `Three seconds passed while Parrish read the crisp, witnessed lines certifying in the merchant’s own hand that every page in both books was original, contemporaneous, and genuine. Not a muscle round Parrish’s mouth moved.`
  - *After:* `Three seconds passed while Parrish read the witnessed lines in which Hosea Tyler certified every page of both books in his own hand.`
  *(Joshua's closing line — `“He let you certify the whole book for him.”` — now lands with full dramatic snap because the narrator hasn't already explained the evidentiary trap fifty lines earlier.)*
- **[Category E — Consecutive Paragraph Starters & Inversions]** Varied four consecutive `Matthew` paragraph openings on the store porch (`Matthew swung down...` / `The boy stepped sideways...` / `His eyes dropped...` / `Both boots stopped dead...`); restored SVO order in `He lashed Hoss Tyler’s two calfskin ledgers tight across the horse’s loins` and `Four sets of iron shoes backed clear of the rail and wheeled south...`; cut nine redundant `flat`/`neat`/`clean`/`evenly`/`quietly`/`very` modifiers while **retaining** `“Revenue officers, Mister Carson,” he said quietly` (where Parrish's drop in volume is the beat itself, setting up Kerr's single canonical `"revenuer"` line per `R-17`).

#### Flagged Questions / Checkpoints
- None. Preserved the single Act One / novel-wide deployment of `"revenuer"` / `"revenuers"` (`R-17`), the `19 Stat. 152` transfer of `§ 3163` book-inspection authority, and Kerr's `109` stem reading at `56°F` = `104 proof` (`3.12` proof gallons).

#### Running Style Notes
- **Preserved:** Tactile hydrometer physics (`The weighted bulb sank. Twice it bobbed, then settled dead still in the clear liquor.`) and Matthew's three untraded muskrat pelts hanging from his saddle-strings on the ride home.

---

### Chapter 7 — *The Store Debt* (`manuscript/07-the-store-debt.md`)

#### Editorial Change Log
- **[Category K — Literal Logic (`bare right glove`)]** Corrected transferred epithet where Parrish's leather glove was called `bare` instead of his hand:
  - *Before:* `Parrish drew his bare right glove smoothly back over his knuckles. Cleanly he hooked the brass throat-chain of his cape into its link.`
  - *After:* `Parrish drew his wet right glove back over his bare knuckles. He hooked the brass throat-chain of his cape into its link.`
- **[Category I — Strict Single-POV Discipline]** Cut two breaches of Joshua's limited POV in Scene 3–4 (one future-omniscient narrator intrusion inside Matthew's perspective, and one off-stage tactical explanation Joshua could not have witnessed before `6:00 a.m.`):
  - *Before:* `Behind Tyler’s corn-crib stood a bay mule he could never ride back up Elk Cove while he lived.`
  - *After:* `Out behind Tyler’s corn-crib stood a bay mule the boy could not ride back up Elk Cove.`
  - *Before:* `Two hundred yards up the road, squarely across the mouth of Elk Cove below William Harper’s meadow, sat five mounted men and a laden government pack-horse, dim as iron statues in the mist. Parrish had placed them there before six o’clock so no horseman from Cranberry Forks could ride past them or reach Beech Knob.`
  - *After:* `Two hundred yards up the road, blocking the mouth of Elk Cove below William Harper’s meadow, sat five mounted men and a laden government pack-horse, dim as iron statues in the mist.`
- **[Category E — Mannered VSO Inversions]** Converted five inverted constructions to crisp SVO order (`Hoss Tyler unhooked his tin lantern, stepped through the narrow partition doorway...`; `The side door swung halfway open. Matthew stepped across the sill.`; `Tyler swung the heavy cover open. He turned straight to the back third...`; `The Deputy Marshal unrolled a square of black tarred oilcloth on the pine counter. He stacked both calfskin volumes inside.`).
- **[Category A, D & H — Repetitions & Tags]** Fixed back-to-back `combed flat with water` / `ordinary flat voice` (`combed sleek with water`); fixed `rhododendron laurel` → `laurel`; replaced `brought back clean from Bakersville` with `brought back unmarked from Bakersville` (clearer evidentiary meaning); cut `asked quietly`, `said evenly`, `said quietly`, `said flatly`, `crossed neat`, `neat brown heading`, `four neat stacks`, `swept... cleanly`, and `leaned flat` (`leaned low`).

#### Flagged Questions / Checkpoints
- **Confirmed clean (`Category K` Blocking):** Verified Joshua's sightline and hearing from the unlit scale-room six feet behind Hoss Tyler's walnut desk (`two-foot tally-hatch` + partition door `six inches ajar`), and verified that Joshua's knife-slash drops his two `112-lb` flour bags in the mud behind Tyler's crib so the claybank mare can take the steep sheep-trace unweighted. Preserved Tyler's verbatim `Folio 114` settlement receipt (`canon §10`, `R-9`, `R-18`).

#### Running Style Notes
- **Preserved:** Kept `one flat metallic carbine crack punched straight up through the dripping hemlocks` — an earned acoustic `flat` contrasting a `.44` saddle carbine in wet fog against black-powder quarry blasts.

---

### Chapter 8 — *The Cold Still* (`manuscript/08-the-cold-still.md`)

#### Editorial Change Log
- **[Category E — Cluster of 10 Mannered Inversions]** Chapter 8 had accumulated the highest density of VSO/adverb-fronted inversions in Act One (`Out of the barn came...`, `Scratch went the lead pencil...`, `Up swung the heavy board`, `Flat it shut without a slam`, `Out onto the porch they stepped`, `Over the top rail vaulted Joshua Brennan`, `Down dropped the barrel`, `Up through the white fog clinked...`, `Past the revenue horses she went`, `Straight ahead he looked`, `From his dark coat breast came...`, `Dry and bottom-up it went onto the shelf`, `Outside her gate halted...`). Converted all thirteen to direct, unforced physical syntax:
  - *Before:* `Scratch went the lead pencil down the ruled foolscap sheet.` → *After:* `The lead pencil scratched down the ruled foolscap sheet.`
  - *Before:* `Her palm came down on the walnut lid. Flat it shut without a slam.` → *After:* `She set one palm on the walnut lid. It shut without a slam.`
  - *Before:* `She washed Jacob’s cold tin cup and scalded it clean. Dry and bottom-up it went onto the shelf.` → *After:* `She washed Jacob’s cold tin cup, scalded it with boiling water, and set it bottom-up on the shelf to dry.`
- **[Category K — Physical Sightline Anchor (`R-10` / `R-19`)]** Grounded how Margaret physically reads Parrish's small lead-pencil entry (`“one boy, killed running at junction barn”`) from four feet away so her Act Three courtroom callback in Chapter 23 (`R-19`) is unimpeachable on blocking:
  - *Before:* `From his dark coat breast came a narrow black-leather pocket memorandum book. Uncapping a brass lead pencil four feet from where Margaret rose upright with wet red clay soaking both knees of her apron, Parrish stood bareheaded at the sled tail and wrote in his neat clerk’s hand. / Plain in black lead stood the entry before he shut the cover.`
  - *After:* `He drew a narrow black-leather memorandum book from his coat breast and rested it open on the oak tailboard, four feet from where Margaret rose upright with wet red clay soaking both knees of her apron. Uncapping a brass lead pencil, Parrish stood bareheaded at the sled tail and wrote in his small, upright hand where every word lay plain under her eyes before he shut the cover:`
- **[Category G, D & H — Stock Tic, Double `clean`, `flat` & Tags]** Cut third occurrence of `Not a muscle in his bearded jaw moved` when Joshua drops his eyes at Jacob's `"Where's Matthew?"`; fixed double `clean` in consecutive scrubbing sentences (`smelled fresh as split timber`); replaced `in a flat look` with `in a steady look` and `spoke the price flat` with `read the price aloud`; cut `said quietly`, `said evenly`, `asked quietly`, and nine mechanical uses of `flat`, `neat`, and `square` while **preserving** `every word flat as cold anvil iron` in William Harper's indictment over Lish's body.

#### Flagged Questions / Checkpoints
- **Continuity note on Statesville mileage (`Category K`, non-contradictory — flagged for awareness):** In Chapter 3 (`L137`, sheriff's dialogue, speaking from **Bakersville**) the sheriff estimates `"Sixty-five miles if the river's down"` to Statesville; in Chapter 8 (`L205`, Margaret's narration, reckoning wagon-road distance from **Elk Cove** near the Tennessee divide — 22 miles north of Bakersville — via the mountain turnpike and valley wagon roads) the text reads `"Ninety wagon-miles led down the mountains to Statesville, three full days in the saddle each way"`. Because Elk Cove sits `22` miles above Bakersville (`22 + ~68 = 90` wagon-miles), the two numbers actually fit the geography accurately! Left intact; noted here so Act Two's Chapter 13 journey from Elk Cove to Statesville uses the same `~90` wagon-mile / three-day saddle measure consistently.

#### Running Style Notes
- **Preserved:** **Clue #2** (`one folded dark wool shawl, brass-pinned — forty cents`, untouched seventeen springs since a five-year-old boy came across the branch, per `R-8`), Margaret's twenty-winter threshold line one boot-length short of her father's barn sill (`Art. X §6` / `R-6`), and her lye-and-shuck scouring of the twelve red-clay boot tracks.

---

## Final Act One Style Report (Chapters 1–8)

### 1. Most Common Prose Weaknesses Found Across Act One
1. **Default Emotional-Suppression Adverbs in Dialogue Tags (`quietly` 18×, `evenly` 12×, `flatly` / `flat` tags):** Because the novel's dramatic ethic prizes emotional containment, the first draft leaned on `said quietly` and `said evenly` to enforce restraint externally even when the dialogue, syntax, and silence already carried it. Cutting 28 of those 30 tags actually made Joshua, Margaret, Harper, and Parrish *quieter* and more formidable on the page.
2. **Overworked Geometric/Cleanliness Modifiers (`flat` 70×, `clean` 58×, `square` 29×, `neat` 27×):** Words that belong naturally to mill carpentry (`flat iron`, `squared granite post`) bled into nearly every ordinary gesture — hands resting `flat`, papers laid `flat`, coats `pinned neat`, stirrups `crossed neat`, men spitting `clean` or dismounting `clean`. Trimming over half of these restored physical crispness to the remaining carpentry and acoustic uses.
3. **Mannered Verb-First / Object-First Inversions (`21` instances, peaking in Chs. 7–8):** Constructions like `Neither ear did he pick up`, `Scratch went the lead pencil`, `Flat it shut`, and `Dry and bottom-up it went onto the shelf` strained toward folk-ballad elevation at the exact moments when plain, hard SVO declarative sentences hit hardest.
4. **Occasional Micro-Breaches of Single-POV Restraint & Over-Explained Subtext:** In four spots (Ch. 3 `neither sneering nor pressing...`, Ch. 4 `taking a price he would not ask twice` and comparing Caleb's wrist-snap to Joshua's, Ch. 5 `waiting to see if one other voice...`, and Ch. 7 `Parrish had placed them there before six o'clock` / `while he lived`), the narrative stepped half an inch outside strict observational bounds or explained a tactical trap the reader had just watched happen.
5. **Stacked Botanical Double-Naming (`rhododendron laurel`, `6×`):** Pairing `rhododendron` and `laurel` as a two-noun compound blurred mountain usage (where *laurel* alone names *Rhododendron maximum* slicks, or *rhododendron* names the shrub in narration).

### 2. Strongest Stylistic Qualities Preserved in Act One
1. **In-Scene Physical & Economic Grounding (`canon §8.8`):** Weights, measures, proof readings, and 1878 sums never feel like research notes because they live in muscle and household arithmetic — `six silver dollars` measured as `eight full days` of ten-hour axe sweat at `75¢/day` (Ch. 1), a `66-ft` Gunter's chain sized against a barn lot vs. Hendrick's `100-ft` spring-steel ribbon (Ch. 2), a `$25` retail liquor stamp weighed as `five full weeks` of wages (Ch. 6), and Margaret's `40¢` shawl priced as `two dozen autumn eggs` or half a winter day at the wheel (Ch. 8).
2. **Procedural & Material Authority:** The millwheel wedge and split-chestnut trough hydraulics (Ch. 1), magnetite pulling the dipping needle forty degrees downward (Ch. 2), Kerr's Tralles hydrometer stem settling at `109` in `56°F` spirit for `104` true proof (Ch. 6), and Parrish's two-step `§ 3163` book examination followed by the Marshal's `Folio 114` *subpoena duces tecum* (Chs. 6–7) create inexorable legal tragedy without melodrama.
3. **Distinct Four-Way Lexical Register (`R-17`) Without Eye Dialect:** Mountain neighbors, county officials, Hoss Tyler, and federal officers sound unmistakably distinct through cadence, syntax, and noun choice (`blockade whiskey` in county/store speech vs. work-verbs among the Brennans vs. Parrish's `illicit distiller`, with zero apostrophe-dropped eye dialect).
4. **Bimodal Sentence Cadence:** Across all eight chapters, periodic sentences of physical labor and statutory consequence (`25–42` words) break cleanly against short declarative hammer-strokes (`“No,” Joshua said.` / `Joshua kept silent.` / `Both boots stopped dead on the frosty boards.`), maintaining a narration median of `11.75` words and `1.39` syllables/word.

### 3. Recurring Authorial Tics to Watch For in Act Two & Act Three
- **Guard the four-word tic cluster (`flat`, `clean`, `square`, `neat`):** Allow at most `2–3` earned material uses per chapter, never as default verb padding (`laid flat`, `stepped clean`, `folded neat`).
- **Ban `said quietly` / `said evenly` / `said flatly` while drafting:** Let room acoustics, hand business, or silence before a reply carry vocal temperature.
- **Never repeat `Not a muscle in his jaw/mouth moved`:** Replace with concrete hand, eye, or tool business (e.g., Joshua's thumb stopping on a hemp sack-tie, Tyler's hand freezing above the sand-shaker).
- **Keep SVO spine under pressure:** In raid, courtroom, and eviction scenes (Chs. 13, 14, 15, 23, 26), resist verb-first inversions (`Up stood...`, `Down came...`).
- **Check load/ledger math across scene breaks:** Whenever sacks, bushels, gallons, interest, or court miles cross from Scene 1 to Scene 4, verify net totals (`2 × 112 lbs = 224 lbs`; `Elk Cove = 90 miles` vs. `Bakersville = 65–68 miles` to Statesville).

### 4. Patterns Intentionally Preserved Rather Than Flattened
- **Ledger, Scale, Debt, and Boundary Motifs:** Repeated references to `Folio 114`, the `forked white oak` and `squared granite post`, the `two split-chestnut troughs`, `twenty-four dollars`, and `the third Monday of April` are the structural engine of Act One and were kept sharp and intact.
- **Verbatim Statutory & Evidentiary Anchors:** Parrish's Bakersville citations, Harper's barn warning (`canon §10`), Hoss Tyler's witnessed January 18 protest, Tyler's March 4 `Folio 114` receipt, Parrish's March 4 memorandum line (`"one boy, killed running at junction barn"`), and the March 4 *Notice of Seizure* were preserved intact.
- **Earned Fragments & Parallelism:** Short single-breath beats (`*Click.*`, `Ten minutes past six.`, `No second shot followed.`) and parallel closing images (water sliding down the chestnut trough across the boundary stone at the end of Chs. 1, 3, 4, and 5) are deliberate architectural rhymes, not accidental repetition.

### 5. Places Where Restraint, Canon Discipline, or Ambiguity Needed Special Care
- **Caleb's Parentage (`R-8`, Chs. 4 & 8):** Preserved the `1866–69` keeping-money sheet (Ch. 4) and the `40¢` brass-pinned wool shawl kept seventeen springs (Ch. 8) untouched while excising the explicit physical wrist-snap comparison between Caleb and Joshua in Ch. 4 so the secret stays strictly inside the three authorized clues.
- **Single-POV Observational Boundaries (`R-4`, Chs. 4, 5, 7, 8):** Kept Joshua and Margaret strictly inside what each can physically see, hear, and reckon when another human being is in the room, reserving interior reckoning for solitary beats (Joshua at his mill desk/drawer; Margaret with her cedar box, scrubbing brush, and barn door).
- **Joshua's Unspoken Knowledge After `Folio 114` (Chs. 7–8):** Preserved the devastating silence between Joshua and Hoss Tyler in the dark scale-room and Joshua's refusal to answer Jacob's `"Where's Matthew?"` in Margaret's yard (`"Didn't ride up the cove with me, Margaret"`), letting the crossed stirrups on the riderless bay mule deliver the truth to Margaret without melodramatic confrontation.

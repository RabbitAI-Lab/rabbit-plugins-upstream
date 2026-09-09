# EIA Process Intelligence

Positioning: extract structured facts about a company's real production lines from environmental impact assessment (EIA) reports, audit the numbers for regulatory gaming, infer process routes and equipment selection, and accumulate the results into a growing triple-store ledger.

Core method: EIA filings rarely disclose per-step yields, so end-to-end yield is back-calculated from the material balance (key input such as substrates vs. chip output), which then locates the bottleneck step. A full worked demonstration (fictionalized IR-detector case) lives in `examples/format-demo-ir-detector-en.md`.

## Design Principles (override everything below)

1. **Queries first.** Extraction and inference serve only the "7 must-answer questions". Before adding any entity/relation/field, there must be at least one recorded real failed query as justification (see references/ledger-schema.md).
2. **EIA numbers are not facts.** An EIA report is a declaration made under regulatory gaming. Before any number enters the ledger it must pass two gates — interest review (which regulatory consequence does it affect, and in which direction would the company distort it) and physical cross-validation (low-risk fields back-calculating high-risk fields).
3. **Caliber discipline.** Every fact carries a source (filename + page + verbatim quote) and disclosure date. 【Disclosed】 and 【Inferred】 are strictly separated. Back-calculated outputs are always ranges with an explicit caliber note, never point values.
4. **One vocabulary.** The process→equipment mapping library IS the ontology's vocabulary layer (equipment-class alias normalization). The mapping library and the ledger share one equipment-class vocabulary — one asset, not two.

## The 7 Must-Answer Questions

| # | Question | Primary evidence |
|---|----------|------------------|
| 1 | Real capacity and build-out cadence (vs. the fundraising narrative) | Product scheme, construction phases, approval info |
| 2 | Process route identification | Process sequence + materials + pollutants (three evidence faces) |
| 3 | Equipment selection tier (country of origin / generation / density) | Equipment list, models, counts vs. capacity |
| 4 | Yield and unit-consumption back-calculation; locate the bottleneck step | Material balance |
| 5 | Inferring process existence from pollution signatures | Hazardous chemicals / hazardous waste / specialty gas lists |
| 6 | Falsifying conflicts between EIA caliber and company claims | All fields vs. BP / interviews / announcements |
| 7 | Field credibility grading and back-calculation | references/field-credibility.md |

## Workflow

### Phase 0 — Obtain the filing (when the user hasn't provided one)

Search in order (distilled from practice; append as you learn):
1. National EIA information disclosure platform; the provincial / municipal / county ecology-and-environment bureau sites of the registration / project location ("EIA acceptance / proposed approval / approval decision" sections)
2. National permit-to-operate (pollutant discharge permit) platform (permit originals + annual execution reports)
3. Legacy repositories such as EiaCloud's assistant and the eiafans forum (for historical versions)

Query patterns: full company name; `<project name> EIA report form`; `<project name> environmental impact report acceptance` + city name. One project often has three published versions (acceptance / proposed approval / decision) — the acceptance version is the fullest. Report forms (short) and full reports (complete) differ greatly; get both.

### Phase 1 — Structured extraction

Extract the PDF section by section into a fact table (field list and gaming grades in references/field-credibility.md):

- Project overview and approval info: approval number, approval date, approval level, EIA preparer, nature of construction (new / expansion / retrofit)
- Product scheme and capacity: by product, by spec, by construction phase
- Process flow: transcribe step by step with pollution-generation markers; convert flow diagrams node by node into text, noting "transcribed from flow diagram"
- Equipment list: name / model / count / source (purchased / leased / reused)
- Raw and auxiliary materials and hazardous chemicals: name / annual usage / hazard properties
- Material balance and water balance: input-output per step
- Pollution sources and treatment facilities: generation point → pollutant → treatment → discharge destination
- Construction schedule and investment: phasing cadence, total investment, environmental protection investment

Every fact row carries a source. OCR scanned files first; transcribe table data verbatim from the original tables — avoid paraphrase drift.

### Phase 2 — Gaming review

Load references/field-credibility.md: tag every numeric field with a `game_risk` (high / med-high / medium / med-low / low) and a distortion direction (inflate / understate / split). For high-risk fields run the three interest-review questions: which regulatory consequence does it affect? which direction benefits the company? any threshold-hugging signature?

Gaming traces found (build-big-vs-permit-small, project splitting, hidden process steps, mass production under a pilot label, etc.) go into a standalone list and are booked via the ledger relation `gaming_trace` — they double as governance due-diligence evidence.

### Phase 3 — Cross-validation

Load references/cross-validation.md: use low-risk trust anchors (equipment counts, building / outfall / treatment-facility physical info) to back-calculate high-risk fields (capacity / materials / emissions). Use external materials as available: permit execution reports, hazardous-waste transfer manifests, environmental penalty records, IPO prospectus construction-in-progress, bidding and customs data.

Tag every field with a `status`: `declared` / `cross-validated` / `conflicts-with-external`. Do not change the number when conflicts arise — the conflict itself goes into the report.

### Phase 4 — Inference

- **Process route**: fix the route with three evidence faces — process sequence, material inputs, pollution signatures (e.g., T2SL vs. VOx, monolithic vs. two-piece packaging, dry vs. wet cleaning); cite each evidence face.
- **Equipment selection**: load references/mappings/<track>.md and infer along "process step → equipment class → tier signal → country / representative vendors". For steps missing from the mapping library, tag 【mapping missing】 and log to the backlog — never improvise.
- **Yield / unit consumption**: back-calculate end-to-end yield and the bottleneck step from the material balance; output a range + caliber footnote ("estimated under EIA-caliber self-consistency").
- **CAPEX intensity**: equipment counts × market price ranges (corroborated by external quotes) → investment intensity per unit capacity, checked against the raise amount and capacity commitments.

Mark every inference 【inferred】, with the chain spelled out: which facts → which rule → which conclusion.

### Phase 5 — Deliver the report

Fixed five-section structure (Markdown):
1. Structured fact table (with source / game_risk / status)
2. EIA caliber vs. company caliber comparison table
3. Gaming-trace list
4. Inference summary (process route / equipment selection / yield range / CAPEX intensity)
5. Interview question list — every missing, vague, or conflicting point in the EIA turned into a DD question

### Phase 6 — Book into the ledger

Append triples per references/ledger-schema.md. Key points:
- Append-only JSONL, one file per industry track, stored in the DD project workspace at `{project dir}/eia-ledger/<track>.jsonl`; no business data lives in this skill directory
- Every entry carries source / game_risk / status / disclosure date / booking date
- Questions the ontology cannot answer go into `failed-queries.md` in the same directory; change the schema only after real failed queries accumulate

## Mapping library maintenance (references/mappings/)

- One file per industry track; row shape: EIA signal (process / pollutant / hazchem keyword) → equipment class (vocabulary) → tier signal → representative vendors by country → reading rationale
- Append rows after every engagement; write nothing without evidence; mark uncertainty with 【to verify】 and state the verification path
- Renaming an equipment class = a vocabulary change; sync the vocabulary section in references/ledger-schema.md

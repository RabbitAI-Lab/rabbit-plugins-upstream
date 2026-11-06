---
name: dataset-validation
description: Validate an incoming dataset for a stated use, investigate defects and missing coverage, and recommend acceptance, restricted use, correction or rejection. Use for delivery QA and fitness-for-use decisions; use a measurement-specific workflow for a standalone metric calculation.
license: MIT-0
---

# Dataset validation

Determine whether the delivered data can support the intended decision. Preserve the delivery and separate checks performed, observations, inferences and unverified conditions.

## Establish the contract

Identify the customer question, entity and relationship grain, population/geography, time window, essential fields and consequential errors. Inspect supplied documentation before asking for missing information. Clarify only ambiguity that could change the decision; continue useful checks and label provisional rules.

Record file/source version and relevant event, publication and retrieval dates. A timestamp on a download is not the observation date. Define identifiers as strings, distinguish individuals, organizations, campuses and relationships, and agree which repeats are legitimate.

## Check the delivery

Inspect actual sheets/files, row boundaries and parsing before trusting a summary. Keep originals unchanged and produce proposed corrections separately.

- Check required columns, types, blanks, allowed values, units and dates. Requiredness and ranges come from the use or source contract. Do not invent “normal” clinical ranges or universal thresholds.
- Check keys, duplicate records, foreign keys, cross-field constraints and aggregation grain. One provider at two locations can be valid. Missing keys cannot establish an identity.
- Reconcile input records, exclusions and output records. Inspect population and subgroup coverage, freshness and differences from a comparable earlier delivery. A strong overall rate can conceal an unusable target cohort.
- Verify essential facts against evidence appropriate to the field and date. A plausible identifier or valid schema does not prove a current affiliation, procedure volume or license. Independent evidence must not merely mirror the same upstream source.
- Sample semantic checks using a stated selection method and material subgroups. Separate defect discovery from estimation; disclose a curated sample and unresolved truth labels. Do not generalize a small clean sample into population-wide perfection.

For a CSV, [profile_csv.py](scripts/profile_csv.py) supplies read-only structural evidence:
```sh
python3 scripts/profile_csv.py delivery.csv --key provider_id location_id --required provider_id facility_id
```
Use actual field names. The profiler does not validate truth, eligibility, freshness or coverage. For a workbook, use an available spreadsheet tool; do not flatten formulas or hidden sheets without inspection.

## Investigate and decide

Trace a failed check to parsing, schema, source fact, matching, transformation or an invalid rule before proposing a fix. Compare a valid case or another relevant entry path. Outliers warrant investigation; they are not automatically errors. Preserve both conflicting values and their provenance.

Return a compact brief:
- Intended use and inspected delivery.
- Material findings with affected records, field evidence, check status (passed, failed, unverified) and consequence.
- Coverage and uncertainty, with explicit numerators and denominators.
- Recommendation: accept, accept with stated limits, hold for correction, or reject for this use.
- Smallest corrective action, owner/input needed if known, and what should be rechecked.

Tie severity and acceptance to the intended use. A failed critical requirement cannot be averaged away. A valid control should pass within its demonstrated limits; do not demand impossible certainty. Missing evidence may justify a restricted or provisional decision, not an invented defect.

A correction or new source version needs the affected checks rerun; retain the previous result. Retrieval failure is not evidence that a record was withdrawn. Stop when the assigned decision is supported or the missing decisive evidence is named.

## Examples and coaching

Read [the worked example](references/example.md) when an example helps. For requested practice, present [the exercise](references/practice.md), let the user attempt it and give specific feedback. Do not require an exercise response or timing to finish an ordinary validation task.


## Optional helper runtime

The included helper uses Python 3 and its standard library. Resolve its scripts/ path relative to this SKILL.md, rather than the agent workspace. The helper is optional for the reasoning workflow. If execution is unavailable, state that limitation instead of claiming it ran.

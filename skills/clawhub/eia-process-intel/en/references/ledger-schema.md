# Ledger Schema (minimal ontology v0.1, 2026-09-09)

Schema evolution rules at the bottom. Changes happen only in this document — never improvise entities mid-engagement.

## Entities (8)

Company / Project (EIA project) / Product / ProcessStep / Equipment (list item) / EquipmentClass (vocabulary layer) / Material / Pollutant

## Relations (8)

| Relation | Subject → Object | Qualifiers (q) |
|----------|------------------|----------------|
| owns | Company → Project | nature of construction, approval number |
| includes_step | Project → ProcessStep | index, pollution-generating flag |
| uses_equipment | ProcessStep → Equipment | count, source (purchased / leased / reused) |
| classified_as | Equipment → EquipmentClass | model, generation signal |
| consumes | ProcessStep → Material | annual usage, unit |
| produces | ProcessStep → Product | capacity, unit |
| emits | ProcessStep → Pollutant | generated / emitted amount, discharge destination |
| gaming_trace | Company → Project | trace type, evidence description |

Rejected entity candidates (do not reintroduce without the process): process route (a derived view — let data accumulate first), equipment vendor (currently an attribute; materialize only after a real "find all downstream users of vendor X" query fails), treatment facility (weak for investment judgment).

## Fact attributes (mandatory on every entry)

- `source`: `{file, page, quote}` — filename, page, verbatim quote
- `game_risk`: high / med-high / medium / med-low / low (defaults from field-credibility.md)
- `status`: declared / cross-validated / conflicts-with-external
- `disc_date`: disclosure date; `added`: booking date

## JSONL format

```json
{"s":"X-Detek (fictional)","p":"owns","o":"T2SL detector line project (fictional)","q":{"construction":"new build"},"source":{"file":"x-detek-eia-20XX.pdf (fictional)","page":12,"quote":"..."},"game_risk":"low","status":"declared","disc_date":"20XX-06","added":"2026-09-09"}
```

## Equipment-class vocabulary

Synchronized with the "equipment class" column of every file under references/mappings/. New classes appear in a mapping file first, then the ledger follows; alias normalization (e.g., "vacuum coater" → PVD) is recorded in the mapping file's rationale column.

## Storage location

DD project workspace at `{project dir}/eia-ledger/<track>.jsonl`; failed queries go into `failed-queries.md` in the same directory (format: date / question verbatim / gap type: missing entity / missing relation / missing attribute / mapping missing). No business data in this skill directory.

## Growth mechanism (schema change rules)

1. Append triples at the end of every engagement
2. Questions the ontology cannot answer → write into failed-queries.md; never fabricate entities on the spot
3. Adding an entity / relation / attribute requires citing at least one failed-queries record; after changing, note the version and date at the top of this document

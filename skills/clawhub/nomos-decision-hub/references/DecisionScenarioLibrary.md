# Decision Scenario Library (P1 upgrade, v2.0)

Pre-built decision scenarios to lower the entry barrier. Each scenario defines the
inputs, the five-operator chain, and the acceptance criteria. Copy the JSON,
replace the content, run the hub.

## Scenario 1 — Compliance gate (regulatory approval)

| Field | Value |
|---|---|
| Question | Should we release this feature under current policy? |
| Inputs | feature spec, policy text, risk register |
| Operators | narrative-strip → assumption-probe → fragility-hedge → responsibility-anchor → causal-reconstruction |
| Fragility focus | unstated policy exemptions, missing data paths |
| Acceptance | sealed report with ≥2 stress scenarios; verdict explicit; no `medium` confidence without evidence |
| Output | sealed report (see `SealedReportSpec.md`) |

## Scenario 2 — Strategic bet (market entry)

| Field | Value |
|---|---|
| Question | Enter market X with product Y? |
| Inputs | market data, competitor map, capability matrix, cost model |
| Operators | same chain; fragility-hedge focuses on demand assumptions and switching costs |
| Acceptance | counterfactual re-selection over ≥3 alternative decisions; sealed report with scenario coverage table |
| Output | sealed report + decision log |

## Scenario 3 — Root-cause trace (incident)

| Field | Value |
|---|---|
| Question | What caused the outage / drift / failure? |
| Inputs | event timeline, logs, config diffs |
| Operators | narrative-strip → causal-reconstruction (root-cause chain) → responsibility-anchor |
| Fragility focus | correlation masquerading as causation |
| Acceptance | causal chain with each link evidenced; no probabilistic language; sealed |
| Output | sealed report |

## Scenario 4 — Resource allocation (constrained budget)

| Field | Value |
|---|---|
| Question | How to allocate a fixed budget across N programs? |
| Inputs | program objectives, cost/benefit estimates, constraint set |
| Operators | chain + weighted-utility resolution (aligned with MotiveConflictRules semantics) |
| Acceptance | allocation table + sensitivity on top-2 uncertain inputs |
| Output | sealed report + allocation table |

## Usage rule

1. Pick the closest scenario template.
2. Replace content placeholders with real inputs.
3. Run the hub; the five operators stay fixed (they are the deterministic core).
4. Every run ends with a sealed report; archive it append-only.

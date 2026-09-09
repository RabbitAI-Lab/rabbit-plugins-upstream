# Cross-Validation Recipes

Principle: use cheap truths (low-risk trust anchors) to test expensive lies (high-risk declared figures). Back-calculated outputs are always ranges with an explicit caliber note and the sensitive parameters named.

## Trust anchors (low-risk fields)

Equipment counts, building floor area, outfall locations, treatment facility sizes — site-checkable and cross-referenced by later filings (discharge permit, completion acceptance). Use these as the base for back-calculating high-risk fields.

## Capacity back-calculation

- **Equipment cycle-time method**: Σ(per-unit hourly output × unit count × annual effective hours) vs. declared capacity. Industry cycle times come from prior engagements on the same track or public line cases — cite the source; mark 【to verify】 when none exists
- **Material method**: key raw material input ÷ industry unit consumption vs. declared capacity
- **Energy method**: annual electricity / water usage ÷ industry per-unit energy / water consumption
- **External checks**: capacity stated on the discharge permit, actual output in execution reports, capacity in prospectus / announcements

Output format: `capacity estimate range [low, high], caliber: estimated under EIA-caliber self-consistency, sensitive parameter: X`. If equipment density is anomalous (units × cycle time << declared capacity), both hypotheses — poor yield and inflated capacity — must be stated.

## Yield / unit-consumption back-calculation (material-balance method)

Key inputs (substrates / targets / gases) vs. outputs (chip / device count) → end-to-end yield range; the per-step material-loss distribution locates the bottleneck step.

The footnote must state: this is an estimate under EIA-caliber self-consistency, not the true yield; understated materials shift the range, and external materials narrow it.

## Emission back-calculation

- Treatment facility design throughput ÷ design removal rate → inlet concentration and source strength vs. declared values
- Peer per-unit emission coefficients (industry-specific permit technical specifications) × capacity
- Execution-report actuals vs. EIA projections: persistently far below projection → understatement or real production curtailment; state both explanations

## Product-mix inference

Hazardous-waste types + waste-liquid composition + by-products: the process origins implied by hazardous-waste codes expose undeclared real product lines. Example: indium-bearing waste liquid → an indium-based process exists; specialty gas species (silane / phosphine / arsine) are fingerprints of epitaxy and implant steps.

## External data sources (in order of availability)

1. National discharge-permit platform: permit original (capacity / emission limits / treatment facilities) + annual execution reports (actual emissions / output)
2. Hazardous-waste transfer manifests / hazardous-waste operating licenses (disposal volume back-calculates waste generation)
3. Credit China / local environmental penalty announcements
4. Prospectuses / annual reports: construction-in-progress, machinery original value, transfers to fixed assets (cross-check the equipment list)
5. Bidding sites and customs data (leads on imported equipment models)

## status tagging rules

- `declared`: EIA text only, nothing verified
- `cross-validated`: at least one independent path (trust anchor or external source) supports it; record the path
- `conflicts-with-external`: contradictory evidence exists — do not change the number; the conflict goes into the report and the gaming-trace list

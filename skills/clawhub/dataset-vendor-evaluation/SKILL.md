---
name: dataset-vendor-evaluation
description: Evaluate a data vendor or candidate dataset against a customer need, existing holdings, quality, access conditions and ongoing cost. Recommend acquire, pilot, defer or reject based on incremental usable value rather than advertised size.
license: MIT-0
---

# Vendor and dataset evaluation

Make the investment decision useful: which customer question this source can answer better, with what evidence, cost and remaining uncertainty.

## Define the comparison

State the customer action, target entities/relationships, geography, time window, essential fields and required freshness. Inspect available internal baseline information. If the baseline is unavailable, assess the source but do not claim it adds new coverage.

Obtain the source's actual composition, sampling/collection method, observation dates, updates, identifiers, formats and documented uses. Separate marketing descriptions, downloaded samples and verified repeat deliveries. Public accessibility does not establish permitted product reuse.

## Evaluate the evidence

Inspect sample selection and exclusions. A vendor-picked demonstration is useful for discovery, not a representative population error estimate. Propose a targeted independent or stratified check when it could change the decision.

Reconcile at the required grain:
- Existing entities with no useful additional information.
- Existing entities with supported useful enrichment.
- Confirmed new eligible entities or relationships.
- Out-of-scope, stale or unusable records.
- Identity or fact cases that remain unresolved.

Count unique eligible entities and fields, not copies, formats or URLs. Do not treat a vendor-local record ID as a proven new provider. A duplicate may still reveal a separate relationship; confirm grain before excluding it.

Evaluate correctness, completeness, matchability, target-population coverage and freshness separately. Use authority appropriate to the field. Document unknown truth labels rather than quietly accepting or rejecting them.

Check the permitted use, redistribution/derived-data restrictions, retention, delivery, API/update access, price basis and integration/maintenance effort that matter to this use. Read supplied terms and name unresolved questions; do not invent legal rights, contract guarantees or pricing.

## Recommend proportionately

Compare available alternatives, including existing sources or a bounded pilot. Explain incremental useful coverage and enrichment supported by evidence, downstream use and the main cost/quality tradeoff.

Recommend acquire, pilot, defer or reject, with the reason and evidence that would change it. A pilot needs the decisive question, actual data/cohort, acceptance tied to customer use and a stopping point. Use QuickTicket principles when a plan is requested, without adding a tracker or compulsory review workflow.

Estimate return only with supported assumptions about usage, outcomes, cost and time. Otherwise state measurable leading value, such as verified additional target contacts, and leave financial return unknown. Do not multiply independent-looking quality rates or extrapolate a curated sample without justified assumptions.

Return a short recommendation and comparison table, with evidence and uncertainties available. Do not buy data, contact a vendor or start recurring collection merely because a recommendation favors acquisition.

See [worked example](references/example.md) or [practice](references/practice.md) when useful.


## Description:

Compare competing retail assortments through Crawlora catalogs. Use to find observed gaps in categories, brands, product attributes, variants, and price bands, with explicit catalog coverage and product-matching evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External retail analysts, category managers, and developers use this skill to collect comparable catalog samples from supported retailers and identify evidence-backed assortment gaps across categories, brands, attributes, variants, and price bands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Catalog queries, store URLs, product identifiers, request bodies, and the Crawlora API key are sent to Crawlora and may consume credits.

Mitigation: Confirm the user's scope and credit budget before collection, keep the API key in the environment, and avoid confidential business data in request parameters unless the user accepts sharing it with Crawlora.

Risk: Partial coverage, failed requests, endpoint caps, or request budgets can be mistaken for confirmed assortment absence.

Mitigation: Record pages, offsets, filters, declared totals, unique IDs, stopping reason, retrieval timestamps, and whether each gap is observed sample absence, confirmed absence, out-of-stock, unknown coverage, or taxonomy mismatch.

Risk: Single catalog snapshots can be misrepresented as trends or demand signals.

Mitigation: Require comparable saved snapshots with the same collection scope for trend claims, and state what additional evidence would validate demand or profitability.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/retail-assortment-gap-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and structured analysis outputs such as coverage ledgers, assortment matrices, and prioritized gap lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include source URLs or IDs, collection time, confidence, coverage limits, and validation notes for each proposed gap.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

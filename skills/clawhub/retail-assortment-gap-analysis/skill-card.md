## Description:

Compare competing retail assortments through Crawlora catalogs. Use to find observed gaps in categories, brands, product attributes, variants, and price bands, with explicit catalog coverage and product-matching evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Retail, ecommerce, and merchandising teams use this skill to compare public storefront catalogs and identify evidence-backed assortment gaps across categories, brands, product attributes, variants, and price bands. It helps separate observed sample gaps from confirmed catalog absence, out-of-stock cases, unknown coverage, and taxonomy mismatches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Store URLs, category or product queries, and related catalog research inputs are sent to Crawlora with the user's API key.

Mitigation: Keep the API key in the environment, avoid secrets or unauthorized private business data in queries, and set request and credit limits before large collections.

Risk: Partial endpoint coverage or capped pagination can be mistaken for confirmed product absence.

Mitigation: Record pages, offsets, filters, declared totals, stopping reasons, and timestamps, and label incomplete coverage as observed sample gaps.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with a coverage ledger, comparable assortment matrix, prioritized gap list, and supporting shell commands when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses scoped Crawlora GET requests and should preserve source IDs, pagination progress, retrieval timestamps, and confidence labels.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Compare competing retail assortments through Crawlora catalogs to find observed gaps in categories, brands, product attributes, variants, and price bands, with explicit catalog coverage and product-matching evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Retail analysts, category managers, and agents use this skill to collect comparable catalog evidence from Shopify, Target, and IKEA, then identify observed assortment gaps with coverage, matching, and confidence notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to an environment-selected API base.

Mitigation: Before running the helper, unset CRAWLORA_API_BASE or verify it points only to https://api.crawlora.net/api/v1.

Risk: Catalog requests may send sensitive private business data to Crawlora.

Mitigation: Avoid passing sensitive private business data unless the user intends to share it with Crawlora.

Risk: Partial fetches, request budgets, endpoint caps, or failed requests can make observed gaps look like confirmed catalog absence.

Mitigation: Report coverage scope, pagination limits, failures, and confidence, and label incomplete coverage as observed sample gaps.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with a coverage ledger, comparable assortment matrix, prioritized gap list, and optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Crawlora API results and should report collection scope, pagination, timestamps, source IDs, confidence, and whether gaps reflect absence, out-of-stock status, unknown coverage, or taxonomy mismatch.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

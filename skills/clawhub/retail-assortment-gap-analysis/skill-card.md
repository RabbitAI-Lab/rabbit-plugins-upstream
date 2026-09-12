## Description:

Compare competing retail assortments through Crawlora catalogs to find observed gaps in categories, brands, product attributes, variants, and price bands, with explicit catalog coverage and product-matching evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Retail analysts, category managers, and developers use this skill to collect scoped public catalog data from Shopify, Target, and IKEA through Crawlora and compare assortments. It helps produce evidence-backed coverage ledgers, comparable assortment matrices, and prioritized gap lists without treating partial samples as confirmed absence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora API key exposure during catalog collection.

Mitigation: Keep CRAWLORA_API_KEY private, pass it through the environment, and rely on the bundled helper's fixed Crawlora API base and private curl config handling.

Risk: Over-collection or unnecessary disclosure of confidential assortment details.

Mitigation: Bound collection to the stores, categories, markets, and credit budget needed for the analysis; avoid sending confidential assortment details unless necessary.

Risk: Partial or failed fetches may be misread as empty catalogs or confirmed market gaps.

Mitigation: Record pages, offsets, filters, totals, stopping reasons, and retrieval timestamps; label incomplete coverage as observed sample gaps and do not treat failed requests as empty markets.

Risk: Catalog comparisons can be misleading when products, variants, currencies, taxes, or package sizes are normalized inconsistently.

Mitigation: Fix store, country, language, currency, retrieval window, price basis, and counting unit before comparison, and preserve unknown values instead of forcing matches.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/retail-assortment-gap-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with tables, source IDs, URLs, confidence notes, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a coverage ledger, comparable assortment matrix, and prioritized gap list with collection scope, timestamps, denominators, and validation needs.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

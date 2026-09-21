## Description:

Compare competing retail assortments through Crawlora catalogs to find observed gaps in categories, brands, product attributes, variants, and price bands with explicit catalog coverage and product-matching evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Retail analysts, category managers, and agents assisting retail teams use this skill to collect scoped catalog data from Shopify, Target, and IKEA through Crawlora and compare assortments. It helps produce evidence-backed coverage ledgers, assortment matrices, and prioritized gap lists while distinguishing partial samples from complete catalog evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party catalog service and requires a Crawlora API key.

Mitigation: Use it only when Crawlora is an acceptable service provider, keep CRAWLORA_API_KEY private, and avoid sharing logs or raw command output that could expose the key.

Risk: Unbounded or overly broad collection can exceed the intended credit budget or scope.

Mitigation: Limit requests to the agreed stores, categories, markets, and budget, and preserve pagination progress and retrieval timestamps for repeatable collection.

Risk: Partial samples, endpoint caps, or taxonomy mismatches can be mistaken for confirmed assortment gaps.

Mitigation: Label incomplete coverage as observed sample gaps, keep explicit denominators and unknown buckets, and report whether evidence supports absence, out-of-stock status, unknown coverage, or taxonomy mismatch.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/retail-assortment-gap-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown analysis with optional shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a coverage ledger, comparable assortment matrix, prioritized gap list, source URLs or IDs, collection timestamps, confidence, and validation needs.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

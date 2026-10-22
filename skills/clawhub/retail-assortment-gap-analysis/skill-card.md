## Description:

Compares competing retail assortments using Crawlora catalogs to identify evidence-backed gaps in categories, brands, attributes, variants, and price bands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Retail analysts and merchandising teams compare public competitor catalogs with their assortment to identify and prioritize observed product gaps while documenting coverage and matching confidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Crawlora API key and network access are required.

Mitigation: Keep the key in the environment and grant network access only if use of Crawlora is acceptable.

Risk: Assortment queries can disclose private assortment data to Crawlora.

Mitigation: Exclude private assortment details from API queries unless sharing them with Crawlora is intended.

Risk: Repeated catalog collection can consume API credits.

Mitigation: Set a request budget and monitor credit usage.

Risk: Incomplete catalog coverage may make observed gaps look like confirmed absences.

Mitigation: Report coverage, collection time, and matching confidence; distinguish sampled gaps from fully enumerated absences.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/retail-assortment-gap-analysis)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown coverage ledger, assortment matrix, and prioritized gap list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source URLs or IDs, retrieval times, product and variant counts, price basis, coverage, and confidence.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

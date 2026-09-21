## Description:

Research luxury-fashion and watch resale listings, sold evidence, condition, and seller signals across specialist marketplaces. Use for sourcing or evidence comparison, not buying or appraisal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare public luxury resale asks, sold evidence where exposed, condition text, and seller or dealer signals across specialist marketplaces. It supports sourcing and evidence comparison, not buying, authentication, or appraisal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Crawlora as a third-party service for public luxury marketplace research and requires a Crawlora API key.

Mitigation: Provide the API key through CRAWLORA_API_KEY and do not paste secrets or private/internal URLs into queries.

Risk: Retail catalog, editorial, store-locator, current inventory, recommendation, and seller reputation outputs can be mistaken for transaction or authenticity evidence.

Mitigation: Treat those outputs as background context; keep active asks, sold evidence, and market context separate, and state evidence gaps plainly.

Risk: Marketplace condition labels and authentication signals are source-stated and not independently verified by the skill.

Mitigation: Report condition and authentication signals as source-stated only and avoid authentication, appraisal, purchase, fee, duty, shipping, or currency-conversion claims unless the source provides them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/luxury-resale-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables or JSON-like lists with source URLs, prices, currencies, condition text, seller signals, timestamps, and evidence-gap notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public-data research; unsupported fields should be null or labeled not provided.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

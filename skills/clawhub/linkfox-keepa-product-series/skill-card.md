## Description:

Queries historical Amazon product time-series data for a single ASIN, including price, BSR, rating, seller-count, and monthly sales trends across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce operators use this skill to retrieve and summarize Keepa-powered historical data for Amazon ASINs. It supports price-history checks, BSR tracking, seller-count review, rating trends, and fulfillment-price comparisons for product research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle account login, API keys, billing, payment links, feedback reports, and stored product-history data.

Mitigation: Install only if you trust LinkFox, configure credentials yourself where possible, and avoid providing phone or payment details through an agent unless you intend to use those flows.

Risk: Product-history responses are persisted in a workspace linkfox directory.

Mitigation: Review the saved output directory for sensitive product-research data and remove files that should not remain in the workspace.

Risk: Queries consume credits and dynamic Keepa token costs may be high.

Mitigation: Confirm user intent before additional paid queries and reuse the documented 24-hour cache for repeated parameter sets.

## Reference(s):

- [Keepa API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-series)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under a workspace linkfox directory, summarizes large responses, and uses a 24-hour local cache for repeated parameter sets.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

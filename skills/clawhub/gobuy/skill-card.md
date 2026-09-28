## Description:

GoBuy helps shopping agents assess marketplace product evidence, compare listings, find stronger-evidenced alternatives, and check independent store trust and agent readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping agents and their users can check evidence behind Amazon, Walmart, and Target listings, compare products, and assess independent stores before deciding what to buy or where to buy it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product identifiers, retailer names, and store URLs may be sent to GoBuy services.

Mitigation: Disclose external lookups and avoid submitting sensitive or private URLs.

Risk: An evidence score may be mistaken for a product-quality or safety recommendation.

Mitigation: Present the score with its verdict and computed date, and describe alternatives as stronger-evidenced rather than recommended.

Risk: Unindexed products or unavailable store scores may leave evidence gaps.

Mitigation: State when a product is not indexed or a store has not been scored; do not invent a verdict or alternatives.

## Reference(s):

- [GoBuy skill release](https://clawhub.ai/digitalmentes7-maker/skills/gobuy)
- [Product evidence reports](https://audit.gobuy.ai)
- [Storefront audit](https://agentic.gobuy.ai)
- [Store scoring API](https://stores.gobuy.ai/api/scan)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence Scores (0–100), verdicts, observed and missing signals, score dates, evidence-ranked alternatives, and store scores when available.]

## Skill Version(s):

1.1.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

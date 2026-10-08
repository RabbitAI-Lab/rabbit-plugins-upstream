## Description:

Helps shopping agents assess product listings, compare evidence, examine review integrity, and check storefront trust before advising on purchases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping agents and their users use this skill to review marketplace listing evidence, compare products, assess suspicious reviews, and check independent stores before purchase decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or store identifiers are sent to GoBuy services, including for broad shopping questions.

Mitigation: Use the service only when the user is comfortable with external trust checks; avoid sending unnecessary identifying details.

Risk: Evidence and review scores could be mistaken for proof of product quality, safety, or review authenticity.

Mitigation: Present scores as evidence-quality indicators with their verdict and date, and describe review flags as heuristic findings rather than proof.

## Reference(s):

- [GoBuy skill release](https://clawhub.ai/digitalmentes7-maker/skills/gobuy)
- [GPV-1 Pre-Purchase Verification Specification](https://docs.gobuy.ai/standard)
- [GPV-1 machine-readable ruleset](https://docs.gobuy.ai/standard/v1.json)
- [The Verification Gap](https://docs.gobuy.ai/verification-gap)
- [Checkout WebMCP integration pattern](https://docs.gobuy.ai/webmcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence scores and verdicts include freshness and missing signals when available; review-integrity findings are heuristic.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

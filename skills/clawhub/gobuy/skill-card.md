## Description:

Helps shopping agents assess marketplace listings, review integrity, and storefront evidence before advising on purchases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping agents and their users can check product evidence, compare listings, assess suspicious reviews, and evaluate storefront signals before making purchase decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product identifiers and store URLs may be sent to GoBuy services.

Mitigation: Disclose the external checks and avoid submitting sensitive or private URLs.

Risk: Evidence and review-integrity scores may be mistaken for proof of quality, safety, or fraudulent reviews.

Mitigation: Present scores as limited evidence signals, include verdicts and dates, and avoid definitive claims about products or reviews.

## Reference(s):

- [GoBuy skill release](https://clawhub.ai/digitalmentes7-maker/skills/gobuy)
- [GoBuy product evidence reports](https://audit.gobuy.ai)
- [GoBuy storefront audit](https://agentic.gobuy.ai)
- [The Verification Gap](https://docs.gobuy.ai/verification-gap)
- [Verify-then-checkout integration pattern](https://docs.gobuy.ai/webmcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include evidence scores, verdicts, review-integrity signals, and score dates.]

## Skill Version(s):

1.1.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

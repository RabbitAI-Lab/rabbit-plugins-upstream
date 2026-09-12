## Description:

Screen startups listed for sale using Crawlora's TrustMRR marketplace, stored company records, and daily metric history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and acquisition researchers use this skill to screen startup acquisition candidates, compare asking prices and dated revenue metrics, inspect marketplace and product evidence, and produce diligence questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Startup search criteria, target URLs, and related research queries are sent to Crawlora under the user's API key.

Mitigation: Use a Crawlora-scoped API key and avoid sending sensitive private deal materials in scrape or search requests.

Risk: TrustMRR revenue data and payment-provider verification may be mistaken for audited financial proof.

Mitigation: Treat revenue metrics as diligence inputs and separately verify profit, refunds, retention, transferability, and seller claims.

Risk: Asking prices, deal scores, sponsored placement, and growth metrics may be overinterpreted as valuation or investment advice.

Mitigation: Label calculations explicitly, preserve dates and definitions, and present open diligence questions instead of making investment recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/startup-acquisition-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora](https://crawlora.net)
- [TrustMRR FAQ](https://trustmrr.com/faq)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with candidate tables, source links, dated metrics, calculations, discrepancies, and diligence questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Crawlora API request examples and explicitly labeled calculations for acquisition screening.]

## Skill Version(s):

1.0.7 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

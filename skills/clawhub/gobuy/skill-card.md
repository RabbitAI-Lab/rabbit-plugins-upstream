## Description:

Helps shopping agents check marketplace product evidence, compare listings, assess review signals, and evaluate independent storefronts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping agents and their users use GoBuy to assess evidence behind product listings and reviews, compare stronger-evidenced alternatives, and check storefront trust signals before making purchasing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or store evidence signals may be mistaken for proof of product quality, safety, or legitimacy.

Mitigation: Describe scores as evidence signals, include the verdict and date, and do not treat review heuristics as proof.

Risk: Product IDs or store domains may be sent to GoBuy services during requested checks.

Mitigation: Disclose this data sharing and send only the identifiers or domains needed for the requested check.

## Reference(s):

- [GoBuy ClawHub skill listing](https://clawhub.ai/digitalmentes7-maker/skills/gobuy)
- [GoBuy product evidence report](https://audit.gobuy.ai)
- [GoBuy storefront audit](https://agentic.gobuy.ai)
- [The Verification Gap](https://docs.gobuy.ai/verification-gap)
- [Checkout WebMCP integration pattern](https://docs.gobuy.ai/webmcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries of product and store evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scores, verdicts, observed or missing signals, score dates, and heuristic review findings.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

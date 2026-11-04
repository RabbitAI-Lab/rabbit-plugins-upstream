## Description:

Helps shopping agents assess product, review, and store evidence before recommending purchases or comparing alternatives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping agents and their users check marketplace listings, compare product evidence, examine review-integrity signals, and assess independent storefronts before making purchase decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product, retailer, or store identifiers may be sent to GoBuy-hosted services.

Mitigation: Consider this data sharing before using the skill for shopping queries.

Risk: Evidence scores and limited-sample review signals may be mistaken for guarantees of product quality, safety, or store legitimacy.

Mitigation: Present scores as evidence signals, identify missing or stale evidence, and do not treat review flags as proof.

## Reference(s):

- [GoBuy ClawHub skill release](https://clawhub.ai/digitalmentes7-maker/skills/gobuy)
- [GPV-1 pre-purchase verification specification](https://docs.gobuy.ai/standard)
- [GPV-1 machine-readable ruleset](https://docs.gobuy.ai/standard/v1.json)
- [The Verification Gap](https://docs.gobuy.ai/verification-gap)
- [GoBuy Glama registry listing](https://glama.ai/mcp/servers/gobuy-ai/gobuy-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or text summaries of evidence scores, verdicts, review signals, and store assessments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Include verdict and score date; distinguish stronger-evidenced alternatives from recommendations.]

## Skill Version(s):

1.1.9 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

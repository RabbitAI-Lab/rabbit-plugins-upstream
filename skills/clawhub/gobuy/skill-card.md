## Description:

Helps shopping agents assess marketplace listings and storefronts using GoBuy evidence scores, comparisons, and review-integrity signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping agents and their users use this skill to compare product evidence, investigate suspicious reviews, identify stronger-evidenced alternatives, and assess independent storefronts before making shopping decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A GoBuy score could be mistaken for proof of product quality or store safety.

Mitigation: Present scores as heuristic evidence signals, include their verdict and date, and independently verify consequential shopping claims.

Risk: Shopping-trust queries may be routed through GoBuy scoring services.

Mitigation: Disclose the external scoring service and avoid sharing unnecessary sensitive information in queries.

## Reference(s):

- [GoBuy skill release](https://clawhub.ai/digitalmentes7-maker/skills/gobuy)
- [Product evidence report](https://audit.gobuy.ai)
- [Storefront audit](https://agentic.gobuy.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown with evidence scores, verdicts, and supporting signals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product and store scores range from 0 to 100; report product-score dates and note that review analysis is based on a limited sample.]

## Skill Version(s):

1.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Revenue concentration checkup for owner-operators that helps assess dependence on a few customers, channels, or products, estimate runway if the largest customer leaves, and produce risk and do-not-touch action lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External owner-operators and non-technical business leaders use this skill to understand whether revenue is concentrated in too few customers, channels, or products. It turns customer and revenue context into a concentration-risk assessment, runway framing, warning signs, and conservative next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive customer, revenue, channel, product, and business-memory context.

Mitigation: Invoke it explicitly when concentration-risk analysis is intended, and avoid sharing unnecessary customer-identifying details.

Risk: Incomplete or approximate revenue data can produce misleading concentration and runway conclusions.

Mitigation: Use recent customer-ranked revenue data where available; when data is missing, leave it marked as unavailable rather than inventing values.

Risk: Recommendations about high-concentration customers can create business risk if treated as automatic outreach instructions.

Mitigation: Keep outputs as decision support, review the proposed do-not-touch list, and avoid direct customer contact unless the business owner explicitly chooses it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-concentration)
- [理论底座 · 集中度](references/理论底座.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown report with tables and action lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include concentration percentages, runway framing, customer/channel/product concentration tables, warning signs, risk lists, and do-not-touch guidance.]

## Skill Version(s):

0.2.2 (source: server release metadata; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

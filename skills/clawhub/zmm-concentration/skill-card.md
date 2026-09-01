## Description:

Revenue concentration checkup for owner-operators that estimates how much revenue depends on a few customers, channels, or products, then produces runway estimates, risk findings, and a do-not-touch action list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External 2B owner-operators and business leads use this skill to assess revenue concentration across customers, channels, and products. It helps estimate runway if the largest customer leaves and turns the analysis into risk, prohibited-action, and next-step guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive revenue and customer-risk information.

Mitigation: Use anonymized customer labels where possible and avoid entering unnecessary customer-identifying details.

Risk: The skill can store summary calibration notes in configured memory.

Mitigation: Review memory settings before use and disable or clear retained notes when business details should not persist.

## Reference(s):

- [理论底座 · 集中度](references/理论底座.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown report with tables and action lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include anonymized customer labels, concentration ratios, runway estimates, risk findings, a do-not-touch list, and numbered next-step options.]

## Skill Version(s):

0.2.1 (source: server release metadata; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

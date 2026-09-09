## Description:

詹明明·该投哪条线 helps operators running multiple business or product lines compare revenue, bottleneck-resource use, marginal return, and exit triggers to decide where to invest, maintain, shrink, or cut.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External business operators, founders, and small-team owners use this skill to assess several live business or product lines together, identify the binding resource, and produce a constrained allocation plan with add, maintain, shrink, or cut decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive business metrics, portfolio decisions, pseudonyms, and follow-up results.

Mitigation: Confirm memory paths before use, apply the skill's pseudonym mode when available, and avoid exposing absolute amounts or identifying business details in shared outputs.

Risk: Portfolio recommendations can be misleading when based on incomplete self-reported revenue, bottleneck-resource, or cash-flow data.

Mitigation: Present data sources and limitations first, mark missing values instead of guessing, and require user confirmation before treating recommendations as decisions.

Risk: Advice about shrinking or cutting a business line can have material operational consequences.

Mitigation: Keep outputs advisory, require explicit resource accounting and exit triggers, and do not execute operational changes on the user's behalf.

## Reference(s):

- [理论底座](artifact/references/理论底座.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-portfolio)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with decision tables, bottleneck-resource accounting, and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include portfolio tables, source and limitation notes, pre-commitment triggers, and follow-up options.]

## Skill Version(s):

0.2.5 (source: server release evidence; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Audits an existing product surface against its design evidence and prepares implementation plans for verified UI improvements without changing product code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qikairo7](https://clawhub.ai/user/qikairo7)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design teams use this skill to audit a product interface against its current design rules and prepare evidence-backed plans for selected improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unsupported UI finding could lead to an inappropriate product change.

Mitigation: Require cited design and runtime evidence, review each proposed correction, and have another agent implement only approved plans.

Risk: Repository inspection and plan writing could exceed the intended read-only scope.

Mitigation: Limit writes to design-plans/ and do not modify product code or run install, format, or commit actions.

## Reference(s):

- [Improve UI on ClawHub](https://clawhub.ai/qikairo7/skills/improve-ui)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Files]

**Output Format:** [Markdown audit findings and, when requested, design plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans are written under design-plans/; product source remains unchanged.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

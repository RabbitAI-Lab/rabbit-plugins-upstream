## Description:

Guides agents through evidence-based premise checks, configuration audits, and reviews of plans that have gone off course.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and teams use this skill before starting a project to test consequential assumptions against evidence, review configuration drift and conflicts, and trace the first point where a plan diverged from expectations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic trigger words may activate the skill when its checklist is not relevant.

Mitigation: Confirm the user wants premise validation or a configuration audit before applying the checklist.

Risk: Non-Chinese users may receive responses in an unintended language.

Mitigation: Ask for, or state, the preferred response language when using the skill.

Risk: Configuration findings may contain sensitive credentials.

Mitigation: Report only the location and recommended remediation; do not repeat credential values.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/premise-and-config-audit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration recommendations]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-linked premise checks and audit findings; report locations of exposed secrets without repeating their values.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; bundled SKILL.md says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

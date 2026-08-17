## Description:

meta-cloudbase guides agents through CloudBase full-stack development and deployment workflows with scenario routing, dependency checks, self-verification, and reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to plan, implement, and deploy Tencent CloudBase web, mini-program, mobile, Cloud Functions, CloudRun, database, authentication, and AI Agent work while checking the correct source-skill route and required CloudBase setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live CloudBase deployment, database, and authentication changes without enough scoping or safety controls.

Mitigation: Review plans before execution, use explicit user-approved targets, prefer staging first, and confirm before deployment, database, or authentication changes.

Risk: The learner can store operational notes and preferences in learned_patterns.json.

Mitigation: Do not store secrets, credentials, or sensitive user notes in learned_patterns.json.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-cloudbase)
- [Distillation report](artifact/distillation_report.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update learned_patterns.json when its learner script is invoked.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

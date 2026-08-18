## Description:

Project Lifecycle Navigator helps agents route software and AI projects through evidence-based intake, scope realignment, read-only health review, latest-delivery alignment, and Owner-led target rebaseline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and project owners use this skill to clarify project goals, control MVP scope, audit existing repositories read-only, compare recent deliveries against current targets, and prepare bounded handoffs for an engineer or coding agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning or audit recommendations could be mistaken for authorization, implementation, or acceptance.

Mitigation: Keep Owner decisions, facts, inferences, verification status, and acceptance boundaries explicit; do not mark work accepted or change governance state.

Risk: Suggested commands or handoffs could cause unintended changes if executed without review.

Mitigation: Review generated handoffs and commands before using another agent or engineer to execute them.

Risk: Project review may expose sensitive project files or prompt the user for secrets.

Mitigation: Operate read-only, avoid requesting secret values, and use environment-variable names with secure provisioning steps instead.

## Reference(s):

- [Project Lifecycle Navigator Skill Page](https://clawhub.ai/englandtong/skills/project-lifecycle-navigator)
- [Skill Definition](artifact/SKILL.md)
- [Usage Examples](artifact/examples/usage-examples.md)
- [New Project Intake Prompt](artifact/prompts/en/01-new-project-intake.en.md)
- [Mid-Project Realignment Prompt](artifact/prompts/en/02-midproject-realignment.en.md)
- [Repository-Wide Health Review Prompt](artifact/prompts/en/03-code-review-upgrade.en.md)
- [Latest Delivery Alignment Review Prompt](artifact/prompts/en/04-latest-delivery-alignment.en.md)
- [Owner-Led Target Rebaseline Prompt](artifact/prompts/en/05-target-rebaseline.en.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Structured Markdown reports, decision tables, review findings, verification plans, and copy-ready handoff prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only advisory output; does not request secret values, edit code, change governance state, or claim QA acceptance.]

## Skill Version(s):

2.0.0 (source: server release metadata and skill body)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

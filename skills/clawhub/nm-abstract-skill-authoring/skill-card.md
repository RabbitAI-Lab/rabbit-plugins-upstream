## Description:

Guides creation of Claude Code skills using test-driven development and persuasion principles for new skill development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to create, validate, and refine Claude Code skills with TDD, description optimization, progressive disclosure, anti-rationalization patterns, and deployment checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers could activate the skill during tasks that are not about authoring or validating skills.

Mitigation: Review activation triggers and use the skill only when the task is explicitly about skill creation, validation, or refinement.

Risk: Persuasion and anti-rationalization templates could be misapplied outside transparent, user-aligned safety or correctness requirements.

Mitigation: Use these patterns only to reinforce documented requirements that the user or project has explicitly accepted.

Risk: Deployment and rollback examples can affect existing local skill directories if copied without checking the environment.

Mitigation: Inspect existing ~/.claude/skills directories and adapt file paths before running installation, deployment, or rollback snippets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skill-authoring)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Modular guidance; no hidden automation or exfiltration was identified by the server security evidence.]

## Skill Version(s):

1.9.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

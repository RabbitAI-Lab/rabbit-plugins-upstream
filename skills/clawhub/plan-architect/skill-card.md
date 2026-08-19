## Description:

plan-architect turns design inputs into executable implementation plans with small tasks, TDD steps, YAGNI and DRY checks, plan documents, and validation checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to convert approved designs, feature work, refactors, bug fixes, migrations, or technical-debt items into task-level implementation plans and validation checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect project files, write planning artifacts, and run validation commands.

Mitigation: Use it in a bounded workspace, review planned file writes, and require explicit confirmation before command execution.

Risk: The evidence reports inconsistent statements about API keys and network/API behavior.

Mitigation: Do not provide API keys or permit network/API use unless a specific user-requested workflow clearly requires it.

Risk: Generated implementation plans may include incorrect code snippets, commands, or assumptions.

Mitigation: Review the plan, validation commands, and rollback steps before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/plan-architect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown plans with checklists, inline code snippets, shell commands, validation steps, dependency notes, and rollback guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write planning artifacts such as plan.md and may propose validation commands for the agent or user to run.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

A structured development workflow skill for individual developers that guides planning, implementation, verification, testing, preference memory, and checkpoint-based task tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to structure coding work into request, planning, execution, verification, and delivery stages, with optional preference memory and checkpoints for task tracking. It is aimed at personal development workflows that need explicit planning and validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation gives conflicting claims about command execution, network/API use, and credentials.

Mitigation: Confirm the intended behavior before enabling command execution, network access, credential use, or automation, and run the skill with the least privileges needed.

Risk: Preference memory and checkpoint files can persist project details or personal workflow preferences.

Mitigation: Store only explicitly requested preferences and review or delete local memory and checkpoint files before sharing a workspace.

Risk: Generated development guidance may include code changes or shell commands that affect a project.

Mitigation: Review proposed diffs and commands before applying them, then run the relevant tests or checks before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-dev-v1-tool-free)
- [SkillHub homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code, shell command, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe local preference and checkpoint files for the agent workflow.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

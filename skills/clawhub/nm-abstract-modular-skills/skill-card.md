## Description:

Build composable skill modules with hub-and-spoke loading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to design, refactor, and maintain modular agent skills with predictable token use, shallow dependencies, and progressively loaded guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate more often than necessary because of broad trigger words.

Mitigation: Review whether its guidance is relevant before applying it to a task, especially when a narrower skill is available.

Risk: The packaged markdown skill does not cover any separate Claude Code plugin behavior.

Mitigation: Review any separately installed plugin, agents, hooks, or commands before enabling them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-modular-skills)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [Core workflow module](artifact/modules/core-workflow.md)
- [Implementation patterns module](artifact/modules/implementation-patterns.md)
- [Optimization techniques module](artifact/modules/optimization-techniques.md)
- [Troubleshooting module](artifact/modules/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; no hidden execution, credential access, persistence, or destructive behavior identified by evidence.security.]

## Skill Version(s):

1.9.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Claudify guides agents through creating, improving, and persisting Claude Code automation such as agents, skills, rules, commands, and hooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to convert recurring workflows into Claude Code automation, review automation behavior, and preserve useful session knowledge. It is intended for users building or maintaining agent, skill, rule, command, hook, or plugin workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent agent behavior through automation artifacts such as skills, rules, hooks, commands, and plugins.

Mitigation: Review generated automation before deployment and prefer project-local scope unless the behavior is intentionally reusable across projects.

Risk: The persistence workflow can save session knowledge to memory or RAG destinations with unclear user control.

Mitigation: Require explicit confirmation for memory or RAG storage and avoid saving sensitive or project-specific information outside its intended scope.

Risk: Hook and slash-command templates may execute shell commands or consume dynamic context.

Mitigation: Validate inputs, pin local tools where applicable, and review hook or command templates before copying them into an active agent environment.

## Reference(s):

- [Claudify Skill Page](https://clawhub.ai/drumrobot/skills/claudify)
- [background-polling.md](background-polling.md)
- [improve.md](improve.md)
- [persist.md](persist.md)
- [automation-decision-guide.md](resources/automation-decision-guide.md)
- [agent-templates.md](resources/agent-templates.md)
- [hook-examples.md](resources/hook-examples.md)
- [plugin-creation.md](resources/plugin-creation.md)
- [slash-command-syntax.md](resources/slash-command-syntax.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and file or configuration recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create automation artifacts and may recommend persistent memory or documentation updates.]

## Skill Version(s):

0.10.0 (source: server release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

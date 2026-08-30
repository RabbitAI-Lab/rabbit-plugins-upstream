## Description:

Desktop automation via native OS accessibility trees using the agent-desktop CLI for observing and operating desktop applications, including UI snapshots, clicks, typing, scrolling, screenshots, clipboard actions, notification handling, window management, and session tracing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent builders use this skill to let an AI agent inspect and operate desktop applications through the agent-desktop CLI, especially when a task requires reading native UI state, filling forms, navigating menus, or controlling windows. It is intended for desktop GUI automation where the caller reviews and executes concrete CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to operate desktop applications with sensitive but purpose-matched capabilities such as clicking, typing, screenshots, clipboard access, notification actions, and session tracing.

Mitigation: Install only when desktop operation is intended, review proposed actions before execution, and use headed mode, CDP launch, session screenshots, and trace export only when necessary for the task.

Risk: Screenshots, clipboard reads, notification contents, and trace exports may expose sensitive local information.

Mitigation: Treat those artifacts as sensitive, avoid sharing them unnecessarily, and prefer scoped observation or tracing settings that collect only what the task requires.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lahfir/skills/agent-desktop)
- [Observation Commands](references/commands-observation.md)
- [Interaction Commands](references/commands-interaction.md)
- [System Commands](references/commands-system.md)
- [Common Automation Workflows](references/workflows.md)
- [macOS Platform](references/macos.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that observe UI state or modify desktop applications when executed by an agent.]

## Skill Version(s):

0.1.27 (source: server release metadata; artifact frontmatter lists 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

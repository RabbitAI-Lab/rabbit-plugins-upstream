## Description:

Reliable computer use via native OS accessibility trees for agents that need to observe and operate desktop applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to let an AI agent inspect desktop UI state and perform GUI actions such as clicking, typing, scrolling, launching apps, reading windows, managing notifications, and handling clipboard or session workflows. It is especially relevant for macOS desktop automation tasks that rely on native accessibility trees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control desktop applications through macOS Accessibility and may also capture screenshots when Screen Recording is granted.

Mitigation: Install only from a trusted, pinned version and grant Accessibility or Screen Recording permissions only for tasks that require them.

Risk: Default session tracing may persist local records of desktop automation activity.

Mitigation: Use no-trace mode for sensitive work and clean up completed sessions with the documented session end and session gc workflow.

Risk: Clipboard, CDP, screenshots, and headed physical input can expose or change user data outside the intended application flow.

Mitigation: Use these capabilities only when the task requires them, inspect command dispositions before retrying, and avoid repeating actions after uncertain or unverified delivery.

Risk: Global installation commands and bun --trust can run package-managed code outside the skill artifact.

Mitigation: Prefer a pinned, verified package version and avoid bun --trust unless package scripts have been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lahfir/skills/agent-desktop)
- [Command workflows](artifact/references/workflows.md)
- [Observation commands](artifact/references/commands-observation.md)
- [Interaction commands](artifact/references/commands-interaction.md)
- [System commands](artifact/references/commands-system.md)
- [macOS guidance](artifact/references/macos.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command-output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing instructions for using the agent-desktop CLI safely and interpreting structured JSON envelopes.]

## Skill Version(s):

0.1.30 (source: server release metadata; artifact frontmatter reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

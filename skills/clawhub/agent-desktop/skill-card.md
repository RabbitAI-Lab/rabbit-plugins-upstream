## Description:

Reliable computer use via native OS accessibility trees for AI agents that need to see and operate desktop applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent builders use this skill to let agents inspect desktop UI state and perform controlled GUI automation tasks such as clicking, typing, scrolling, window management, clipboard use, and notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad desktop control through native accessibility features.

Mitigation: Install it only from a trusted source and grant Accessibility or Screen Recording permissions only to the launcher that needs them.

Risk: Screenshots, clipboard reads, notifications, CDP launches, and session traces can expose sensitive local information.

Mitigation: Use the narrowest command scope that fits the task, avoid full-screen captures unless needed, and use no-trace or session cleanup options when local history should not be retained.

Risk: GUI actions can mutate application state or be unsafe to repeat after uncertain delivery.

Mitigation: Follow an observe-act-verify loop, inspect action disposition before retrying, and prefer fresh snapshots after UI changes.

## Reference(s):

- [agent-desktop ClawHub page](https://clawhub.ai/lahfir/skills/agent-desktop)
- [Observation Commands](references/commands-observation.md)
- [Interaction Commands](references/commands-interaction.md)
- [System Commands](references/commands-system.md)
- [Common Automation Workflows](references/workflows.md)
- [macOS Platform](references/macos.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash command examples and JSON output schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return structured JSON envelopes; screenshots and session traces may be produced when requested.]

## Skill Version(s):

0.1.32 (source: server release metadata; artifact frontmatter reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

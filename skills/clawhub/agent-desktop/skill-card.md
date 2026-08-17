## Description:

Desktop automation via native OS accessibility trees using the agent-desktop CLI for observing, interacting with, and automating desktop applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to inspect native desktop UI state and perform GUI actions such as clicking controls, filling forms, navigating menus, taking screenshots, managing windows, using the clipboard, and handling macOS notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to control real desktop applications.

Mitigation: Install and use it only when live desktop control is intended, and review macOS Accessibility permissions before operation.

Risk: Screenshots and clipboard reads can expose sensitive user or application data.

Mitigation: Use screenshots and clipboard commands only when needed, and avoid collecting or exporting sensitive UI state.

Risk: Headed or physical actions can affect the live UI through focus, cursor, keyboard, or notification changes.

Mitigation: Use headed mode only when physical interaction is intended and verify actions with fresh observations.

Risk: Session traces and replay artifacts may retain sensitive desktop state.

Mitigation: Run session cleanup for retained traces and treat screenshot-enabled trace exports like sensitive screenshots.

## Reference(s):

- [agent-desktop Skill Page](https://clawhub.ai/lahfir/skills/agent-desktop)
- [Observation Commands](references/commands-observation.md)
- [Interaction Commands](references/commands-interaction.md)
- [System Commands](references/commands-system.md)
- [Workflows](references/workflows.md)
- [macOS Platform](references/macos.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents toward command-line desktop automation workflows that return structured JSON envelopes from agent-desktop.]

## Skill Version(s):

0.1.24 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Desktop automation via native OS accessibility trees using the agent-desktop CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to observe desktop UI state and perform GUI automation tasks such as filling forms, navigating menus, managing windows, using the clipboard, handling notifications, and verifying interactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad desktop observation and control through the launching terminal.

Mitigation: Install and use it only in environments where that level of desktop automation access is acceptable.

Risk: Screenshots, clipboard operations, notifications, and trace artifacts may expose sensitive information from the desktop.

Mitigation: Avoid sensitive screens unless necessary, prefer app- or window-scoped screenshots, use no-trace for private workflows, and clean up sessions when finished.

Risk: Headed or physical-input commands can move focus, cursor position, or interact with the active desktop.

Mitigation: Use headless semantic commands by default and reserve headed commands for workflows that intentionally need physical input.

## Reference(s):

- [Observation Commands](references/commands-observation.md)
- [Interaction Commands](references/commands-interaction.md)
- [System Commands](references/commands-system.md)
- [Common Automation Workflows](references/workflows.md)
- [macOS Platform](references/macos.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI returns JSON envelopes and can produce screenshots or trace artifacts when requested.]

## Skill Version(s):

0.1.25 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

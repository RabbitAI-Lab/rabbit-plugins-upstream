## Description:

agent-desktop helps AI agents observe and control desktop applications through native OS accessibility trees for tasks such as reading UI state, clicking, typing, scrolling, screenshots, window management, clipboard use, and notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill when an agent needs to inspect and operate desktop GUI applications, including form filling, menu navigation, app and window management, screenshots, clipboard workflows, notifications, and multi-step observe-act automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Desktop automation can control local applications through sensitive operating-system permissions.

Mitigation: Install only if the publisher and package are trusted, and grant Accessibility or Screen Recording permissions only for tasks that need them.

Risk: Screenshots, clipboard content, and trace exports can contain sensitive information.

Mitigation: Use --no-trace or a controlled AGENT_DESKTOP_HOME for sensitive work, and clean up sessions, screenshots, clipboard exports, and trace exports after use.

Risk: Forced commands and risky system shortcuts may interrupt or terminate user work.

Mitigation: Avoid --force unless the user explicitly intends that behavior, and review proposed destructive or system-level actions before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lahfir/skills/agent-desktop)
- [Observation Commands](references/commands-observation.md)
- [Interaction Commands](references/commands-interaction.md)
- [System Commands](references/commands-system.md)
- [Common Automation Workflows](references/workflows.md)
- [macOS Platform](references/macos.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is intended for an agent that invokes the agent-desktop CLI and interprets structured JSON command responses.]

## Skill Version(s):

0.1.26 (source: server release metadata; artifact frontmatter says 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

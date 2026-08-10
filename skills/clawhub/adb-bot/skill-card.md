## Description:

AI-driven Android automation via ADB Bot for screen capture, UI recognition, taps, swipes, text input, app launch, and multi-device control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hilbp](https://clawhub.ai/user/hilbp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to control authorized Android devices through ADB Bot, including inspecting screens, interacting with apps, entering text, and coordinating actions across multiple connected devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Android screens and control connected devices, which may expose private information or perform unintended state-changing actions.

Mitigation: Use it only with devices and apps the user is authorized to control, avoid sensitive screens unless necessary, and confirm high-impact actions before execution.

Risk: Recorded workflows may preserve private data or reusable actions that were not intended for later replay.

Mitigation: Review recorded workflows before reuse or sharing, and remove steps that include private data or unsafe actions.

## Reference(s):

- [ADB Bot website](https://adb-bot.hilbp.com/?utm_source=clawhub&utm_medium=readme)
- [ADB Bot GitHub repository](https://github.com/hilbp/adb-bot)
- [OpenClaw repository](https://github.com/openclaw/openclaw)
- [ClawHub skill page](https://clawhub.ai/hilbp/skills/adb-bot)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide an agent to call ADB Bot MCP tools; the skill itself does not emit standalone files.]

## Skill Version(s):

1.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

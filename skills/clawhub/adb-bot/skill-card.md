## Description:

ADB Bot lets OpenClaw control connected Android devices through a local MCP service for screenshots, UI recognition, taps, swipes, text entry, app launch, workflow recording, and multi-device actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hilbp](https://clawhub.ai/user/hilbp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to let OpenClaw inspect and operate local Android devices through ADB Bot, including screen analysis, UI actions, app control, replayable workflows, and coordinated operation across multiple connected devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control real Android devices, including screenshots, UI-tree inspection, typing, app actions, and multi-device execution.

Mitigation: Use a test device first, avoid sensitive apps during inspection, and require explicit confirmation before messages, purchases, settings changes, or multi-device commands.

Risk: USB or Wi-Fi debugging can leave devices exposed after automation is complete.

Mitigation: Disable or revoke debugging access when finished and keep the ADB Bot service limited to trusted local use.

Risk: Workflow recording and replay may repeat actions or preserve sensitive interaction history.

Mitigation: Review ADB Bot workflow recordings and storage settings before relying on automatic replay.

## Reference(s):

- [ADB Bot website](https://adb-bot.hilbp.com)
- [ADB Bot GitHub releases](https://github.com/hilbp/adb-bot/releases)
- [ADB Bot GitHub repository](https://github.com/hilbp/adb-bot)
- [OpenClaw](https://github.com/openclaw/openclaw)
- [ClawHub skill page](https://clawhub.ai/hilbp/skills/adb-bot)
- [ClawHub publisher profile](https://clawhub.ai/user/hilbp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, Text]

**Output Format:** [Markdown with inline shell commands and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local ADB Bot MCP service and a connected Android device identified by serial number.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

树莓派串口急救 helps agents guide authorized Raspberry Pi UART serial troubleshooting when SSH or networking is unavailable, including wiring safety, permissions, baud issues, boot-log capture, and JishuBuddy handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and device operators use this skill to recover or diagnose Raspberry Pi systems through a safe, permissioned serial-console workflow when network access or SSH is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the helper tool uses a global npm installation on the operator's computer and the tool discloses default telemetry.

Mitigation: Review the displayed version, registry, npm prefix, and install command before approval, and set JISHUBUDDY_TELEMETRY_DISABLED=true before launch when telemetry should be disabled.

Risk: Serial-port access, permission changes, or serial writes can affect the connected Raspberry Pi or expose device output.

Mitigation: Require separate approval for opening the port, changing access permissions, or sending input; start with bounded read-only capture and avoid replaying writes after reconnect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/raspberry-pi-serial-rescue)
- [Source homepage](https://github.com/x-aijishu/jishubuddy-skills/tree/main/raspberry-pi-serial-rescue)
- [JishuBuddy package](https://www.npmjs.com/package/jishubuddy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and bounded diagnostic instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user approval before installing JishuBuddy, opening serial ports, changing permissions, or sending serial input.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

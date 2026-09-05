## Description:

glkvm helps an agent remotely administer a target host through the GLKVM IP-KVM HTTP API, including keyboard and mouse input, screenshots and OCR, Fingerbot and ATX power actions, device reboot and firmware upgrade, and virtual MSD ISO storage management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[duzefu](https://clawhub.ai/user/duzefu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and administrators use this skill to guide an agent through authorized GLKVM remote administration tasks for a device and attached host, including screen inspection, HID input, power control, firmware operations, and virtual ISO storage workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables administrative control over a GLKVM device and attached host.

Mitigation: Use it only for devices the user owns or administers, and operate it on a trusted network.

Risk: The session cookie file contains an administrative token.

Mitigation: Treat /tmp/glkvm_cookies.txt as a credential and remove it when the session is finished.

Risk: Screenshots and OCR output may expose sensitive information from the target host screen.

Mitigation: Handle screen captures and OCR text as sensitive data and avoid retaining them beyond the task.

Risk: Power control, reboot, firmware upgrade, and MSD write operations can interrupt work, alter device state, or cause data loss.

Mitigation: Explain the action and obtain explicit user confirmation before performing disruptive operations.

Risk: The skill uses HTTPS requests with certificate verification disabled for GLKVM API access.

Mitigation: Limit use to trusted networks and independently verify the device address before sending credentials or commands.

## Reference(s):

- [ClawHub glkvm Skill Page](https://clawhub.ai/duzefu/skills/glkvm)
- [Publisher Profile](https://clawhub.ai/user/duzefu)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and HTTP API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference temporary screenshot and cookie files during authorized GLKVM sessions.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

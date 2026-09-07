## Description:

Control 750+ BLE intimate devices via Intiface Central using direct Buttplug v4 WebSocket protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chizumystic](https://clawhub.ai/user/chizumystic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to let an agent control compatible BLE intimate devices through Intiface Central, including listing devices, starting vibration, running patterns, and stopping devices. It is intended for consent-aware local or trusted-network operation where the user understands how to stop device activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control intimate hardware and includes indefinite vibration or pattern modes.

Mitigation: Use only with explicit participant consent, prefer timed commands, and confirm that the device stops after each session.

Risk: Remote WebSocket operation can expose device control beyond the local machine if a LAN address is used.

Mitigation: Use localhost by default and enable LAN access only on trusted networks with trusted participants.

Risk: Interrupted or disconnected sessions may leave uncertainty about the physical device state.

Mitigation: Know the stop command before use and verify that the device has actually stopped after interruptions or disconnects.

## Reference(s):

- [Intiface Central](https://intiface.com/central/)
- [Buttplug.io-compatible device index](https://iostindex.com)
- [Intiface Direct on ClawHub](https://clawhub.ai/chizumystic/skills/intiface-direct-package)
- [ws package tarball](https://registry.npmjs.org/ws/-/ws-8.21.1.tgz)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and Node.js command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate WebSocket control commands for local or trusted-network Intiface Central sessions.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

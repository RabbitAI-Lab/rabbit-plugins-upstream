## Description: <br>
Control 750+ BLE intimate devices via Intiface Central using the direct Buttplug v4 WebSocket protocol without MCP bridges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chizumystic](https://clawhub.ai/user/chizumystic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users with Intiface Central use this skill to let an agent list devices and issue vibration, stop, and pattern commands for connected Buttplug-compatible intimate devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can issue immediate physical actuation commands to intimate hardware over local or LAN WebSocket without built-in confirmation or value checks. <br>
Mitigation: Use only with explicit consent, confirm the exact device and command before actuation, start with low values, and keep an immediate stop option available. <br>
Risk: Remote or LAN Intiface access can expose connected device control on untrusted networks. <br>
Mitigation: Keep Intiface bound to localhost unless remote access is intentionally needed, and use only trusted networks for non-local connections. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chizumystic/skills/intiface-direct-control) <br>
- [Intiface Central](https://intiface.com/central/) <br>
- [Buttplug-compatible device index](https://iostindex.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON protocol examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and an Intiface Central WebSocket endpoint, defaulting to ws://localhost:12345.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

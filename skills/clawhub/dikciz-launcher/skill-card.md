## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Android device owners and operators use this skill to install and control Dikciz Launcher, manage its home and widgets, and carry out requested device, file, and automation tasks through its supported interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device controls, personal data, communications, and file operations can have sensitive or lasting effects.

Mitigation: Keep actions within the owner's requested scope, request only the Android access needed for the task, and obtain explicit direction for sensitive or destructive operations.

Risk: Remote control endpoints and enabled automation scripts can expose device access, files, or shell capabilities.

Mitigation: Keep remote control authenticated on a trusted network or encrypted VPN, protect bearer credentials, and enable only trusted scripts.

Risk: Background rules and recording features may capture or transmit device data or incur provider usage.

Mitigation: Review background rules and recordings, and configure only the requested automation and data sharing.

## Reference(s):

- [Dikciz Launcher project](https://github.com/psyb0t/dikciz-launcher)
- [Installation and connection guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [User guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/user-guide.md)
- [Configuration guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/dikciz-configuration.md)
- [Scripting tutorial](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/scripting-tutorial.md)
- [Hardware and speech guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/hardware-controls.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Code, Files, Guidance]

**Output Format:** [Markdown guidance with command examples, configuration snippets, and device operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions and results depend on the connected launcher build, Android permissions, and the owner's requested scope.]

## Skill Version(s):

0.30.3 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

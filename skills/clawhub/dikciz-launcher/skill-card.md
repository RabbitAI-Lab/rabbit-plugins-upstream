## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Android device owners use this skill to install Dikciz Launcher or operate an owner-selected phone through MCP, HTTP, or WebSocket. It supports scoped launcher, device-data, media, peripheral, file, and automation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote controls can expose sensitive phone functions and data.

Mitigation: Keep the endpoint private and authenticated, operate only on the owner-selected device, and grant only permissions needed for the requested task.

Risk: Assistant conversations can send requested phone data to the configured model provider.

Mitigation: Review what data the task sends and which provider receives it before using assistant features.

Risk: Privileged or destructive device actions can have lasting effects.

Mitigation: Require explicit owner direction for the action and approve its scope before proceeding.

## Reference(s):

- [Dikciz setup and connection](references/setup.md)
- [Dikciz capabilities](references/capabilities.md)
- [Hardware and speech operations](references/hardware-and-speech.md)
- [Files, notifications, and durable jobs](references/operations.md)
- [Dikciz Launcher project](https://github.com/psyb0t/dikciz-launcher)
- [Automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Files, APKs, and shell guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/files-and-apks.md)
- [Embedded chat guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/embedded-chat.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/dikciz-launcher)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Natural-language guidance, shell commands, JSON API arguments, and device operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available results depend on the selected device, granted Android access, and the installed build.]

## Skill Version(s):

0.30.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

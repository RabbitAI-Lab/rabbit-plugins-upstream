## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Android device owners and developers use this skill to install Dikciz Launcher and operate its launcher, widgets, device data, hardware features, files, and automation through the device's discovered control APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device control can affect private data, connected hardware, files, and privileged shell operations.

Mitigation: Use only the owner-selected device and explicitly requested scope; grant only the Android access needed, and set root to false when app-sandbox execution is intended.

Risk: Remote control traffic and credentials could be exposed if endpoints are reachable over an untrusted network.

Mitigation: Keep bearer credentials in the secret environment, enable authentication, and use a trusted connection or encrypted VPN.

Risk: Assistant features may send phone data or screenshots to the configured model provider, and event rules may continue using that provider while hidden.

Mitigation: Configure only requested assistant and event behavior, review what data is shared, and clear event rules when finished.

Risk: An APK could be replaced or signed by an unexpected publisher.

Mitigation: Verify the APK checksum and signing certificate before installation.

## Reference(s):

- [Dikciz Launcher release page](https://clawhub.ai/psyb0t/skills/dikciz-launcher)
- [Project documentation index](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/index.md)
- [Install and connect guide](artifact/references/setup.md)
- [Capability reference](artifact/references/capabilities.md)
- [Hardware and speech operations](artifact/references/hardware-and-speech.md)
- [File and shell guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/files-and-apks.md)
- [Embedded chat guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/embedded-chat.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Concise task results and instructions, with structured JSON or device files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include device status, captured media, transferred files, or command output; availability depends on the selected device and its granted access.]

## Skill Version(s):

0.30.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

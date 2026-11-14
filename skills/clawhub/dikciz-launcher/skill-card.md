## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and device owners use this skill to install Dikciz Launcher on an owner-selected Android phone and operate its launcher, apps, files, and supported device capabilities through the owner's configured endpoint. Operations remain subject to the requested task scope and Android permissions granted by the owner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include an official-release download that the scanner reports as outside the declared network allowlist; the scan also notes that its analysis was partial.

Mitigation: Review the network permissions and official-release download steps before installing, and verify the APK checksum and signing certificate against the project README.

## Reference(s):

- [Setup and connection guide](references/setup.md)
- [Dikciz capabilities](references/capabilities.md)
- [Hardware and speech operations](references/hardware-and-speech.md)
- [Files, notifications and durable jobs](references/operations.md)
- [Dikciz documentation index](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/index.md)
- [Automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Android access guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/android-access.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions, Files]

**Output Format:** [Markdown guidance, shell commands, JSON API requests, and device operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on the requested device operation; results may include files such as screenshots or transfers.]

## Skill Version(s):

0.32.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

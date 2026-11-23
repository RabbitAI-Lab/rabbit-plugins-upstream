## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External users use the skill to install an existing Dikciz APK and operate their selected Android device through its discovered interfaces. It guides scoped access to launcher features, files, hardware, automation and companion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanners classify the skill as suspicious because its setup guidance reportedly permits GitHub downloads outside the declared network scope; this is a review warning, not a finding of malicious intent.

Mitigation: Review download and network permissions before installing. Use an APK and verification materials obtained through an approved route, or confirm that the allowed network scope covers official release downloads; retain checksum and signing-certificate verification.

## Reference(s):

- [Dikciz Launcher project](https://github.com/psyb0t/dikciz-launcher)
- [Setup and Android access](references/setup.md)
- [Capabilities](references/capabilities.md)
- [Operations and companion workflows](references/operations.md)
- [Hardware and speech](references/hardware-and-speech.md)
- [Remote access tokens](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/remote-access-tokens.md)
- [Automation control](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Files and APKs](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/files-and-apks.md)
- [Custom apps](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/custom-apps.md)
- [Companion workflows](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/companion.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands, JSON arguments and API or MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations and results depend on the selected device, its Android permissions, available hardware and owner-authorized scope.]

## Skill Version(s):

0.36.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

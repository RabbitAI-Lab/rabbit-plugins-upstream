## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Android device owners and operators use the skill to install Dikciz Launcher on a selected device and manage its launcher, apps, data, hardware, and automations through documented controls. Device changes and sensitive actions require the owner's requested scope and Android access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence because setup instructions allow GitHub access beyond the declared network scope; scan evidence is incomplete.

Mitigation: Review the network-scope concern before installing. If proceeding with an official release download, require an explicit request and verify its checksum and signing certificate.

Risk: The scan did not cover all referenced local paths, so its findings may not describe those materials.

Mitigation: Review the missing referenced paths before relying on the scan assessment.

## Reference(s):

- [Install and connect to Dikciz](references/setup.md)
- [Dikciz capabilities](references/capabilities.md)
- [Dikciz operations](references/operations.md)
- [Hardware and speech](references/hardware-and-speech.md)
- [Remote access tokens](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/remote-access-tokens.md)
- [Token permission definitions](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/token-permissions.md)
- [Automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Files, APKs, and shell guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/files-and-apks.md)
- [Dikciz Launcher on ClawHub](https://clawhub.ai/psyb0t/skills/dikciz-launcher)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions, Files]

**Output Format:** [Markdown guidance with shell examples and structured device-control requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions are scoped to the selected device and its available Android permissions.]

## Skill Version(s):

0.31.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

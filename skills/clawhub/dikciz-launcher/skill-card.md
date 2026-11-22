## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External device owners and agent operators use this skill to install or operate Dikciz Launcher and manage its home, apps, files, Android data, hardware, and automations through the device's discovered interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags setup guidance as appearing to reach beyond the declared network scope; the scan was partial and four local references in SKILL.md were unresolved.

Mitigation: Review the setup network scope and resolve those references before installation; connect only to the owner-selected phone endpoint and documented recipients or providers for requested operations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/psyb0t/skills/dikciz-launcher)
- [Project documentation](https://github.com/psyb0t/dikciz-launcher)
- [Setup and connection guide](references/setup.md)
- [Capabilities reference](references/capabilities.md)
- [Operations reference](references/operations.md)
- [Hardware and speech reference](references/hardware-and-speech.md)
- [Automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Token permissions guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/token-permissions.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, Files]

**Output Format:** [Markdown guidance, shell commands, and structured MCP, HTTP, or WebSocket requests and results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations and results depend on the selected device, its live interface, and owner-granted Android access.]

## Skill Version(s):

0.35.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

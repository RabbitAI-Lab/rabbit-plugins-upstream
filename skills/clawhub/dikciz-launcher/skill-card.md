## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Android device owners use this skill to install Dikciz Launcher or operate an owner-selected phone through its discovered controls. It provides task-scoped guidance for launcher settings, device data, peripherals, files, and automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill controls powerful Android functions, and the external controller and installed APK were not fully audited.

Mitigation: Use a verified APK or explicitly authorize its retrieval; keep remote control authenticated on loopback or an encrypted private connection, and approve privileged actions individually.

Risk: Enabled Lua scripts act as full device controllers and can continue background work.

Mitigation: Enable only scripts you trust for the requested task, and stop unwanted background work.

Risk: Phone content sent through the assistant reaches its configured model provider.

Mitigation: Review the configured provider and send only phone content needed for the requested task.

## Reference(s):

- [Setup and connection](references/setup.md)
- [Capabilities](references/capabilities.md)
- [Files, notifications, and jobs](references/operations.md)
- [Hardware and speech](references/hardware-and-speech.md)
- [Dikciz Launcher documentation index](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/index.md)
- [Dikciz Launcher on ClawHub](https://clawhub.ai/psyb0t/skills/dikciz-launcher)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance, shell commands, and structured device results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested operation and may include device files such as screenshots, audio, or configuration.]

## Skill Version(s):

0.30.6 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

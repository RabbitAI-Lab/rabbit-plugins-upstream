## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and device owners use this skill to install Dikciz Launcher and operate an owner-selected Android phone through its discovered controls. It provides guidance for scoped device actions, configuration, automation, and hardware features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device controls can access personal data or change phone settings and files.

Mitigation: Use only the selected owner-controlled phone, grant only the permissions and token capabilities needed, and keep state-changing actions within the owner's requested scope.

Risk: Remote access or bearer credentials could expose phone controls.

Mitigation: Keep remote access private and authenticated, and store bearer credentials in a secret environment.

Risk: Custom apps share the Android access granted to Dikciz Launcher.

Mitigation: Review custom app code before enabling it and stop unwanted background work.

Risk: The security review does not cover the external controller, phone-side code, or APK.

Mitigation: Verify those components separately before use.

## Reference(s):

- [Setup and connection guide](artifact/references/setup.md)
- [Capabilities guide](artifact/references/capabilities.md)
- [Operations guide](artifact/references/operations.md)
- [Hardware and speech guide](artifact/references/hardware-and-speech.md)
- [Dikciz Launcher project](https://github.com/psyb0t/dikciz-launcher)
- [Remote access token guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/remote-access-tokens.md)
- [Automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Custom apps guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/custom-apps.md)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration guidance, Device results and requested files]

**Output Format:** [Markdown guidance, JSON requests, shell commands, and structured device results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected device, its available features, and owner-granted Android permissions.]

## Skill Version(s):

0.31.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

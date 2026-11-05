## Description:

Install and operate Dikciz Launcher on an owner-selected Android device. Use when controlling its home, HTML widgets, Lua, Android data, sensors, camera, audio, speech, Bluetooth, NFC, USB, Wi-Fi, files, APKs, shell sessions or command jobs through MCP, HTTP or WebSocket. Source builds use the Android Lab skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Android device owners and developers use this skill to install Dikciz Launcher and carry out requested, scoped tasks on their selected device through its documented controls. It also guides setup, configuration, and verification of device operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device controls and requested phone features can access sensitive data or perform consequential actions.

Mitigation: Grant only the phone permissions and token capabilities needed for the task, and require the owner's requested scope for sensitive changes or privileged actions.

Risk: Remote connections and assistant features can expose credentials or send requested phone data to configured recipients and providers.

Mitigation: Keep bearer credentials in the secret environment and use loopback forwarding or an encrypted VPN for remote access.

Risk: Controller scripts provide broad command access, and this review does not cover the external controller, APK, or SOS implementation.

Mitigation: Review scripts before enabling them and assess external components separately before use.

Risk: Official-release downloads require GitHub access beyond the declared network scope.

Mitigation: Use that access only when the user requests an official download, and verify the release checksum and signing certificate as documented.

## Reference(s):

- [ClawHub release](https://clawhub.ai/psyb0t/skills/dikciz-launcher)
- [Dikciz Launcher repository](https://github.com/psyb0t/dikciz-launcher)
- [Setup and connection guide](references/setup.md)
- [Capabilities reference](references/capabilities.md)
- [Operations reference](references/operations.md)
- [Remote access token guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/remote-access-tokens.md)
- [Custom apps guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/custom-apps.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Device operation results]

**Output Format:** [Human-readable instructions, shell commands, and structured API requests or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include requested device-operation results and configuration or file changes.]

## Skill Version(s):

0.30.12 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

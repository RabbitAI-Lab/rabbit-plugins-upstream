## Description:

Install a Dikciz Launcher APK with ADB and use its home screen, configuration, HTML widgets, Lua automation, WebSocket and HTTP controls, file transfers, APK installation, and MCP tools on the user's selected Android device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External users and Android developers can use this skill to install or connect to Dikciz Launcher on a selected Android device and manage its home screen, configuration, widgets, automations, files, and remote controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote control endpoints exposed beyond loopback may allow unintended access to device controls.

Mitigation: Keep controls on loopback, or use an authenticated encrypted private connection and a trusted network.

Risk: Persistent automations and broad Android permissions can cause unintended device actions.

Mitigation: Review automations before enabling them, grant only permissions needed for the task, and verify action results on the selected device.

Risk: Shell operations request root by default, and installation or configuration changes can affect the device or user data.

Mitigation: Use app-sandbox execution with root disabled when appropriate, verify the APK and control client, preserve existing configuration, and obtain explicit approval for privileged or destructive actions.

## Reference(s):

- [Dikciz capabilities](artifact/references/capabilities.md)
- [Install and connect to Dikciz](artifact/references/setup.md)
- [Dikciz user guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/user-guide.md)
- [Dikciz configuration guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/dikciz-configuration.md)
- [Dikciz scripting tutorial](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/scripting-tutorial.md)
- [Dikciz automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Dikciz files, APKs, and shell guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/files-and-apks.md)
- [Dikciz releases](https://github.com/psyb0t/dikciz-launcher/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and examples should be adapted to the selected device and its live launcher contract.]

## Skill Version(s):

0.17.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

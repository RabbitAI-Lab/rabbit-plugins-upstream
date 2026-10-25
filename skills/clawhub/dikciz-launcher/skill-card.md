## Description:

Install a Dikciz Launcher APK with ADB and use its home screen, configuration, HTML widgets, Lua automation, WebSocket and HTTP controls, file transfers, APK installation, and MCP tools on the user's selected Android device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Android device owners and developers use the skill to install or connect to Dikciz Launcher on a selected device, then manage its home screen, configuration, widgets, automation, and remote controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review covers the skill instructions, not the APK or external client's implementation.

Mitigation: Verify the APK's source and signing certificate before installation, and assess the external client separately.

Risk: Android permissions, scripts, and widgets can access device capabilities or affect user data.

Mitigation: Grant only permissions needed for the requested task and enable only trusted scripts and widgets.

Risk: Remote control access can expose device operations.

Mitigation: Keep remote access authenticated and private, preferably over an encrypted VPN.

Risk: Root shell commands have elevated privileges.

Mitigation: Use root: false for ordinary shell commands.

## Reference(s):

- [Setup and connection guide](references/setup.md)
- [Capabilities reference](references/capabilities.md)
- [Dikciz user guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/user-guide.md)
- [Dikciz configuration guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/dikciz-configuration.md)
- [Dikciz scripting tutorial](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/scripting-tutorial.md)
- [Dikciz automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Dikciz files and APKs guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/files-and-apks.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell commands, configuration examples, and HTML, JavaScript, or Lua snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device- and task-specific instructions; commands should use the selected device and discovered control interface.]

## Skill Version(s):

0.24.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

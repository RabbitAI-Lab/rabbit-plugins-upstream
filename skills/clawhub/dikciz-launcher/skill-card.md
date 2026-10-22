## Description:

Install a Dikciz Launcher APK with ADB and use its home screen, configuration, HTML widgets, Lua automation, WebSocket and HTTP controls, file transfers, APK installation, and MCP tools on the user's selected Android device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External users and Android automation developers use this skill to install or connect Dikciz Launcher on a selected Android device and manage its home screen, configuration, and automation features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell requests root by default, and Lua action policies do not restrict every script command.

Mitigation: Use root:false for app-sandbox execution, enable only trusted scripts, and obtain explicit approval before privileged operations.

Risk: Remote controls can expose powerful Android operations if reachable or unauthenticated.

Mitigation: Keep endpoints private and authenticated, and forward only the selected device's ports to host loopback.

Risk: Android permissions and special access can expose device data or capabilities.

Mitigation: Grant only the permissions needed for the task and use owner approval for sensitive access.

Risk: The clean scan verdict does not certify a separately supplied APK.

Mitigation: Assess the specific APK independently before installation.

## Reference(s):

- [Setup reference](references/setup.md)
- [Capabilities reference](references/capabilities.md)
- [User guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/user-guide.md)
- [Configuration guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/dikciz-configuration.md)
- [Scripting tutorial](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/scripting-tutorial.md)
- [Automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Files and APKs guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/files-and-apks.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device-dependent; requires the selected Android device and its granted permissions.]

## Skill Version(s):

0.20.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

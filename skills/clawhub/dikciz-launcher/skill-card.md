## Description:

Install a Dikciz Launcher APK with ADB and use its home screen, configuration, HTML widgets, Lua automation, WebSocket controls, and MCP tools on the user's selected Android device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Android device owners and developers use this skill to install or connect to Dikciz Launcher on a selected device, customize its home and widgets, and carry out approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Launcher configuration replacement, home reset, device administration, accessibility control, SMS actions, and root shell commands can change or expose device state.

Mitigation: Use the selected device only; explain the effect and seek explicit approval before these high-impact actions.

Risk: Remote-control credentials or exposed control endpoints can enable unauthorized device access.

Mitigation: Keep bearer tokens in a private secret environment and forward only the selected device's ports to host loopback.

Risk: A successful install or queued automation event does not prove the intended device action completed.

Mitigation: Verify the launcher on the selected device and check fresh snapshots, script status, and logs after actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/dikciz-launcher)
- [Dikciz capabilities](references/capabilities.md)
- [Installation and connection](references/setup.md)
- [Dikciz user guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/user-guide.md)
- [Dikciz configuration guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/dikciz-configuration.md)
- [Dikciz scripting tutorial](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/scripting-tutorial.md)
- [Dikciz automation control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with command, configuration, HTML, and Lua snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions and installation results require verification on the selected device.]

## Skill Version(s):

0.15.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

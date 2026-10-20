## Description:

Install a Dikciz Launcher APK with ADB and use its home screen, configuration, HTML widgets, Lua automation, WebSocket and HTTP controls, file transfers, APK installation, and MCP tools on the user's selected Android device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and device owners use this skill to install or connect to Dikciz Launcher on a selected Android device, configure its home screen and automation, and control supported device features with user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device control can affect other apps or change device settings, including through Accessibility, SMS, root shell, APK installation, and Device Administration.

Mitigation: Use only on a device the user controls; explain sensitive actions and obtain approval before requesting the necessary Android access.

Risk: Exposed network controls or leaked bearer tokens could allow unauthorized device access.

Mitigation: Keep bearer tokens in a secret environment rather than files or command arguments, and review direct network binding before enabling it.

## Reference(s):

- [Dikciz Launcher user guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/user-guide.md)
- [Dikciz Launcher configuration guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/dikciz-configuration.md)
- [Dikciz Launcher scripting tutorial](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/scripting-tutorial.md)
- [Dikciz Launcher automation control](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)
- [Dikciz Launcher files and APKs](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/files-and-apks.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with bash, JSON, and Lua examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device-specific instructions; verify outcomes using live device state.]

## Skill Version(s):

0.15.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

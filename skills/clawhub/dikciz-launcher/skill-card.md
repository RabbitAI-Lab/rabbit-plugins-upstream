## Description:

Install a Dikciz Launcher APK with ADB and use its home screen, configuration, HTML widgets, Lua automation, WebSocket controls, and MCP tools on the user's selected Android device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Android device owners and developers use this skill to install a user-provided Dikciz Launcher APK and manage the selected device's home screen, widgets, configuration, and automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted APK or targeting the wrong Android device can compromise or alter the device.

Mitigation: Use an APK and device the owner trusts; confirm the selected device before installing or issuing commands.

Risk: Accessibility actions, SMS, explicit intents, and shell or root-capable commands can cause high-impact device changes.

Mitigation: Obtain approval for each high-impact action, grant only needed access, and verify the outcome on the selected device.

Risk: Exposed control ports or bearer tokens can enable unauthorized device control.

Mitigation: Keep forwarded ports on host loopback and bearer tokens in a secret environment, not files or command arguments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/dikciz-launcher)
- [Installation and connection](references/setup.md)
- [Dikciz capabilities](references/capabilities.md)
- [Dikciz user guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/user-guide.md)
- [Dikciz configuration guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/dikciz-configuration.md)
- [Dikciz scripting tutorial](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/scripting-tutorial.md)
- [Dikciz automation-control guide](https://github.com/psyb0t/dikciz-launcher/blob/main/docs/automation-control.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device-specific instructions and verification results.]

## Skill Version(s):

0.13.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

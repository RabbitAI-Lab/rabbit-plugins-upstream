## Description:

Agent Notify helps users configure local sound, desktop, and taskbar or dock notifications for AI coding agents when confirmation is needed or a task completes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miluer-tcq](https://clawhub.ai/user/miluer-tcq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to install and customize local notification hooks so they can be alerted when an AI coding agent needs confirmation or finishes a task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer persistently changes agent settings to add local command hooks.

Mitigation: Review the generated settings.json hook changes before installing, especially when multiple coding agents share local configuration.

Risk: The security review notes script argument-handling weaknesses.

Mitigation: Prefer a version that fixes Python argument interpolation and review custom sound or config paths before use.

Risk: The artifact claims Windows support, but the provided artifact files do not include the referenced Windows notification script.

Mitigation: Treat Windows setup as incomplete until notify-windows.ps1 is included or the Windows support claim is removed.

## Reference(s):

- [Agent Notify on ClawHub](https://clawhub.ai/miluer-tcq/skills/agent-notify)
- [miluer-tcq Publisher Profile](https://clawhub.ai/user/miluer-tcq)
- [Bundled README](artifact/README.md)
- [Default Notification Configuration](artifact/config/default.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local setup, test, customization, and uninstall guidance for notification hooks.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

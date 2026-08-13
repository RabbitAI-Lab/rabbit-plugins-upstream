## Description:

Develop, run, and troubleshoot Python programs for the UNIHIKER M10 from Windows or macOS using the unihiker and PinPong APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nick-ccq](https://clawhub.ai/user/nick-ccq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and hardware engineers use this skill to generate, deploy, and troubleshoot Python programs for a connected UNIHIKER M10. It supports display, buttons, sensors, buzzer, GPIO, audio, SSH deployment, Python environment selection, and offline dependency installation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect to and modify a UNIHIKER M10 over SSH.

Mitigation: Use it only for intended M10 development, verify the board connection first, and review the planned upload, execution, package install, or process termination before it runs.

Risk: Factory-default SSH credentials may remain active on the device.

Mitigation: Change the default password and enter current credentials interactively instead of storing passwords in project files.

Risk: Generated programs can operate hardware, record audio, display Wi-Fi QR codes, install packages, or continue running in the background.

Mitigation: Review generated Python before deployment, confirm wiring and privacy assumptions, and track whether a program is running in the foreground or background and how to stop it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nick-ccq/skills/unihiker-m10-python)
- [Publisher profile](https://clawhub.ai/user/nick-ccq)
- [Project homepage](https://github.com/Nick-ccq/unihiker-m10-python)
- [Connection guide](references/connection-guide.md)
- [Python environments](references/m10-python-env.md)
- [Hardware reference](references/m10-hardware.md)
- [UNIHIKER and PinPong API](references/unihiker-pinpong-api.md)
- [Code templates](references/code-templates.md)
- [Examples](references/examples.md)
- [No-local-Python workflow](references/no-python-workflow.md)
- [Offline dependencies](references/offline-dependencies.md)
- [macOS workflow](references/macos-workflow.md)
- [Official UNIHIKER M10 image documentation](https://www.unihiker.com.cn/wiki/m10/burner)
- [Official UNIHIKER M10 documentation](https://www.unihiker.com.cn/wiki/m10/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python code, shell commands, PowerShell commands, and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce deployable Python programs and device operation commands for a connected UNIHIKER M10.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

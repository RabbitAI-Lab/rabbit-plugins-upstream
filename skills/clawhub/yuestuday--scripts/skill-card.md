## Description:

Windows background watchdog for the OpenClaw Gateway: 5s health checks, auto-restart on crash, hidden no-window operation, tray status icon, and a maintenance lock that keeps repairs (doctor --fix) from racing the watchdog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuestuday](https://clawhub.ai/user/yuestuday)

### License/Terms of Use:

MIT-0

## Use Case:

Windows OpenClaw operators and developers use this skill to install a background Gateway watchdog, check its health, and coordinate repairs without competing restarts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The administrator installer can terminate unrelated node.exe and wscript.exe processes.

Mitigation: Review the installer before running it; prefer process targeting limited to OpenClaw-owned instances.

Risk: The hidden watchdog can run openclaw doctor --fix automatically and persist as a scheduled task.

Mitigation: Install only when persistent background repair is intended; review scripts and document how to disable or uninstall the scheduled tasks.

## Reference(s):

- [Gateway Watchdog on ClawHub](https://clawhub.ai/yuestuday/skills/scripts)
- [Deployment guide](README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with PowerShell and Windows command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

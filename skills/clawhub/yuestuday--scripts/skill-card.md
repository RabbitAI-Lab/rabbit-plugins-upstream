## Description:

Windows background watchdog for the OpenClaw Gateway: 5s health checks, auto-restart on crash, hidden no-window operation, tray status icon, and a maintenance lock that keeps repairs (doctor --fix) from racing the watchdog. Auto-repair is OFF by default; the watchdog only restarts the Gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuestuday](https://clawhub.ai/user/yuestuday)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators running an OpenClaw Gateway on Windows use this skill to install and manage a background watchdog, check Gateway health, recover from failures, and coordinate maintenance safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks this release suspicious for concerns involving administrator task setup, the background watchdog, and maintenance controls; coverage was partial, with tool-misuse analysis degraded for one installer file.

Mitigation: Review the administrator installer, executable selection, and watchdog pause behavior before installation; inspect the relevant scripts yourself before granting elevation.

Risk: The watchdog runs hidden and persists through scheduled tasks across logons, which can make its activity less visible and leave it running after setup.

Mitigation: Review the task changes and logging behavior before installation, and keep the documented pause and uninstall steps available.

## Reference(s):

- [Gateway Watchdog on ClawHub](https://clawhub.ai/yuestuday/skills/scripts)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [PowerShell, batch, and VBScript files with Markdown deployment guidance and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-specific; scheduled-task installation requires Administrator privileges; the watchdog runs persistently in the background.]

## Skill Version(s):

0.0.2 (source: server release metadata; artifact frontmatter states 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Installs egregore watchdog daemon via launchd or systemd for autonomous relaunching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after initializing an egregore project or setting up egregore on a new machine when they want the session watchdog to relaunch work automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs a persistent watchdog that can relaunch autonomous egregore sessions in the background.

Mitigation: Install only when autonomous relaunching is intended; review the referenced install scripts, confirm they run as the current user rather than root, and verify how to disable the launchd or systemd timer.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-egregore-install-watchdog)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operating-system-specific launchd and systemd installation, verification, logging, troubleshooting, and uninstall guidance.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description: <br>
Installs an egregore watchdog daemon via launchd or systemd for autonomous relaunching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill after initializing or moving an egregore project when they want the local egregore process relaunched automatically by the operating system scheduler. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs a watchdog that can relaunch egregore autonomously every five minutes. <br>
Mitigation: Use it only when autonomous relaunching is desired, confirm the five-minute schedule is acceptable, and keep the uninstall command available. <br>
Risk: The generated launchd or systemd scheduler files change local background process behavior. <br>
Mitigation: Review the scheduler files before running the installer and verify the installed service or timer status afterward. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-install-watchdog) <br>
- [egregore project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operating-system-specific launchd and systemd install, verification, uninstall, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

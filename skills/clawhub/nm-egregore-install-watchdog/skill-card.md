## Description: <br>
Installs an egregore watchdog daemon through launchd or systemd so egregore can relaunch autonomously. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when setting up egregore on a workstation or server and want a local watchdog to relaunch sessions when work is available. It is not intended for CI/CD runners or environments where manual control over session launches is required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs a persistent watchdog using launchd or systemd that can relaunch egregore on a schedule. <br>
Mitigation: Review the scheduler unit or plist before installation, confirm the user wants persistent relaunch behavior, and keep the uninstall command available. <br>
Risk: The security scan verdict is suspicious because persistence requires clearer consent and removal guidance. <br>
Mitigation: Confirm the installation target, schedule interval, log location, and removal path before enabling the watchdog. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-install-watchdog) <br>
- [Egregore project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash commands and verification guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide installation of a persistent user-level launchd or systemd watchdog when the proposed commands are executed.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

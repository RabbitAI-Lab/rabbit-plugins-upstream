## Description: <br>
Removes the egregore watchdog daemon and its associated files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to stop automatic egregore session relaunching and remove the user-level watchdog files created by the install-watchdog workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The cleanup commands remove specific user-level service files and watchdog logs. <br>
Mitigation: Verify the paths belong to the egregore watchdog installation before running the removal commands. <br>
Risk: Removing the watchdog disables automatic egregore session relaunching. <br>
Mitigation: Use the skill only when automatic relaunching is no longer wanted or when switching to manual invocation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-uninstall-watchdog) <br>
- [Egregore plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes platform-specific macOS launchd and Linux systemd cleanup commands plus verification steps.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter states 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

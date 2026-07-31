## Description: <br>
Removes the egregore watchdog daemon and its associated files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to stop and remove an egregore watchdog service when they no longer want automatic session relaunching or are cleaning up egregore infrastructure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The cleanup commands delete watchdog service files, a pid file, and a log from user-level paths. <br>
Mitigation: Review the listed paths and confirm the egregore watchdog was installed before running the removal commands. <br>
Risk: Running the commands stops automatic egregore session relaunching. <br>
Mitigation: Use the skill only when automatic relaunching should be disabled or when removing egregore infrastructure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-uninstall-watchdog) <br>
- [Egregore plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides removal of named watchdog service files, pid files, and logs.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

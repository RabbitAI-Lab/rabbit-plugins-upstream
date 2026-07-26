## Description: <br>
Use the ClawdHub CLI to search, install, update, and publish agent skills from clawdhub.com. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nicoataiza](https://clawhub.ai/user/nicoataiza) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to manage ClawdHub skills from the command line, including search, install, update, list, authentication, and publishing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CLI commands can change local skill directories or publish skill folders. <br>
Mitigation: Review the target registry, working directory, and command arguments before login, install, update, or publish actions. <br>
Risk: Bulk update commands with force and no-input flags can apply broad local skill changes. <br>
Mitigation: Avoid `--no-input --force` bulk updates unless broad local changes are intentional. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/nicoataiza/skills/clawdhub-bak-2026-01-28t18-01-16-10-30) <br>
- [ClawdHub registry](https://clawdhub.com) <br>
- [ClawdHub npm package](https://www.npmjs.com/package/clawdhub) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may install, update, or publish skills through the ClawdHub CLI and should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

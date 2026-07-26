## Description: <br>
Manage Todoist tasks using the `todoist` CLI. Add, list, and complete tasks from the command line. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and task-focused users use this skill to have an agent produce Todoist CLI commands for listing, creating, and completing tasks from the command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands produced by the skill can modify tasks in a connected task account. <br>
Mitigation: Review commands before execution and use a narrowly scoped Todoist token where available. <br>
Risk: The security summary says credential and backend documentation is broader and less scoped than a Todoist-only tool should be. <br>
Mitigation: Use the skill only when task-account access is expected, and do not provide a Microsoft Graph token unless the publisher documents the required permissions. <br>
Risk: The authoritative security verdict is suspicious. <br>
Mitigation: Review the skill carefully before installation and test with a low-impact or isolated task account first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/brainz-tasks) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the `todoist` CLI and a task-service credential such as `TODOIST_API_TOKEN`; commands can modify the connected task account.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

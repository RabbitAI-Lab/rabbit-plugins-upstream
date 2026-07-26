## Description: <br>
Manage and track tasks and projects persistently with priorities, completion status, filtering, and secure Markdown export across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johstracke](https://clawhub.ai/user/johstracke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agents, and teams use Task Runner to keep persistent task lists across conversations, organize work by project, prioritize items, mark completion, and export project status to Markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task descriptions are stored locally and may persist across conversations. <br>
Mitigation: Avoid storing secrets or sensitive details in tasks, and review or delete local task data according to your retention needs. <br>
Risk: Markdown export can write files in the workspace, home directory, or /tmp and may overwrite an existing file. <br>
Mitigation: Review export paths before running the export command and choose non-sensitive destinations. <br>


## Reference(s): <br>
- [ClawHub Task Runner page](https://clawhub.ai/johstracke/skills/task-runner) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [CLI text output and Markdown export files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Persists task data locally and can write Markdown exports to user-selected safe paths.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Workflowy outliner CLI for reading, searching, adding, editing, completing, deleting, and reporting on Workflowy outline nodes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[waldyrious](https://clawhub.ai/user/waldyrious) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Workflowy users use this skill to inspect, search, and update Workflowy outlines through the unofficial workflowy CLI, including bulk operations and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflowy CLI requires a Workflowy API key that can grant access to outline content. <br>
Mitigation: Protect the API key in the WORKFLOWY_API_KEY environment variable or ~/.workflowy/api.key and restrict file permissions for local key storage. <br>
Risk: The skill can create, update, move, complete, transform, bulk-replace, or delete Workflowy nodes. <br>
Mitigation: Require explicit user confirmation before running mutating, destructive, or bulk commands, and prefer dry-run or interactive modes for replacements. <br>
Risk: Full-tree export or backup methods can expose broad outline content. <br>
Mitigation: Prefer scoped reads for ordinary tasks and use export or backup methods only when broad access is necessary. <br>


## Reference(s): <br>
- [Workflowy Skill on ClawHub](https://clawhub.ai/waldyrious/skills/workflowy) <br>
- [workflowy CLI repository](https://github.com/mholzen/workflowy) <br>
- [workflowy CLI command reference](https://github.com/mholzen/workflowy/blob/main/docs/CLI.md) <br>
- [Workflowy API reference](https://workflowy.com/api-reference/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that read or mutate Workflowy outline data through the workflowy CLI.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

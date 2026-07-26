## Description: <br>
Stdin/stdout file inbox/outbox bridge for passing files to/from Clawdbot using an MCP stdio server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[safatinaztepe](https://clawhub.ai/user/safatinaztepe) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill as a local filesystem-backed handoff area for moving input files through inbox and tmp folders and placing deliverables in an outbox. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent can access files intentionally placed in the stdio inbox, tmp, and outbox folders. <br>
Mitigation: Place only files intended for agent processing in those folders. <br>
Risk: Overwrite and delete operations can destructively change files inside the stdio folders. <br>
Mitigation: Review requested file operations and use overwrite or delete only when replacement or removal is intended. <br>
Risk: The stdio_paths output can reveal absolute local filesystem paths. <br>
Mitigation: Avoid sharing stdio_paths output when local path disclosure is sensitive. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [MCP tool responses as JSON text, with files read and written as base64 content in local stdio folders] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Operations are restricted to the configured inbox, tmp, and outbox folders.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

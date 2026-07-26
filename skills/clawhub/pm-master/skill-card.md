## Description: <br>
PM Master helps project managers coordinate BA and SA work across project kickoff, MVP planning, workload assessment, overall project planning, and iteration planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leo21cn](https://clawhub.ai/user/leo21cn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Project managers and delivery teams use this skill as a PM assistant to draft project kickoff, MVP, workload, overall planning, and iteration planning artifacts from provided requirements, architecture, constraints, and staffing inputs. Outputs are proposals that require review by a real PM before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project requirements, architecture documents, staffing, cost, or schedule data may be sent to an external MCP service. <br>
Mitigation: Use the skill only when the publisher and MCP service operator are trusted for the project data being shared, and notify users before confidential project materials are sent. <br>
Risk: The artifact includes a hard-coded shared bearer token for the remote MCP service. <br>
Mitigation: Revoke the published token and replace it with user-provided credentials before production or confidential use. <br>
Risk: The security verdict is suspicious because of the external service and credential handling. <br>
Mitigation: Review the skill and deployment configuration before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leo21cn/skills/pm-master) <br>
- [Remote MCP service endpoint](https://mcp.smartmoves.com.cn/pm/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown documents and conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces PM planning drafts through staged remote MCP tool workflows; outputs should be reviewed by a human PM before use.] <br>

## Skill Version(s): <br>
1.8.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

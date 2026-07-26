## Description: <br>
BA Master Agent converts vague product or system concepts into structured requirements assets, including requirements specifications, process models, data dictionaries, user stories, UI view specifications, and compliance review reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leo21cn](https://clawhub.ai/user/leo21cn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business analysts, product teams, and implementation teams use this skill to clarify requirements and produce structured BA deliverables from early concepts or existing requirements materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends requirements, process descriptions, data dictionaries, and compliance materials to a remote MCP service. <br>
Mitigation: Use it only for data that is approved for transfer to mcp.smartmoves.com.cn, and confirm any required data-processing agreement before using confidential client or regulated data. <br>
Risk: The artifact includes an embedded bearer token for the remote service. <br>
Mitigation: Treat the token as shared or compromised and prefer a release that requires user-provided credentials. <br>
Risk: The MCP proxy can call a broad set of BA tools through the remote service. <br>
Mitigation: Review the available tools before deployment and prefer an allowlist of permitted BA tools. <br>


## Reference(s): <br>
- [Ba Master ClawHub listing](https://clawhub.ai/leo21cn/skills/ba-master) <br>
- [Publisher profile](https://clawhub.ai/user/leo21cn) <br>
- [Remote MCP service endpoint](https://mcp.smartmoves.com.cn/ba/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown documents and conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include Mermaid diagrams, requirements tables, user stories, UI specifications, and compliance review summaries.] <br>

## Skill Version(s): <br>
1.8.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

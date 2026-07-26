## Description: <br>
Group cruise travel solution MCP Server for corporate groups and organizations, helping teams request tailored cruise travel products. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this MCP skill to support group cruise planning for companies, corporate groups, and organizations that need customized cruise travel options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote MCP use can send task context to an external cruise-planning service and may return guidance that affects corporate travel decisions. <br>
Mitigation: Use the skill for explicit group cruise-planning tasks, avoid sharing unnecessary sensitive travel details, and review agent outputs before acting on recommendations. <br>
Risk: The security guidance notes that operational workflows can depend on authenticated CLI credentials and production-impacting actions. <br>
Mitigation: Use explicit targets, dry runs where available, and human confirmation before production changes, emails, public comments, bans, transfers, or migrations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/craftwave-skill-6-mcp) <br>
- [MCP server schema](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, API calls, configuration] <br>
**Output Format:** [MCP tool responses and JSON server configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a remote streamable HTTP MCP endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

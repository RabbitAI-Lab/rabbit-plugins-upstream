## Description: <br>
Luxury Cruise Experience MCP Server helps travelers filter premium cruise options by brand and destination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-focused agents use this MCP server to discover luxury cruise journeys and narrow premium options by cruise brand and destination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects agents to a third-party remote MCP endpoint for cruise search behavior. <br>
Mitigation: Review the endpoint and requested actions before installation, and use the skill only in environments where third-party travel-service calls are appropriate. <br>
Risk: Security evidence recommends reviewing commands and preserving dry-run or audit-log checks before use. <br>
Mitigation: Keep review and audit steps enabled and verify the installed bundle matches the server-provided release evidence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/craftwave-skill-8-mcp) <br>
- [Remote MCP endpoint](https://cruise-mcp.olavacations.com/api/gw/mcp/6426abde-462c-468a-9959-5ae1aeb52d69) <br>
- [MCP server schema](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Guidance] <br>
**Output Format:** [MCP tool responses from a remote streamable HTTP server] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Filters luxury cruise options by brand and destination through a hosted remote endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

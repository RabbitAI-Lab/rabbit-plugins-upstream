## Description: <br>
This MCP server recommends high-end cruise experiences, facilities, and services for luxury travelers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users or travel-planning agents use this MCP connector to request luxury cruise recommendations and information about premium facilities and services from a third-party remote service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connector sends agent requests to a third-party cruise recommendation service. <br>
Mitigation: Avoid sending sensitive personal, payment, passport, account, or credential information unless the provider is trusted and its data handling is understood. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/309441738/skills/craftwave-skill-7-mcp) <br>
- [Remote MCP endpoint](https://cruise-mcp.olavacations.com/api/gw/mcp/7b49d758-2bec-48a6-be3d-19b11f954c07) <br>
- [Model Context Protocol server schema](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [MCP responses from a remote streamable HTTP server] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connects to a third-party remote MCP endpoint for cruise recommendation content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

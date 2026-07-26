## Description: <br>
Cruise Products for Beach Vacations MCP Server helps agents explore cruise products tailored for beach vacation enthusiasts, sun seekers, and relaxation lovers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can connect an agent to the OLA Vacations remote MCP service to search beach-focused cruise vacation products. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent queries are sent to a remote OLA Vacations MCP service and may contain travel preferences or booking details. <br>
Mitigation: Install only when remote cruise product search is intended, review the provider's privacy terms, and avoid sending unnecessary personal information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/ola-cruise-beach-mcp) <br>
- [OLA Vacations remote MCP service](https://cruise-mcp.olavacations.com/api/gw/mcp/a6060d76-a93a-43af-aca2-e3051a9d47c7) <br>
- [MCP server schema](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, configuration] <br>
**Output Format:** [MCP tool responses over streamable HTTP with markdown installation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a remote OLA Vacations MCP endpoint; security evidence reports no local execution, persistence, or credential handling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

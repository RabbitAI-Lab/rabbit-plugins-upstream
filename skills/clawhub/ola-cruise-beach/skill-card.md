## Description: <br>
Explore cruise products specifically tailored for beach vacation enthusiasts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search beach-oriented cruise products, including filtering by brand, departure city, price range, destination, duration, cruise line, and date. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise-search inputs are sent to an external CruiseSkillBridge/olavacations MCP gateway. <br>
Mitigation: Avoid submitting sensitive personal or business data unless the publisher provides acceptable privacy, logging, and retention details. <br>
Risk: The artifact contains no local executable code, so behavior depends on the remote MCP service that answers product_list queries. <br>
Mitigation: Review the disclosed MCP remote URL and test the tool with non-sensitive inputs before relying on results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/309441738/skills/ola-cruise-beach) <br>
- [MCP Server Reference](references/mcp.md) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>
- [Cruise MCP Gateway](https://cruise-mcp.olavacations.com/api/gw/mcp/a6060d76-a93a-43af-aca2-e3051a9d47c7) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, API calls, guidance] <br>
**Output Format:** [MCP tool responses and JSON-compatible request or response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes product_list queries through a disclosed external streamable HTTP MCP gateway.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

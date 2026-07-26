## Description: <br>
Helps users compare cruise products by price, itinerary, brand, and related filters through a remote MCP product lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Travel shoppers, cruise advisors, and agent builders can use this MCP skill to retrieve filtered cruise product lists for comparison by brand, departure city, price range, destination, duration, cruise line, and date. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise search and filter requests are sent to the disclosed CruiseSkillBridge/Ola Vacations MCP gateway. <br>
Mitigation: Install and use the skill only when the user trusts that remote service, and avoid entering sensitive personal details unless required and approved. <br>
Risk: Documentation indicates a product_list lookup and contains placeholder capability text, so users may overestimate the level of automated comparison. <br>
Mitigation: Validate the available MCP tool behavior against the intended workflow before relying on outputs for booking or commercial decisions. <br>


## Reference(s): <br>
- [MCP Server 接入](references/mcp.md) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>
- [Ola Vacations MCP gateway](https://cruise-mcp.olavacations.com/api/gw/mcp/607dada7-85a0-4d70-b7df-bddcdec3009f) <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/ola-cp-comparison) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [MCP remote responses with Markdown setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a streamable HTTP MCP remote endpoint for product_list cruise filtering.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter/server.json: 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

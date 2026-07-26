## Description: <br>
为公司团体或组织提供邮轮旅行方案，适合团队出行的需求，制定专属的邮轮产品。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and travel-planning teams use this MCP skill to find cruise products for corporate groups or organizations, including filtering by brand, departure city, price range, destination, duration, ship, and date. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise planning queries are sent to an external CruiseSkillBridge/olavacations MCP gateway, and logging or retention practices are not clearly documented. <br>
Mitigation: Avoid sending confidential employee, traveler, payment, or internal business details unless the publisher and gateway service are trusted. <br>


## Reference(s): <br>
- [MCP server reference](references/mcp.md) <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/craftwave-skill-6) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>
- [MCP server schema](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API Calls] <br>
**Output Format:** [Markdown and MCP tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The published product_list tool filters cruise products by brand, departure city, price range, destination, duration, ship, and date.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

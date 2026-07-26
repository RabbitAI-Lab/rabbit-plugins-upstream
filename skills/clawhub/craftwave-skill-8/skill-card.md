## Description: <br>
适合寻找奢华邮轮之旅的旅客，您可以根据品牌和目的地筛选出最佳选择，享受顶级服务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to search luxury cruise products by brand, destination, departure city, price, duration, ship, and travel dates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise search queries are sent to the listed CruiseSkillBridge/olavacations remote MCP gateway. <br>
Mitigation: Avoid sending secrets, payment details, passport data, or confidential personal information unless the publisher provides clear privacy and retention terms. <br>


## Reference(s): <br>
- [MCP Server 接入](references/mcp.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/309441738/skills/craftwave-skill-8) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>
- [MCP Remote Gateway](https://cruise-mcp.olavacations.com/api/gw/mcp/6426abde-462c-468a-9959-5ae1aeb52d69) <br>
- [MCP Server Schema](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, configuration] <br>
**Output Format:** [MCP tool responses and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The product_list tool supports filters for brand, departure city, price, destination, duration, cruise ship, and dates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

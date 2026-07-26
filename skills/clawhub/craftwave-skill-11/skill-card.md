## Description: <br>
通过智能助手帮助客户快速找到合适的邮轮产品，轻松获取信息与建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-focused agents use this skill to search cruise products, filter options by trip criteria, and retrieve product details or recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise search queries and related request content are sent to the CruiseSkillBridge/olavacations external gateway. <br>
Mitigation: Do not include secrets, payment data, or sensitive personal information unless the gateway's privacy and retention terms have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/craftwave-skill-11) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>
- [CruiseSkillBridge MCP gateway](https://cruise-mcp.olavacations.com/api/gw/mcp/edc528f4-5640-48bd-8b90-6c5f37f44e06) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, API calls] <br>
**Output Format:** [Markdown or structured tool responses with cruise product search results and product details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are mediated through the CruiseSkillBridge/olavacations external gateway.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
cruise-product —— 由 CruiseSkillBridge 一键发布的MCP。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this remote MCP skill to list, search, and retrieve details for cruise products through published tools such as product_list, product_info, and product_search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise search requests are sent to an external CruiseSkillBridge/olavacations MCP gateway and may be counted in provider statistics. <br>
Mitigation: Install only if that external request handling is acceptable, and do not send secrets, payment details, or sensitive customer data unless the provider's privacy and retention practices meet your needs. <br>


## Reference(s): <br>
- [MCP Server 接入](references/mcp.md) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/309441738/skills/cruise-product) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Configuration, Guidance] <br>
**Output Format:** [MCP tool responses, Markdown guidance, and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote MCP calls are routed through the CruiseSkillBridge/olavacations gateway.] <br>

## Skill Version(s): <br>
17.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

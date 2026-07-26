## Description: <br>
通过 NPM 使用邮轮产品 API，开发者可以在自己的应用中集成邮轮产品信息。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to integrate cruise product discovery into applications, including product listing, product detail lookup, and keyword search through a remote CruiseSkillBridge gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends cruise-product search inputs and product identifiers to a remote CruiseSkillBridge/Olavacations service. <br>
Mitigation: Use only when remote processing is acceptable, and do not submit secrets, credentials, personal data, or regulated business data without suitable privacy and retention terms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/npm) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>
- [CruiseSkillBridge gateway invoke endpoint](https://cruise-mcp.olavacations.com/api/gw/s/d7f4b5ce-46c8-4a1f-a270-e04b0fe32424/invoke) <br>
- [MCP server schema](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON request examples and remote API endpoints] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote calls are metered through CruiseSkillBridge; avoid submitting secrets, credentials, personal data, or regulated business data unless acceptable terms are provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter and server.json report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

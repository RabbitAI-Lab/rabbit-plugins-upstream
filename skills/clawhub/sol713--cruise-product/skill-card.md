## Description: <br>
cruise-product is a CruiseSkillBridge-published MCP skill that exposes tools for cruise product listing, detail lookup, and keyword search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sol713](https://clawhub.ai/user/sol713) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents can use this skill to search cruise products, filter cruise listings by travel and pricing criteria, and retrieve cruise product details by product identifier. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact documentation contains template placeholder language, so the public description may not fully describe operational behavior. <br>
Mitigation: Review the MCP tool names, server configuration, and expected cruise product data sources before deployment. <br>
Risk: Cruise product search and detail responses may influence purchasing or booking decisions. <br>
Mitigation: Validate product availability, pricing, and itinerary details against authoritative booking systems before commercial use. <br>
Risk: Security guidance recommends reviewing the skill's assumptions before relying on its recommendations for real decisions. <br>
Mitigation: Have a human reviewer confirm that the skill's outputs are appropriate for the intended workflow and decision context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sol713/skills/cruise-product) <br>
- [Publisher profile](https://clawhub.ai/user/sol713) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>
- [Model Context Protocol server schema](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [MCP tool responses, typically text or JSON returned from cruise product list, detail, and search tools.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses depend on the requested product filters, product identifiers, keywords, and the configured MCP endpoint.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter, server release metadata, server.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

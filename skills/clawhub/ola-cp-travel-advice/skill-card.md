## Description: <br>
Provides practical cruise travel advice, including preparation tips, best departure timing, and destination recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and travel-planning agents use this skill to request practical cruise preparation, timing, destination, and product-detail guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise-related requests and product identifiers are sent to the CruiseSkillBridge/olavacations remote MCP gateway. <br>
Mitigation: Avoid sending secrets, payment details, account credentials, or unnecessary personal information. <br>
Risk: Cruise planning guidance may be incomplete or unsuitable for a specific traveler, itinerary, or booking constraint. <br>
Mitigation: Review recommendations against current cruise operator policies and trusted travel sources before booking or purchase. <br>


## Reference(s): <br>
- [MCP server connection guide](artifact/references/mcp.md) <br>
- [MCP server manifest](artifact/server.json) <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/ola-cp-travel-advice) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Configuration] <br>
**Output Format:** [Natural-language guidance with MCP tool responses and setup snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use the product_info MCP tool to retrieve cruise product details by product identifier.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence; artifact frontmatter and server.json report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

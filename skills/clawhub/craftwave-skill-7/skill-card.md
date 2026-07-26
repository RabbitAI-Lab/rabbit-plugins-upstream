## Description: <br>
专为追求奢华的旅行者推荐高端邮轮体验，提供顶级设施与服务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External travelers, travel planners, and agents use this MCP skill to find luxury cruise options and filter cruise products by brand, departure city, destination, price, itinerary length, ship, and date. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise search inputs are sent through the CruiseSkillBridge/olavacations gateway and counted in usage statistics. <br>
Mitigation: Avoid secrets, payment details, passport data, and sensitive personal information unless the publisher provides adequate privacy and retention terms. <br>
Risk: Privacy documentation for the remote recommendation flow is incomplete. <br>
Mitigation: Review publisher privacy and retention terms before using the skill with customer or traveler data. <br>
Risk: Cruise recommendations or product filters may be incomplete, stale, or unsuitable for a specific booking. <br>
Mitigation: Verify pricing, availability, itinerary details, and booking requirements with the cruise provider before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/309441738/skills/craftwave-skill-7) <br>
- [MCP Server 接入](references/mcp.md) <br>
- [CruiseSkillBridge](https://cruiseskillbridge.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Markdown or JSON-derived text from MCP tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cruise search inputs are sent to a remote CruiseSkillBridge/olavacations gateway and may be counted in usage statistics.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter and server.json report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

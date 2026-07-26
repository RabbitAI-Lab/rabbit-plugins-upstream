## Description: <br>
Recommends cruise products based on user preferences and prior selections to help identify suitable sailing options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[309441738](https://clawhub.ai/user/309441738) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Travel shoppers, planners, and agents use this skill to search cruise products by keyword and request recommendations based on stated preferences and past choices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cruise search terms, preferences, and any history provided by the user are sent to an external remote MCP gateway. <br>
Mitigation: Share only the information needed for search or recommendation tasks, and avoid sensitive personal, financial, passport, or account details unless privacy, logging, retention, and data handling terms are documented. <br>
Risk: Cruise recommendations may be incomplete, stale, or unsuitable for final booking decisions. <br>
Mitigation: Treat results as discovery guidance and verify availability, pricing, itinerary details, and provider terms before booking. <br>


## Reference(s): <br>
- [MCP Server Access](references/mcp.md) <br>
- [Remote MCP Gateway](https://cruise-mcp.olavacations.com/api/gw/mcp/a1f27563-e74b-4840-9e18-c3c884eae9ce) <br>
- [ClawHub Skill Page](https://clawhub.ai/309441738/skills/ola-cp-recommendations) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, Configuration] <br>
**Output Format:** [Markdown or JSON responses from a remote MCP tool] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote streamable HTTP MCP gateway; no local persistence reported in the security evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

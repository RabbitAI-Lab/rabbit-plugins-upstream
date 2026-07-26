## Description: <br>
Search flights and discover travel destinations using the Jinko MCP server, including destination discovery by criteria and specific route flight comparison. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kevinjinko](https://clawhub.ai/user/kevinjinko) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and travel-planning agents use this skill to search flight options, compare routes, find lower-cost travel windows, and discover destinations based on criteria such as budget, climate, activities, cabin class, and trip length. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The broad travel-planning trigger may lead the agent to use Jinko's external MCP service for general travel discussions. <br>
Mitigation: Ask the user to confirm before searching, or keep non-search travel discussions explicit when tool use is not desired. <br>
Risk: Flight and destination searches require sending trip details to Jinko's MCP service. <br>
Mitigation: Share only the route, date, budget, cabin, locale, and currency details needed for the requested search. <br>


## Reference(s): <br>
- [Jinko MCP server](https://mcp.gojinko.com) <br>
- [ClawHub skill page](https://clawhub.ai/kevinjinko/skills/jinko-flight-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, API calls] <br>
**Output Format:** [Markdown or plain text with MCP tool calls and returned flight or destination results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a connected Jinko MCP server at https://mcp.gojinko.com; tool inputs include routes, dates, budgets, cabin class, locale, and currency when available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

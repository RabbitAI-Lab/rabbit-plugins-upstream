## Description: <br>
Use when the user asks to find flights, compare itineraries, search hidden-city routes, check cheapest dates, explore destinations, search hotels, plan a trip, or general flights / trip planning, grounded in official Skiplagged MCP results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wzs](https://clawhub.ai/user/wzs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and travel-planning agents use this skill to search Skiplagged flight, hotel, car, flexible-date, and destination-discovery results, then present concise options with booking links and caveats for hidden-city itineraries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel-search requests may send routes, dates, and preferences to Skiplagged's public service. <br>
Mitigation: Avoid unnecessary personal information and use the skill only for explicit flight, hotel, car, or flexible-date searches. <br>
Risk: Hidden-city itineraries can involve checked-bag constraints and missed-leg implications. <br>
Mitigation: Present clear caveats whenever hidden-city options appear and encourage users to confirm details through returned booking links. <br>
Risk: Flight prices and availability can change quickly. <br>
Mitigation: Treat returned results as point-in-time and prompt users to verify current details before booking. <br>


## Reference(s): <br>
- [Skiplagged Flights on ClawHub](https://clawhub.ai/wzs/skills/skiplagged-flights) <br>
- [wzs publisher profile](https://clawhub.ai/user/wzs) <br>
- [Skiplagged](https://skiplagged.com) <br>
- [Skiplagged MCP docs and privacy notes](https://skiplagged.github.io/mcp/) <br>
- [MCPorter CLI README](https://raw.githubusercontent.com/steipete/mcporter/main/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown or concise text with optional shell command examples and JSON MCP results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Top results are typically summarized as mobile-friendly bullet lists; prices and availability should be treated as point-in-time.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

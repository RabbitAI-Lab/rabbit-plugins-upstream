## Description: <br>
Live flight tracking and aviation data via FlightAware AeroAPI through MCP, including flight status, airport activity, schedules, aircraft ownership, and FlightAware alert management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure and use a FlightAware MCP server for live flight, airport, operator, aircraft, schedule, and alert workflows. It is useful when an agent needs to answer aviation status questions or manage FlightAware flight alerts through a user's AeroAPI account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a FlightAware AeroAPI key and queries may count against quota or billing. <br>
Mitigation: Confirm the key belongs to the intended account, avoid exposing it in logs or prompts, and use the documented cache settings to reduce repeated live-data calls. <br>
Risk: FlightAware alert create, update, and delete tools can change account alert settings. <br>
Mitigation: Use mutating alert tools only when the user explicitly intends the change and rely on the disclosed confirmation behavior before network-changing actions. <br>
Risk: Installation depends on an external npm package. <br>
Mitigation: Confirm the package and publisher are trusted before installation, consistent with the security guidance in the release evidence. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/flightaware-mcp) <br>
- [npm package @chrischall/flightaware-mcp](https://www.npmjs.com/package/@chrischall/flightaware-mcp) <br>
- [FlightAware AeroAPI Portal](https://www.flightaware.com/aeroapi/portal/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool results returned as text, structured data, or generated flight-map files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the user's FlightAware AeroAPI key; supports optional cache TTL and output directory environment variables.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

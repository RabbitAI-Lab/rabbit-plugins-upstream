## Description:

Live flight tracking and aviation data via FlightAware AeroAPI through MCP for flights, airports, schedules, aircraft ownership, and flight alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and aviation operations teams use this skill to query FlightAware AeroAPI through an MCP server for live flight status, airport boards, routes, schedules, aircraft ownership lookups, maps, and alert management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses the user's FlightAware AeroAPI key, and requests count against the user's FlightAware plan.

Mitigation: Install only when the user accepts FlightAware API usage and billing implications, and configure caching or usage limits appropriate to the plan.

Risk: Flight alert and webhook tools can change account settings when confirmed.

Mitigation: Review alert and webhook changes before setting confirm to true; rely on the dry-run preview for account-mutating actions.

Risk: Flight map PNGs may be written into the current working directory by default.

Mitigation: Set AEROAPI_OUTPUT_DIR to an expected directory before requesting map output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)
- [Source link listed in skill artifact](https://github.com/chrischall/flightaware-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Configuration, Shell commands, Files]

**Output Format:** [Markdown or structured text with MCP tool results, setup snippets, and optional PNG map files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user's FlightAware AeroAPI key; alert changes are confirm-gated and map output can be directed with AEROAPI_OUTPUT_DIR.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

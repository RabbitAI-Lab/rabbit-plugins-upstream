## Description:

Live flight tracking and aviation data via FlightAware AeroAPI through MCP for flight, airport, operator, aircraft, schedule, and alert workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and aviation users use this skill to connect an agent to FlightAware AeroAPI for live flight status, positions, routes, airport boards, weather, delays, schedules, aircraft ownership, and alert management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external npm MCP package that receives the user's FlightAware AeroAPI key.

Mitigation: Install it only after reviewing the package or source to the level required for your supply-chain assurance.

Risk: FlightAware alert tools can modify account state when confirmed.

Mitigation: Use the documented dry-run behavior first and provide explicit confirmation only for intended alert changes.

Risk: AeroAPI usage is billed or quota-limited per query.

Mitigation: Configure cache TTLs where appropriate and monitor usage against the selected FlightAware plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package @chrischall/flightaware-mcp](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return FlightAware API responses, compact or full views, and flight-map PNG files when the MCP server is configured.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

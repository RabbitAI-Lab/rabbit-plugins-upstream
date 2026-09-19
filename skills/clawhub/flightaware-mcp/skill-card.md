## Description:

Provides live flight tracking, airport, aircraft, schedule, weather, and alert-management access through FlightAware AeroAPI via an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users configure this skill when they want an agent to answer flight, airport, aircraft, schedule, weather, and FlightAware alert questions using their own AeroAPI key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running an untrusted MCP package could expose the user to code or behavior they did not intend to trust.

Mitigation: Verify that the @chrischall/flightaware-mcp package and source are trusted before installing or registering the MCP server.

Risk: FlightAware AeroAPI requests use the user's API key and may count against quota or bill the user's subscription.

Mitigation: Use an appropriate AeroAPI key, review FlightAware usage terms and billing, and use documented cache settings where suitable.

Risk: Alert management tools can create, update, delete, or change FlightAware alert endpoints.

Mitigation: Review dry-run previews carefully and only set confirmation fields when the requested account change is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package: @chrischall/flightaware-mcp](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP setup steps, FlightAware API usage guidance, and notes about MCP tools that can create flight-map PNG files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

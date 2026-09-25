## Description:

Live flight tracking and aviation data via FlightAware AeroAPI through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate a FlightAware MCP server for live flight status, aircraft, airport, schedule, route, position, map, and alert workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user's FlightAware AeroAPI key for live requests, which may consume subscription quota.

Mitigation: Configure the intended AeroAPI key only, monitor quota usage, and use the documented cache settings where appropriate.

Risk: Alert-management tools can change FlightAware account configuration.

Mitigation: Review alert creation, update, deletion, and endpoint-change prompts before approving them.

Risk: Installation depends on a third-party npm package and repository.

Mitigation: Verify that the npm package and repository match the trusted publisher before installing or running the MCP server.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)
- [flightaware-mcp source repository](https://github.com/chrischall/flightaware-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline JSON and shell code blocks; configured MCP tools return flight data, receipts, and optional PNG map files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a FlightAware AeroAPI key; live requests may count against the user's FlightAware quota.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

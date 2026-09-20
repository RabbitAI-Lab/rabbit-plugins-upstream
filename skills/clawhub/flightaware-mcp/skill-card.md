## Description:

Live flight tracking and aviation data via FlightAware AeroAPI through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and use a FlightAware MCP server for live flight status, routes, positions, airport boards, aircraft ownership, schedules, weather, delays, and confirm-gated flight alert management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AeroAPI key in MCP configuration.

Mitigation: Store the key only in local configuration or environment-managed secrets and avoid sharing generated MCP config with the key included.

Risk: FlightAware AeroAPI calls consume the user's subscription quota and may incur billing.

Mitigation: Use the documented caching settings where appropriate and review usage against the FlightAware plan before high-volume queries.

Risk: Alert tools can modify FlightAware alert settings when confirm is set to true.

Mitigation: Review the dry-run preview before using confirm: true for create, update, delete, or endpoint changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package: @chrischall/flightaware-mcp](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON and bash code blocks; MCP tool outputs return FlightAware response data and can write flight-map PNG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AeroAPI API key. Compact view strips media URLs by default, and alert writes are confirm-gated.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

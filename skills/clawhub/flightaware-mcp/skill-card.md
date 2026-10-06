## Description:

Connects an agent to FlightAware AeroAPI for live flight tracking, airport information, aircraft details, schedules, and flight alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers, aviation professionals, and developers use this skill to look up flights, airport activity, aircraft ownership, and schedules or manage FlightAware flight alerts through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted package or exposing an AeroAPI key could compromise the user's account.

Mitigation: Confirm the package is trusted before installation and use your own AeroAPI key securely.

Risk: Flight queries can consume paid AeroAPI quota.

Mitigation: Check the subscription quota and expected query volume before use.

Risk: Alert tools can create, change, or delete FlightAware alert settings.

Mitigation: Review proposed alert changes and confirm them before applying.

## Reference(s):

- [FlightAware MCP on ClawHub](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [FlightAware MCP npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [Text, JSON, Images, Configuration guidance]

**Output Format:** [MCP tool responses with flight and airport data, optional flight-map PNGs, and Markdown setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [AeroAPI key required; read responses default to compact media-stripped data, with full responses available.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

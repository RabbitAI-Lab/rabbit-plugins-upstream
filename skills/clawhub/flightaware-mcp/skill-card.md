## Description:

Live flight tracking and aviation data via FlightAware AeroAPI through MCP for flight, airport, operator, schedule, aircraft ownership, and alert workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect an agent to FlightAware AeroAPI for live flight status, position, route, airport board, schedule, aircraft owner, and alert management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses an unpinned third-party MCP package.

Mitigation: Pin @chrischall/flightaware-mcp to a specific reviewed version before installation.

Risk: The setup requires a billing-capable AeroAPI key in local MCP configuration.

Mitigation: Keep secret-bearing configuration out of source control and avoid storing the real key in a project .mcp.json file.

Risk: FlightAware AeroAPI requests count against quota and may be billed.

Mitigation: Monitor AeroAPI usage and use the documented cache TTL settings where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package @chrischall/flightaware-mcp](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Configuration]

**Output Format:** [Agent responses with compact or full AeroAPI payloads, setup JSON snippets, dry-run receipts for alert changes, and optional PNG flight maps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided AeroAPI key; requests count against FlightAware quota and may be billed.]

## Skill Version(s):

0.5.3 (source: server release evidence, created 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

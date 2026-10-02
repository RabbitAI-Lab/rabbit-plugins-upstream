## Description:

Connects an agent to FlightAware AeroAPI for live flight tracking, airport information, schedules, aircraft details, and flight alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to check flight status and position, inspect airport activity, look up aircraft and schedules, or manage FlightAware flight alerts using their own AeroAPI key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external package uses the user's AeroAPI key for live requests that may consume quota.

Mitigation: Verify the package before installing, protect the key, and monitor AeroAPI usage.

Risk: Alert-management tools can change account settings.

Mitigation: Review the proposed alert operation and confirm it only when intended.

Risk: A global MCP configuration could expose the connector across projects.

Mitigation: Use a project-local MCP configuration when narrower access is needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [FlightAware MCP npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, Shell commands, Image files]

**Output Format:** [Text or Markdown responses, MCP configuration examples, and optional PNG flight maps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flight data is returned from AeroAPI; optional maps may be saved to disk or returned inline.]

## Skill Version(s):

1.2.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

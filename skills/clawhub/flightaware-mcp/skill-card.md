## Description:

Connects agents to FlightAware AeroAPI for flight tracking, airport and aircraft information, schedules, and flight alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and aviation professionals use this skill to check flights, airport activity, aircraft details, schedules, and alerts through FlightAware AeroAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The AeroAPI key is shared with the MCP server.

Mitigation: Use a key you are comfortable exposing to this server.

Risk: AeroAPI queries may incur charges.

Mitigation: Check your subscription and expected query volume before using the tools.

Risk: Generated flight maps may be saved to a local output directory.

Mitigation: Choose an appropriate output directory and review saved files.

Risk: Alert changes modify the user's FlightAware account.

Mitigation: Review and confirm alert changes before applying them.

## Reference(s):

- [FlightAware MCP package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [Text and JSON; optional PNG flight maps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live data depends on the user's AeroAPI subscription; flight maps may be saved locally.]

## Skill Version(s):

1.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

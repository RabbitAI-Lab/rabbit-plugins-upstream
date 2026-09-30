## Description:

Connects an agent to FlightAware AeroAPI for flight tracking, airport and aircraft information, schedules, and flight alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can check live flight status, routes, airport activity, schedules, and aircraft ownership, and manage flight alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The AeroAPI key is stored in MCP configuration and used for billable requests.

Mitigation: Protect the key, review the package or linked source before installation, and monitor API usage and charges.

Risk: Creating, updating, or deleting flight alerts changes the user's account.

Mitigation: Review the alert-change preview and obtain user approval before confirming the write.

Risk: Flight-map output can write PNG files to the selected directory.

Mitigation: Choose an appropriate output directory and review file output before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)
- [flightaware-mcp npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [Source repository linked in skill documentation](https://github.com/chrischall/flightaware-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Configuration, Guidance, Images]

**Output Format:** [Markdown guidance and JSON responses; optional PNG flight maps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flight maps may be saved as files or returned inline.]

## Skill Version(s):

1.2.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description: <br>
Live flight tracking and aviation data via FlightAware AeroAPI through MCP for flight status, positions, routes, airport boards, schedules, aircraft ownership, and flight alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and operate a FlightAware MCP server for live flight tracking, airport status checks, aircraft and operator lookups, schedules, and alert management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AeroAPI credentials are stored in MCP configuration. <br>
Mitigation: Use an AeroAPI key suitable for local MCP configuration and avoid sharing configuration files that contain the key. <br>
Risk: FlightAware AeroAPI requests can consume quota or incur billing. <br>
Mitigation: Monitor FlightAware usage, use the documented cache settings where appropriate, and avoid unnecessary repeated live-data queries. <br>
Risk: Confirmed alert operations can modify the user's FlightAware account. <br>
Mitigation: Review dry-run previews and use confirm-gated alert changes only when the requested account change is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp) <br>
- [npm package @chrischall/flightaware-mcp](https://www.npmjs.com/package/@chrischall/flightaware-mcp) <br>
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a FlightAware AeroAPI key; API use counts against the user's FlightAware quota.] <br>

## Skill Version(s): <br>
0.3.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

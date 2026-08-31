## Description:

flightaware-mcp helps agents use FlightAware AeroAPI through MCP for live flight tracking, airport boards, routes, aircraft ownership, schedules, and flight-alert management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to answer flight-status, airport, route, aircraft, schedule, and alert-management questions through a configured FlightAware MCP server and their own AeroAPI key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses the user's FlightAware AeroAPI key and API calls can count against quota or billing.

Mitigation: Configure the key only in trusted MCP settings, monitor AeroAPI usage, and use caching or pinned package versions where repeatable behavior matters.

Risk: Alert-management tools can create, update, delete, or change alert webhook endpoints.

Mitigation: Review alert changes before confirmation and require explicit approval for account-changing operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe MCP tool calls and FlightAware API-backed results; some actions require a configured AeroAPI key and may affect account alerts.]

## Skill Version(s):

0.3.5 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

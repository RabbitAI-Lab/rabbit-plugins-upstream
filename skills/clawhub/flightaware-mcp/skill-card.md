## Description:

Provides live flight tracking, airport, aircraft, schedule, route, weather, and FlightAware alert access through a FlightAware AeroAPI MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure an agent for FlightAware AeroAPI-backed flight tracking, airport lookups, operator and aircraft information, schedules, and alert management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses mutable third-party MCP code installed through npx while handling a FlightAware AeroAPI key.

Mitigation: Review the npm package or declared source before use, pin a specific package version or commit, and keep the AeroAPI key out of shared project configuration.

Risk: The MCP server can make network requests and may return live aviation data or account alert receipts based on the user's AeroAPI subscription.

Mitigation: Run the server with only the local and network access it needs, confirm alert-changing operations before execution, and monitor AeroAPI usage against the account quota.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm Package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [Declared Source Link](https://github.com/chrischall/flightaware-mcp)
- [FlightAware AeroAPI Portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe MCP tool calls that return text, JSON-like AeroAPI responses, receipts, or flight-map PNG output depending on the selected server tool.]

## Skill Version(s):

0.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

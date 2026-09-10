## Description:

Live flight tracking and aviation data via FlightAware AeroAPI through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to track live flights, inspect flight status, routes, positions, airport boards, aircraft ownership, schedules, and FlightAware alert settings through an MCP server backed by FlightAware AeroAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: FlightAware AeroAPI requests use the user's AeroAPI key and may count against quota or billing.

Mitigation: Verify the configured AeroAPI key and expected request volume before use; use the documented cache TTL settings where appropriate.

Risk: Alert write tools can create, update, delete, or change FlightAware alert settings.

Mitigation: Use confirm:true only after reviewing the requested alert operation; otherwise rely on the dry-run preview behavior.

Risk: Full responses can expose upstream AeroAPI payloads, while compact responses only strip media URLs.

Mitigation: Choose compact responses for normal use and request full responses only when the complete upstream payload is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package: @chrischall/flightaware-mcp](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON configuration snippets and optional PNG flight map files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools default to compact responses that strip media URLs; full responses can return upstream AeroAPI payloads, and alert write tools require confirm:true for account-changing actions.]

## Skill Version(s):

0.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

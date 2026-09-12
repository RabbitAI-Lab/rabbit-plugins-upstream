## Description:

Live flight tracking and aviation data via FlightAware AeroAPI through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate the FlightAware MCP server for flight status, positions, routes, airport boards, schedules, aircraft ownership, and flight alert workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can run an unpinned third-party MCP package while sending requests authenticated with an AeroAPI key.

Mitigation: Review the package before installing and pin a reviewed version or commit in MCP configuration.

Risk: A real AeroAPI key placed in a project MCP config could be committed or shared.

Mitigation: Keep the key out of shared project files, use a restricted key with quota controls, and remove the MCP config when the integration is no longer needed.

Risk: FlightAware AeroAPI usage counts against the user's subscription quota and may incur per-query billing.

Mitigation: Use the documented cache TTL settings for repeated live-data and reference-data requests, and monitor quota usage on the FlightAware account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/flightaware-mcp)
- [npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live aviation data responses, flight-map PNG outputs, and dry-run receipts for confirm-gated alert changes.]

## Skill Version(s):

0.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

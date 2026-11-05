## Description:

Live flight tracking and aviation data via FlightAware AeroAPI through MCP. Use when the user asks to track a flight, look up a flight's status/position/route/track, see an airport's arrivals/departures/delays/weather, find flights for an airline, look up an aircraft's owner, get scheduled flights between dates, or manage FlightAware flight alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers, aviation enthusiasts, and developers use this skill to look up live flight, airport, airline, aircraft, and schedule information, and to manage FlightAware flight alerts through their AeroAPI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The AeroAPI key grants account access and is used for requests.

Mitigation: Store the key securely and avoid exposing it in prompts, logs, or shared configuration.

Risk: AeroAPI requests count against the user's subscription and may incur per-query charges.

Mitigation: Monitor query usage and confirm the account tier supports the requested endpoint.

Risk: Creating or changing flight alerts or delivery endpoints changes account state.

Mitigation: Review the proposed alert or endpoint change and approve it before confirming the write.

Risk: The skill depends on an external MCP package and server version.

Mitigation: Review and pin the external server version before use.

## Reference(s):

- [FlightAware AeroAPI portal](https://www.flightaware.com/aeroapi/portal/)
- [npm package](https://www.npmjs.com/package/@chrischall/flightaware-mcp)
- [Project repository linked by the skill](https://github.com/chrischall/flightaware-mcp)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, Images]

**Output Format:** [Flight and aviation data as text or JSON; flight maps as PNG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live AeroAPI results may be paginated; flight-map tools can save a PNG or return it inline.]

## Skill Version(s):

1.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

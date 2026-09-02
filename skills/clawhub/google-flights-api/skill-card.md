## Description:

Search Google Flights for a route and date as structured JSON, including price, airline, duration, stops, and leg details for round-trip, one-way, and multi-city itineraries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search routes, compare fares, airlines, durations, and stops, and retrieve structured flight results for itinerary planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight searches consume Scavio credits.

Mitigation: Confirm the search parameters before running requests and monitor credit balance.

Risk: The skill requires a third-party Scavio API key.

Mitigation: Store SCAVIO_API_KEY in the environment or a secret manager and keep it out of source control.

Risk: Returned prices, airlines, times, and durations may be stale or unavailable if the upstream flight service changes or fails.

Mitigation: Use only API-returned data, state the requested currency when quoting fares, and retry or adjust filters when the API returns errors or no flights.

## Reference(s):

- [Scavio Google Flights API documentation](https://scavio.dev/docs/google-flights)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/google-flights-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands, Python examples, and structured JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each API request costs one credit.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

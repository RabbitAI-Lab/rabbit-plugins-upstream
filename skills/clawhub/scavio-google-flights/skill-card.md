## Description:

Search Google Flights for a route and date as structured JSON with price, airline, duration, stops, and legs; supports round-trip, one-way, and multi-city searches with cabin, stops, and airline filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel-support agents use this skill to look up Google Flights results through Scavio for specific routes and dates, compare fares and itinerary details, and return only API-backed flight data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight search details are sent to Scavio when the API is called.

Mitigation: Tell users when their route, dates, passenger counts, and filters will be sent to Scavio, and avoid sending sensitive travel details unless needed.

Risk: Each API request consumes one Scavio credit.

Mitigation: Confirm required route and date parameters before calling the API, and avoid repeated calls when filters or dates are unclear.

Risk: The Scavio API key can be exposed if pasted into source code or shared transcripts.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and never include real keys in generated code.

Risk: Flight prices, schedules, and availability can be wrong if invented or quoted without context.

Mitigation: Report only API-returned data and include relevant context such as currency, dates, stops, and the time-sensitive nature of fares.

## Reference(s):

- [Scavio Google Flights documentation](https://scavio.dev/docs/google-flights)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/scavio-google-flights)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Code, Guidance]

**Output Format:** [Markdown guidance with inline shell and Python examples plus structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each Scavio API request costs one credit.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

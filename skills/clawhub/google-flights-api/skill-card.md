## Description:

Search Google Flights for route dates and return structured JSON with prices, airlines, durations, stops, and leg details, including round-trip, one-way, and multi-city options with cabin, stop, and airline filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent builders use this skill to search flight options for route and date inputs, compare fares and itineraries, and return flight details as structured JSON for travel planning workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight search details are sent to Scavio using the configured SCAVIO_API_KEY.

Mitigation: Avoid unnecessary personal information in search parameters and review Scavio's terms or privacy handling for sensitive travel plans.

Risk: Returned prices, airlines, times, and durations may be incorrect if the agent fabricates or extrapolates beyond API data.

Mitigation: Only report values returned by the API, state the requested currency when quoting fares, and ask the user to adjust search parameters when no flights are returned.

## Reference(s):

- [Scavio Google Flights Documentation](https://scavio.dev/docs/google-flights)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/google-flights-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [Structured JSON with concise Markdown guidance when explaining results or errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each flight search request uses one Scavio credit.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

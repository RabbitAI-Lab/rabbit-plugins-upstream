## Description:

Search Google Flights for a route and date as structured JSON, including price, airline, duration, stops, and flight legs for round-trip, one-way, and multi-city itineraries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel-planning agents use this skill to search and compare flight options by route, date, cabin, stops, airlines, price, duration, and itinerary legs through Scavio's Google Flights API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key, and misuse could expose credentials.

Mitigation: Store SCAVIO_API_KEY in environment or secret storage and do not place real keys in source code.

Risk: Each request costs 1 credit and can consume paid quota.

Mitigation: Confirm searches before execution, monitor remaining credits, and avoid unnecessary repeated calls.

Risk: Route, date, passenger, cabin, stop, and airline parameters are sent to Scavio's API.

Mitigation: Share only the travel details needed for the search and avoid including unrelated sensitive information.

Risk: Flight prices, schedules, and availability can change or be incomplete.

Mitigation: Return only API-provided fares and itineraries, state the requested currency, and avoid fabricating prices, airlines, times, or durations.

## Reference(s):

- [Scavio Google Flights API documentation](https://scavio.dev/docs/google-flights?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-flights-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-flights-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-flights-api)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell setup, Python request examples, and structured JSON response handling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. API requests cost 1 credit each and return structured flight data from Scavio's API.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Search Google Flights for a route and date as structured JSON, including price, airline, duration, stops, and leg details for round-trip, one-way, and multi-city itineraries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Travel-planning agents and developers use this skill to search and compare Google Flights itineraries by route, dates, cabin, stops, airlines, price, and duration. It returns structured flight data that can support fare comparison, itinerary planning, and travel workflow automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight search details are sent to Scavio's API.

Mitigation: Use the skill only for searches the user is comfortable sharing with Scavio.

Risk: Each API request uses one credit from the SCAVIO_API_KEY account.

Mitigation: Confirm intended searches before calling the API and monitor account credit usage.

Risk: The required SCAVIO_API_KEY could be exposed if handled carelessly.

Mitigation: Load the key from an environment variable or secret store and keep it out of source control.

## Reference(s):

- [Scavio Google Flights documentation](https://scavio.dev/docs/google-flights?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-flights-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-flights-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-flights-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples, Python code examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to call Scavio's Google Flights API and return only API-provided flight data.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

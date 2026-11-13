## Description:

Search one-way flight options by departure city, destination city, and date using Ctrip mobile results, then sort by price ascending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linger0](https://clawhub.ai/user/linger0)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to ask an agent for quick one-way flight lookups by origin, destination, and date. The agent can run the bundled CLI and return concise fare options with flight number, departure and arrival time, price, and transfer status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested route and travel date are sent to Ctrip for live flight results.

Mitigation: Use the skill only when the user is comfortable sharing the requested itinerary details with Ctrip.

Risk: Live flight results can fail or become incomplete if Ctrip is unreachable or changes the page data format.

Mitigation: Report script errors or zero-result responses plainly, and do not invent schedules, prices, or transfer details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linger0/skills/flight-search)
- [City code mapping](references/city_codes.json)
- [Ctrip mobile flight results endpoint](https://m.ctrip.com/html5/flight/{origin}-{destination}-day-{offset}.html)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Concise Chinese plain text or JSON from the bundled CLI, with agent-facing guidance for presenting results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are sorted by ascending price and should not invent missing prices or schedules.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Scavio Booking helps agents search Booking.com through Scavio for live hotel prices, full property details, rooms, rate plans, and guest review breakdowns in structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel-data teams use this skill to research accommodations, compare live hotel pricing and review signals, inspect individual Booking.com properties, and build rate-shopping or travel-research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party API provider for hotel research.

Mitigation: Install only when third-party API use is acceptable for the intended workflow.

Risk: Hotel searches require a SCAVIO_API_KEY and consume API credits.

Mitigation: Store SCAVIO_API_KEY as an environment secret and monitor credit usage.

Risk: Travel searches can include sensitive personal travel details.

Mitigation: Avoid sending personal travel details beyond what is needed for the search.

Risk: Live prices and availability can change and may reflect defaulted dates or currency if request parameters are incomplete.

Mitigation: Send explicit check-in and check-out dates plus currency, read echoed dates before quoting prices, and include the property URL for verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/booking-com-hotel-data)
- [Scavio Booking Search documentation](https://scavio.dev/docs/booking-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=booking-com-hotel-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=booking-com-hotel-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions and inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for Scavio Booking.com API requests and structured JSON hotel-data responses.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

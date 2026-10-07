## Description:

Research public StubHub and SeatGeek event calendars and resale-price snapshots for location, category, performer, and venue comparisons without purchasing tickets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, event planners, and other users compare public resale event schedules and price signals across StubHub and SeatGeek by location, category, performer, or venue. The skill supports research, not purchases or checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event searches, location coordinates, and an API key are sent to Crawlora.

Mitigation: Use the skill only if this data sharing is acceptable; protect the API key and limit location details to what the search needs.

Risk: Resale prices and availability are snapshots, not guaranteed inventory or final checkout totals.

Mitigation: Label prices as resale snapshots with source, currency, and observation time; do not present them as purchase offers or fee-inclusive totals.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/live-events-ticketing-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Dated Markdown comparison table with explanatory notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes provider and event ID, source URL, local event time, price meaning and currency, availability signal, and observation timestamp.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

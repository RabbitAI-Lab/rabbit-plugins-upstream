## Description:

Compares public Agoda and Expedia flight offers through Crawlora to build a sourced shortlist with matched itinerary criteria, prices, connections, and fare-condition caveats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning assistants use the skill to compare observed Agoda and Expedia flight offers and explain itinerary tradeoffs without treating search results as confirmed bookings or final fares.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flight-search details and a Crawlora API key are sent to Crawlora's API.

Mitigation: Use the skill only when comfortable sharing those details with Crawlora, and keep the API key private.

Risk: Search snapshots may not reflect final fares, baggage or refund terms, seat availability, or booking status.

Mitigation: Verify prices and conditions with the provider before making travel decisions or paying.

Risk: One-way offers and departing legs from round-trip searches may be mistaken for equivalent complete itineraries.

Mitigation: Label trip and price basis explicitly and do not present departing-leg results as completed round trips.

## Reference(s):

- [Flight itinerary comparison endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/flight-itinerary-comparison)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown comparison table and tradeoff brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source links, observation times, price basis, and unknown fare conditions.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

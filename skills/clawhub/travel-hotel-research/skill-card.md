## Description:

Researches hotels, flights, attractions, short-term rentals, and live events through the Crawlora API across Booking.com, Expedia, Agoda, TripAdvisor, Trip.com, Airbnb, and Ticketmaster, returning normalized JSON for comparison and review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research travel options and live events, compare prices and reviews, and retrieve normalized JSON for trip-planning or due-diligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel queries, dates, destinations, and POST bodies are sent to the third-party Crawlora API.

Mitigation: Avoid confidential personal details in search terms or request bodies, and install only when third-party API use is acceptable.

Risk: The skill requires a Crawlora API key for requests.

Mitigation: Store CRAWLORA_API_KEY in the environment and do not hardcode, pass, or commit the key.

Risk: The skill provides research data only and does not complete bookings or payments.

Mitigation: Treat returned travel and event data as research input and verify details before booking or purchase decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/travel-hotel-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, text]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; helper requests public travel, stay, attraction, review, and event data from Crawlora endpoints.]

## Skill Version(s):

1.0.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

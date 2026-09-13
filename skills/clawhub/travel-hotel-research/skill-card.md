## Description:

Researches hotels, flights, attractions, short-term rentals, and live events via the Crawlora API -- Booking.com, Expedia, Agoda, TripAdvisor, Trip.com, Airbnb, and Ticketmaster -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and compare travel options, reviews, attractions, live events, flights, and short-term rentals through Crawlora API-backed lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper uses a Crawlora API key and sends travel search details, dates, locations, and listing identifiers to Crawlora.

Mitigation: Use a limited Crawlora key, avoid shared or untrusted shell environments, and do not include sensitive personal information in requests.

Risk: ClawHub security evidence reports a credential-handling hardening gap in the curl helper.

Mitigation: Review the helper before deployment and consider patching curl invocation hardening before relying on it.

Risk: Some Expedia POST request-body details are documented as unconfirmed in the artifact.

Mitigation: Confirm current Expedia payload shapes in Crawlora documentation or the playground before using those endpoints for decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API requests may include travel searches, dates, locations, listing IDs, and similar request details.]

## Skill Version(s):

1.0.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

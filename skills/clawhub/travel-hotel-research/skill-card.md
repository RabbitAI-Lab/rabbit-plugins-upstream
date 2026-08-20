## Description:

Researches hotels, flights, attractions, short-term rentals, and live events via the Crawlora API - Booking.com, Expedia, Agoda, TripAdvisor, Trip.com, Airbnb, and Ticketmaster - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, travel researchers, and agent users use this skill to search and compare hotels, flights, attractions, short-term rentals, live events, reviews, and listing details across supported travel platforms through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel searches, dates, locations, listing IDs, and similar request parameters are sent to Crawlora and may reach underlying travel platforms.

Mitigation: Avoid secrets and unnecessary personal details in search terms; use only request data needed for the travel task.

Risk: A Crawlora API key is required and could be exposed if it is hardcoded or committed.

Mitigation: Keep CRAWLORA_API_KEY in the environment and do not place it in files, query parameters, or shared artifacts.

Risk: Some Expedia POST body field names are documented by the artifact as unconfirmed.

Mitigation: Confirm current Expedia request shapes in Crawlora documentation or the Crawlora playground before relying on those endpoints.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs)
- [Crawlora playground](https://crawlora.net/playground)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/travel-hotel-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in the CRAWLORA_API_KEY environment variable; API calls send request parameters to Crawlora.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

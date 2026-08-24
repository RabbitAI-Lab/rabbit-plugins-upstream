## Description:

Researches hotels, flights, attractions, short-term rentals, and live events via the Crawlora API - Booking.com, Expedia, Agoda, TripAdvisor, Trip.com, Airbnb, and Ticketmaster - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research and compare travel options, lodging, attractions, events, reviews, and related public travel data through documented Crawlora API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can be used as a broader authenticated Crawlora API client than the stated travel research purpose.

Mitigation: Review before installing, provide a Crawlora API key only when trusted, and manually limit usage to the documented travel endpoints.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora Documentation](https://crawlora.net/docs)
- [Crawlora Playground](https://crawlora.net/playground)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/travel-hotel-research)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API calls; responses are public travel and event data returned by the API.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

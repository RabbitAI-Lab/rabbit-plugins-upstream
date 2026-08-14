## Description:

Researches hotels, flights, attractions, short-term rentals, and live events through Crawlora endpoints for Booking.com, Expedia, Agoda, TripAdvisor, Trip.com, Airbnb, and Ticketmaster, returning JSON for comparison and review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and compare public travel, lodging, attraction, flight, event, Airbnb host, and listing information before making travel decisions. It supports research workflows and does not perform booking or payment actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Crawlora helper can call endpoints beyond the advertised travel scope.

Mitigation: Limit use to the documented travel, lodging, attraction, flight, Airbnb, and Ticketmaster endpoints before installation or agent execution.

Risk: Search terms and supplied JSON request bodies are sent to Crawlora.

Mitigation: Avoid sending secrets, sensitive personal data, or confidential itinerary details in Crawlora requests.

Risk: Some Expedia POST body field names are documented as unconfirmed.

Mitigation: Confirm Expedia request-body shapes in the Crawlora documentation or playground before relying on those endpoints.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/travel-hotel-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples; Crawlora API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests send search terms and provided JSON request bodies to Crawlora.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

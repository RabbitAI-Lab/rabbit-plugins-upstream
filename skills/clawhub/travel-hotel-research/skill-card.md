## Description:

Researches hotels, flights, attractions, short-term rentals, and live events via the Crawlora API across Booking.com, Expedia, Agoda, TripAdvisor, Trip.com, Airbnb, and Ticketmaster, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Travel researchers, trip planners, and agents use this skill to compare lodging, flights, attractions, events, and public review data across supported travel platforms. It helps gather structured travel options and due-diligence details without performing bookings or payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API helper can be redirected with CRAWLORA_API_BASE, which could expose the Crawlora API key and travel query data to an arbitrary server.

Mitigation: Use the skill only from a trusted shell, avoid setting CRAWLORA_API_BASE except for deliberate testing with non-production credentials, and rotate the key if it was used with an untrusted base URL.

Risk: Travel searches, dates, locations, listing IDs, and related queries are sent to Crawlora and may be forwarded to downstream travel providers.

Mitigation: Avoid sending sensitive personal travel details unless that disclosure is acceptable for the use case.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora Documentation](https://crawlora.net/docs)
- [Crawlora Playground](https://crawlora.net/playground)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/travel-hotel-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends travel searches, dates, locations, and listing IDs to Crawlora and possibly downstream travel providers.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

飞猪旅行 provides full-category travel search for hotels, flights, trains, attraction tickets, Marriott products, food, local transit, fast search, and itinerary planning using Fliggy and map-provider proxy services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to search Chinese travel products, compare prices and schedules, find restaurants, plan local transit, and draft itineraries. It returns informational results and booking links rather than completing purchases or payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel searches, locations, addresses, and route details are sent through publisher-controlled proxy services.

Mitigation: Avoid sensitive trip details unless the publisher discloses proxy logging, retention, and provider data-flow practices.

Risk: The map-provider proxy path is under-disclosed relative to the skill's travel-search description.

Mitigation: Review the AMap/Gaode proxy behavior before installation and disclose it to users who rely on food or local-transit results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/fliggy-travel)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text travel search results with prices, schedules, ratings, routes, and booking links when returned by the upstream service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns informational recommendations and links; it does not complete bookings or payments.]

## Skill Version(s):

1.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

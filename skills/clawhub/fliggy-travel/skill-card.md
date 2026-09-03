## Description:

飞猪旅行 supports travel search and planning across hotels, flights, trains, attraction tickets, Marriott hotels, food, local transport, and itinerary planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to search travel options and draft itineraries across hotels, flights, trains, attractions, food, local transport, and Marriott listings. It returns informational results and booking links; it does not place orders or process payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel plans, routes, addresses, dates, and hotel or flight searches are sent through the publisher's proxy service.

Mitigation: Review organizational data-sharing requirements before installation and avoid entering sensitive personal or business travel details unless that proxy use is acceptable.

Risk: Server security evidence flags hardcoded cloud proxy endpoints, a shared proxy token, and a scan-avoidance code comment.

Mitigation: Manually review the proxy behavior and token handling before deployment, and monitor for publisher updates that remove shared credentials or clarify the proxy trust model.

Risk: Travel prices, schedules, availability, and routes can change after the skill returns results.

Mitigation: Treat returned travel options as planning guidance and verify current terms, availability, and pricing on the linked provider page before booking.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/fliggy-travel)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and plain-text travel search results with prices, ratings, schedules, route details, itinerary suggestions, and booking links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are generated from remote travel and mapping proxy calls and may include time-sensitive availability or pricing.]

## Skill Version(s):

1.4.1 (source: server release evidence; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

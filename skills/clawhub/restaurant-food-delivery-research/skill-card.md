## Description:

Researches restaurants and grocery or food delivery through the Crawlora API, including Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search and menus, and Instacart grocery search, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research public restaurant reviews, reservation context, delivery menus, nearby food options, and grocery products through Crawlora endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant or grocery searches, addresses, coordinates, postal codes, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, prefer coarse location when exact address is unnecessary, and keep the API key in CRAWLORA_API_KEY rather than hardcoding or committing it.

Risk: Crawlora credit usage may accrue for successful API requests.

Mitigation: Monitor Crawlora credit consumption and keep requests focused on the documented restaurant, delivery, and grocery endpoints.

Risk: Location-scoped or store-scoped endpoint results can be incomplete or depend on upstream platform availability.

Mitigation: Provide the required location or store identifiers and verify important prices, availability, reservations, or store details before relying on them for decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/restaurant-food-delivery-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; many restaurant, delivery, and grocery endpoints require location, postal code, or store identifiers.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

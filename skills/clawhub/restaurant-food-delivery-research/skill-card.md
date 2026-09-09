## Description:

Researches restaurants and grocery/food delivery via the Crawlora API: Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search and menus, and Instacart grocery search, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to research restaurant reviews, reservation availability, delivery restaurant menus, and grocery/store search results for user-specified locations. It is useful for comparing food delivery options, checking menus and prices, and gathering public restaurant or grocery information as JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send authenticated requests to a broader Crawlora API surface than the restaurant-focused description suggests.

Mitigation: Review endpoints before installation and prefer a version that allowlists only the food-delivery and grocery endpoints needed for the deployment.

Risk: Restaurant, grocery, search, and location data is sent to Crawlora when the skill is used.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid sending sensitive or unnecessary location details.

Risk: Changing CRAWLORA_API_BASE could redirect API-key-authenticated traffic to an untrusted destination.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is fully trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/restaurant-food-delivery-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; many calls require latitude/longitude or postal code; no ordering or payment actions are performed.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

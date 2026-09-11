## Description:

Researches restaurants and grocery or food delivery via the Crawlora API, including Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search and menus, and Instacart grocery search, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research restaurant reviews, reservation availability, delivery options, menus, prices, and grocery items across supported Crawlora food and delivery providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant, grocery, delivery, and location queries are sent to Crawlora, and some workflows may include precise addresses or coordinates.

Mitigation: Share the least precise location that still answers the request and avoid precise home addresses unless required for the specific search.

Risk: The usable endpoint catalog is broader than the short description and includes many food, grocery, chain-menu, and delivery providers.

Mitigation: Review reference/endpoints.md and limit calls to provider routes that are relevant to the user's request.

Risk: The helper requires a Crawlora API key.

Mitigation: Provide the key only through CRAWLORA_API_KEY and do not hardcode, commit, or pass it in query parameters.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora Website](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/restaurant-food-delivery-research)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples; helper responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns public restaurant, menu, review, delivery, and grocery data through Crawlora API calls.]

## Skill Version(s):

1.0.16 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

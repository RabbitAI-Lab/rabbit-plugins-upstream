## Description:

Researches restaurants and grocery/food delivery via the Crawlora API - Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search/menus, and Instacart grocery search - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research restaurant reviews, menus, reservations, delivery availability, and grocery products across Crawlora-supported food platforms. It is suited for comparing restaurants or delivery options near a location and returning structured JSON for agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send authenticated requests to a broader set of Crawlora API paths than the food-delivery description implies.

Mitigation: Review and restrict allowed endpoint paths and HTTP methods to the declared Yelp, OpenTable, DoorDash, Uber Eats, and Instacart use cases before production use.

Risk: A Crawlora API key and location or address-like search data are sent to Crawlora.

Mitigation: Use only approved Crawlora credentials, avoid hardcoding secrets, and avoid submitting sensitive or unnecessary location details.

Risk: CRAWLORA_API_BASE can redirect production credentials to a different API base.

Mitigation: Pin the API base to the approved Crawlora endpoint or block overriding CRAWLORA_API_BASE in production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/restaurant-food-delivery-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs rely on Crawlora API responses and may include public restaurant, menu, review, reservation, delivery, grocery, and location-scoped data.]

## Skill Version(s):

1.0.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Researches restaurants and grocery/food delivery via the Crawlora API, including Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search and menus, and Instacart grocery search, returning clean JSON for restaurant, menu, delivery, and grocery research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research restaurant reviews, reservations, menus, nearby delivery options, and grocery product or store information through Crawlora endpoints. It is suited to location-aware restaurant and grocery lookup tasks that need structured JSON rather than page scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant, delivery, grocery, address, postal-code, and coordinate queries are sent to Crawlora and its upstream data sources.

Mitigation: Use a dedicated Crawlora API key, avoid unnecessarily precise home or work locations, and submit only the location detail needed for the task.

Risk: The supported provider list is broader than the short description and includes many restaurant, delivery, chain menu, and grocery endpoints.

Mitigation: Review reference/endpoints.md before use and restrict requests to the specific provider endpoints needed.

Risk: Public restaurant, menu, price, availability, and delivery data can be incomplete, location-scoped, or time-sensitive.

Mitigation: Treat returned data as research context and verify critical booking, ordering, pricing, or availability details before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/restaurant-food-delivery-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

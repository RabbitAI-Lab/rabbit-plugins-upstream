## Description:

Researches restaurants and grocery/food delivery via the Crawlora API - Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search/menus, and Instacart grocery search - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to research public restaurant reviews, menus, reservations, delivery availability, and grocery/store information across supported food platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the Crawlora API key and request parameters to Crawlora, including exact addresses, postal codes, coordinates, restaurant searches, or grocery queries supplied by the user.

Mitigation: Use coarse locations when exact delivery results are not needed, set CRAWLORA_API_KEY through the environment, and avoid hardcoding or committing the key.

Risk: The skill exposes a broad food, restaurant, delivery, and grocery endpoint catalog beyond the five platforms emphasized in the short description.

Mitigation: Review the endpoint reference before use and limit requests to the platforms and data categories needed for the task.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/restaurant-food-delivery-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and location inputs such as coordinates, postal codes, or addresses for many supported endpoints.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

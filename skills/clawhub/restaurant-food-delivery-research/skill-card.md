## Description:

Researches restaurants and grocery or food delivery via the Crawlora API, including Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search and menus, and Instacart grocery search, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare restaurant reviews, menus, reservations, delivery options, and grocery availability across supported public food platforms for a given location or store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call broader Crawlora API paths beyond the restaurant and delivery endpoints described by the skill.

Mitigation: Review requested paths before execution and restrict use to the documented food-related endpoints when a food-only workflow is required.

Risk: Lookup terms, coordinates, locations, and postal codes are sent to Crawlora.

Mitigation: Avoid submitting sensitive personal locations or private data; use coarse locations when they are sufficient for the task.

Risk: The skill requires a Crawlora API key.

Mitigation: Store the key only in CRAWLORA_API_KEY and do not hardcode it, pass it in URLs, or commit it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/restaurant-food-delivery-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from Crawlora]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends lookup inputs such as search terms, coordinates, locations, or postal codes to Crawlora.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

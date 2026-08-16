## Description:

Researches restaurants and grocery or food delivery through Crawlora API endpoints for Yelp reviews, OpenTable reservations, DoorDash and Uber Eats restaurant search and menus, and Instacart grocery search, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research restaurant reviews, menus, reservations, delivery options, and grocery availability across supported food platforms. It is suited for comparison, due diligence, and location-scoped food research workflows that return normalized JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send arbitrary requests to Crawlora, which is broader than the stated restaurant, delivery, and grocery research purpose.

Mitigation: Review or constrain artifact/scripts/crawlora.sh before deployment when the agent should be limited to the documented food and grocery endpoints.

Risk: Using the skill gives an agent access to a Crawlora API key and can send location, address, search, and JSON request data to Crawlora.

Mitigation: Use only approved data, keep CRAWLORA_API_KEY in the environment rather than files or prompts, and scope agent access to the minimum workflows needed.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/restaurant-food-delivery-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are raw JSON suitable for jq or downstream analysis.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

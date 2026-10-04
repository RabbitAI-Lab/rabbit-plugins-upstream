## Description:

Researches public restaurant reviews, reservations, delivery menus, and grocery listings through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare restaurants, reviews, reservations, delivery options, menus, and grocery products near a specified location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant searches, addresses, postal codes, and coordinates are shared with a third-party API.

Mitigation: Use the service only for user-directed research and avoid submitting unnecessary location details.

Risk: Exposure of the Crawlora API key could allow unauthorized use.

Mitigation: Keep the key in the environment; do not include it in prompts, URLs, or committed files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/restaurant-food-delivery-research)
- [Supported endpoints and parameters](reference/endpoints.md)
- [Crawlora API and key setup](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Location-scoped, public restaurant, delivery, and grocery data; no ordering or payments.]

## Skill Version(s):

1.0.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

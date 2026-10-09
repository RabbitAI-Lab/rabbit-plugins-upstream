## Description:

Researches restaurant reviews, reservations, delivery menus, and grocery products through the Crawlora API and returns structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers can compare nearby restaurants, reviews, menus, delivery options, and grocery availability across supported services. A Crawlora API key and location or store details are required for relevant searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant and grocery searches can expose precise addresses, coordinates, or postal codes to Crawlora and upstream data sources.

Mitigation: Use approximate locations where practical and avoid submitting sensitive address details.

Risk: The Crawlora API key may be disclosed if embedded in prompts, commands, or logs.

Mitigation: Keep CRAWLORA_API_KEY in the environment, scope it appropriately, and exclude it from logs and shared outputs.

Risk: The endpoint reference covers more services than the short skill description suggests.

Mitigation: Review the endpoint reference and allow only the services needed for the task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/restaurant-food-delivery-research)
- [Supported endpoints and parameters](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured JSON results with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public restaurant, menu, review, reservation-availability, and grocery data; no ordering or payments.]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

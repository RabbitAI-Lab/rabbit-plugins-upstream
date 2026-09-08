## Description:

Researches Costco products, categories, warehouse stock and availability, nearby warehouses, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Costco products, compare prices and ratings, check delivery or warehouse availability, browse categories, and retrieve product reviews through Crawlora.

### Deployment Geography for Use:

Global, with US-only delivery availability lookups.

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key and request data to an overridden API host.

Mitigation: Leave CRAWLORA_API_BASE unset or set it only to https://api.crawlora.net/api/v1 before running commands.

Risk: The bundled helper accepts arbitrary Crawlora paths beyond the documented Costco endpoints.

Mitigation: Use only the documented Costco GET endpoints in reference/endpoints.md unless a reviewer approves a broader API call.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/costco-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Costco availability checks require a US postal code and two-letter state code.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

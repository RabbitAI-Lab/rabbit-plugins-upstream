## Description:

Researches Walmart products, prices, sellers, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Walmart listings, compare product prices and availability, inspect sellers, and summarize review snapshots through normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send requests outside the stated Walmart workflow.

Mitigation: Limit use to /walmart/search, /walmart/product/{item_id}, and /walmart/product/{item_id}/reviews unless the destination and request are explicitly trusted.

Risk: The skill requires a Crawlora API key and makes external API calls.

Mitigation: Keep the API key in CRAWLORA_API_KEY, avoid hardcoding or committing it, and do not send sensitive data in request bodies or query parameters.

Risk: Changing CRAWLORA_API_BASE can redirect requests and credentials to a different service.

Mitigation: Leave CRAWLORA_API_BASE unset or set it only to a trusted Crawlora API endpoint.

## Reference(s):

- [Walmart endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/walmart-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Crawlora API key and public Walmart product, search, and review data.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

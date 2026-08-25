## Description:

Researches Zara's catalog, including category taxonomy, listings, product detail, keyword search, search suggestions, and nearby physical stores, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping assistants use this skill to browse Zara categories, search products, inspect product colors, sizes, stock, images, and find nearby Zara stores through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper is a generic Crawlora API client that can call unrelated routes and send arbitrary request bodies beyond the Zara-only purpose.

Mitigation: Limit use to the documented Zara endpoints, review commands before execution, and avoid sending sensitive personal data, unnecessary locations, or unrelated prompts through the helper.

Risk: The skill requires a Crawlora API key for API access.

Mitigation: Provide the key only through CRAWLORA_API_KEY and do not hardcode, commit, or pass it in query parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/zara-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [API calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for API access; Zara store lookup requires latitude and longitude.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

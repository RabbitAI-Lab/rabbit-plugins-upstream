## Description:

Researches Zara's catalog - category taxonomy, category listings, product detail, keyword search, search suggestions, and nearby physical stores - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping research agents use this skill to browse Zara categories, search products, inspect product details, compare colors and sizes, and find nearby stores through normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper script can make broader Crawlora requests than the Zara-only purpose describes.

Mitigation: Review requested paths before execution and restrict normal use to the documented Zara endpoints.

Risk: Search terms, coordinates, and other request values are sent to the Crawlora API.

Mitigation: Use only non-sensitive queries and location coordinates, and do not pass private prompts, account data, or internal documents.

Risk: The Crawlora API key is required for requests.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid committing it, and prefer a scoped or disposable key where possible.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/zara-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns normalized public Zara catalog and store data through the Crawlora API.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Researches Lululemon catalog categories, listings, product details, outfit recommendations, reviews, and store locations through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to browse Lululemon categories, inspect product pricing, sizing, availability and reviews, discover styled outfit recommendations, and locate stores without scraping storefront HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper is broader than the Lululemon research purpose and can send arbitrary API paths and payloads with the user's Crawlora key.

Mitigation: Use the helper only for the documented /lululemon/* GET endpoints and review commands before execution.

Risk: Requests may send unintended or sensitive data to Crawlora and consume Crawlora credits.

Mitigation: Avoid passing sensitive text in request bodies, keep the API key in CRAWLORA_API_KEY, and monitor usage for unexpected credit consumption.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/lululemon-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; documented Lululemon endpoints return normalized JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

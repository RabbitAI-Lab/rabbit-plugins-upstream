## Description:

Researches secondhand, resale, and handmade marketplaces via the Crawlora API, including Poshmark, Etsy, Vinted, StockX, Mercari, Depop, and Whatnot, and returns clean JSON for listing, seller, shop, and resale price research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and compare public resale, secondhand, streetwear, sneaker, livestream, and handmade marketplace listings. It helps check seller or shop storefronts, inspect item details, and gather market price signals through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, item queries, and seller or shop identifiers are sent to Crawlora.

Mitigation: Avoid sensitive or private search terms and use the skill only for public marketplace research.

Risk: The helper can send the Crawlora API key with arbitrary paths and can use CRAWLORA_API_BASE if that environment variable is set.

Mitigation: Use a limited Crawlora key, review requested endpoints before execution, and run only in environments where CRAWLORA_API_BASE is controlled by trusted configuration.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/resale-secondhand-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API requests with CRAWLORA_API_KEY; responses are normalized JSON from public marketplace data.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

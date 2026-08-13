## Description:

Researches secondhand, resale, and handmade marketplaces via the Crawlora API across Poshmark, Etsy, Vinted, StockX, Mercari, Depop, and Whatnot, returning clean JSON for listing, seller, shop, and price research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and compare public resale marketplace listings, inspect seller or shop storefronts, check sneaker and streetwear resale prices, and research handmade or vintage goods through documented Crawlora API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shell helper can call arbitrary Crawlora API paths, including paths outside the documented resale marketplace scope.

Mitigation: Use the helper only with the documented Poshmark, Etsy, Vinted, StockX, Mercari, Depop, and Whatnot endpoints in reference/endpoints.md.

Risk: Marketplace search terms, seller or shop names, listing IDs, and filters are sent to Crawlora with the user's API key.

Mitigation: Avoid personal, confidential, secret, or sensitive data in query strings and JSON bodies, and keep CRAWLORA_API_KEY in the environment rather than in committed files or URLs.

Risk: The helper script contains unrelated example API paths that may broaden perceived scope.

Mitigation: Treat artifact examples outside the resale endpoints as non-scope examples and rely on the skill instructions and endpoint reference for supported use.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/resale-secondhand-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API requests; public marketplace data only.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

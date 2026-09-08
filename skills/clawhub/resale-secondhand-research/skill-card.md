## Description:

Researches secondhand, resale, and handmade marketplaces through the Crawlora API, returning normalized JSON for listings, sellers, shops, sneaker resale prices, and live shopping research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to query public marketplace listing, seller, shop, and resale-price data across supported resale and handmade marketplaces through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the user's Crawlora API key to arbitrary API paths, methods, and an environment-overridden API host.

Mitigation: Use a scoped or low-risk Crawlora key, run the helper only in trusted shell environments, keep CRAWLORA_API_BASE unset unless reviewed, and prefer a restricted helper for production use.

Risk: Marketplace research outputs may influence purchasing or seller-vetting decisions while reflecting only public data available through Crawlora at request time.

Mitigation: Treat outputs as research inputs and verify listings, sellers, prices, and availability directly on the relevant marketplace before acting.

Risk: The skill depends on live Crawlora API access, valid credentials, account credits, and endpoint-specific parameters such as required StockX and Whatnot categories.

Mitigation: Confirm CRAWLORA_API_KEY is configured, monitor API credits and failures, and consult the endpoint reference for required parameters before issuing calls.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/resale-secondhand-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live API calls; outputs are based on public marketplace data returned by Crawlora.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

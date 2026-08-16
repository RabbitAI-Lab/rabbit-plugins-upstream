## Description:

Researches products, prices, brands, and categories on Zalando using the Crawlora API, returning clean JSON for product search, category browsing, autocomplete, product lookup, and storefront market resolution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and shopping research agents use this skill to retrieve Zalando product, price, brand, category, SKU, autocomplete, and storefront data through Crawlora instead of scraping Zalando pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send API-keyed requests to a configurable external endpoint.

Mitigation: Keep CRAWLORA_API_BASE unset unless the replacement endpoint is intentionally trusted, and use only a Crawlora API key suitable for this local helper.

Risk: The helper script is broader than the Zalando-focused skill purpose.

Mitigation: Restrict normal use to the documented Zalando endpoints and review generated commands before execution.

Risk: Requests may include product queries or other user-provided data sent to Crawlora.

Mitigation: Avoid passing sensitive, private, or unrelated data through the script.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/zalando-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Crawlora API key in CRAWLORA_API_KEY; Zalando product, search, category, and suggest calls require an explicit market code.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

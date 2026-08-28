## Description:

Researches products, prices, brands, and categories on Zalando using the Crawlora API and returns clean JSON for product search, category browse, autocomplete, product detail, and market lookup tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce analysts use this skill to research public Zalando catalog data, compare prices, resolve storefront markets, inspect products by SKU, and browse market-specific categories through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API endpoints beyond the documented Zalando paths while using the user's Crawlora API key.

Mitigation: Review the requested path before execution and restrict routine use to /zalando/* endpoints unless a generic Crawlora API call is intentionally approved.

Risk: Using the skill sends Zalando queries and the Crawlora API key to Crawlora.

Mitigation: Use only when that data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode, commit, or pass the key in query parameters.

Risk: Search and category results are limited to the first page, which can make product or price comparisons incomplete.

Mitigation: Disclose the first-page limitation in analysis and avoid presenting results as exhaustive.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns normalized public Zalando catalog data; search and category endpoints expose only the first result page.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

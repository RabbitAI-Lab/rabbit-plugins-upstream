## Description:

Researches Old Navy's catalog and Gap Inc. sibling storefronts (Gap, Banana Republic, Athleta) for categories, products, colors, sizes, pickup availability, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to answer product discovery, category browsing, local pickup availability, nearest-store, and review-summary requests for Old Navy, Gap, Banana Republic, and Athleta without scraping storefront pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send authenticated requests beyond the documented Old Navy and Gap-family endpoints.

Mitigation: Review commands before execution and restrict use to the documented storefront paths.

Risk: A changed CRAWLORA_API_BASE could send the Crawlora API key to a custom host.

Mitigation: Keep CRAWLORA_API_BASE unset or pinned to https://api.crawlora.net/api/v1 in trusted environments.

Risk: Live product search results may be best-effort and can include recommended results instead of exact keyword matches.

Mitigation: Validate returned product names, categories, and variants before making recommendations.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live API calls; helper output is raw JSON suitable for jq or agent summarization.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

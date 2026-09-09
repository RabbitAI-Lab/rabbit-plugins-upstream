## Description:

Researches H&M's catalog - storefront categories, product listings, product detail, free-text search, and nearby physical stores - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to browse H&M categories, search product listings, inspect product details such as colors, sizes, stock, and reviews, and find nearby H&M stores through Crawlora's normalized API instead of scraping hm.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can use the user's Crawlora API key for arbitrary Crawlora paths, methods, request bodies, or an overridden API base.

Mitigation: Review commands before execution, keep requests scoped to the documented /hm endpoints, avoid setting CRAWLORA_API_BASE unless the target is trusted, and rotate the API key if it may have been exposed.

## Reference(s):

- [hm-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; uses public H&M catalog and store data exposed through Crawlora.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

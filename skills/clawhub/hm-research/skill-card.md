## Description:

Researches H&M's catalog, including storefront categories, product listings, product detail, free-text search, and nearby physical stores, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping researchers use this skill to browse or search H&M products, compare product details such as price, color, stock, and reviews, and find nearby stores through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: H&M search terms, product IDs, and optional location queries are sent to Crawlora.

Mitigation: Use the skill only for queries you are comfortable sharing with Crawlora, and avoid sensitive or unnecessary location inputs.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed in URLs.

Mitigation: Store CRAWLORA_API_KEY in environment-secret storage and keep it out of source files, logs, and query parameters.

Risk: Changing CRAWLORA_API_BASE can redirect requests to an unintended host.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination host is intentionally trusted.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; optional CRAWLORA_API_BASE changes the API destination.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

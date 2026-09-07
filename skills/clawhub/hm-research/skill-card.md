## Description:

Researches H&M catalog categories, listings, product detail, free-text search, and nearby stores through the Crawlora API, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, shopping researchers, and agents use this skill to browse H&M categories, search products, compare product detail, review size and color availability, and find nearby H&M stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key and request data could be sent outside the stated H&M-only scope through the generic API helper or an untrusted API base override.

Mitigation: Keep CRAWLORA_API_KEY only in the environment, review commands before execution, and avoid CRAWLORA_API_BASE overrides unless the destination is trusted.

Risk: H&M search terms, product IDs, and store-location queries are sent to Crawlora during live API use.

Mitigation: Use the skill only when sharing those query details with Crawlora is acceptable, and avoid precise coordinates unless they are needed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live API calls.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

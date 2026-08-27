## Description:

Researches Target catalog categories, products, filters, prices, questions, and reviews through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping researchers use this skill to search or browse Target catalog data, compare product price and availability by store, and summarize product detail, Q&A, and reviews without scraping target.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora API paths, not only Target endpoints.

Mitigation: Keep requests limited to the documented /target endpoints and review generated commands before execution.

Risk: The skill requires a Crawlora API key.

Mitigation: Provide the key only through CRAWLORA_API_KEY; do not hardcode, commit, or pass it as a query parameter.

Risk: Target catalog, price, availability, Q&A, and review data can be paginated, store-specific, or change over time.

Mitigation: Check pagination, store_id, and TCIN inputs before relying on results for purchasing decisions or recommendations.

## Reference(s):

- [Target endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results are paginated, and store_id affects pricing and availability.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

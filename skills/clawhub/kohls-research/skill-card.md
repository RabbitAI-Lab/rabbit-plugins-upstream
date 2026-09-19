## Description:

Researches Kohl's catalog categories, product reviews, nearby stores, and search suggestions through the Crawlora API as normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to browse Kohl's category taxonomy, summarize products and reviews, find nearby stores, and collect typeahead suggestions without scraping Kohls.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends category, suggestion, review, and store-location queries to Crawlora as a third-party service.

Mitigation: Use it only when third-party Crawlora processing is acceptable, and avoid including secrets or unnecessary personal details in requests.

Risk: The helper requires a Crawlora API key.

Mitigation: Store the key in CRAWLORA_API_KEY, use a dedicated Crawlora key, and do not hardcode or commit credentials.

Risk: Product discovery is limited to documented Kohl's category browsing and typeahead suggestions.

Mitigation: Start from known category values or returned facet categories, and do not rely on unsupported product search or single-product lookup behavior.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/kohls-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Kohl's catalog, review, store, and suggestion data through documented GET endpoints.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

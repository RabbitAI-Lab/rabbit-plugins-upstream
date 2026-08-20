## Description:

Researches Walmart products, prices, sellers, and reviews using the Crawlora API, returning clean JSON for product discovery, price comparison, listing tracking, and review pulls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to search Walmart listings, compare current product prices and sellers, retrieve product details, and summarize review snapshots through Crawlora instead of scraping Walmart pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Walmart search terms, item IDs, and review requests are sent to Crawlora with the configured Crawlora API key.

Mitigation: Avoid private data in queries and request bodies, keep the API key in CRAWLORA_API_KEY, and do not hardcode or commit the key.

Risk: The skill is intended for documented Walmart endpoints, while the helper script can call a broader Crawlora API path if directed.

Mitigation: Use the documented Walmart endpoints unless broader Crawlora API access is intentional and reviewed.

Risk: Walmart review results are a single on-page snapshot rather than a complete paginated review history.

Mitigation: Treat review summaries as snapshot evidence and avoid presenting them as exhaustive review analysis.

## Reference(s):

- [walmart-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends Walmart queries, item IDs, and review requests to Crawlora.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

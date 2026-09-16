## Description:

Researches Ulta Beauty's catalog — categories, products, shades, questions, reviews, and nearby stores — using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Ulta Beauty products, categories, shades, customer Q&A, reviews, and nearby store locations through Crawlora instead of scraping Ulta pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and location searches are sent to Crawlora as a third-party API provider.

Mitigation: Keep CRAWLORA_API_KEY secret, review sensitive queries before use, and prefer zip code or city searches when exact address precision is unnecessary.

Risk: Unknown categories, products, searches, or locations can return empty results or 404 responses.

Mitigation: Check response status, pagination, and empty-result cases before relying on the output for recommendations.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands that return normalized JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be paginated; API access requires CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

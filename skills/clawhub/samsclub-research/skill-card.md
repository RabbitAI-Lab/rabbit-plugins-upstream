## Description:

Researches Sam's Club's catalog, including department and category navigation, product grids, product details with pricing, availability and ratings, related-item shelves, and curated content pages, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping research agents use this skill to browse Sam's Club departments, inspect category product grids, retrieve product pricing, availability and ratings, and compare related products without scraping samsclub.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key and Sam's Club lookup requests are sent to Crawlora, and the helper script can use an environment-controlled API base.

Mitigation: Use the skill only when this third-party data flow is acceptable, keep the API base pinned to https://api.crawlora.net/api/v1, avoid setting CRAWLORA_API_BASE, and restrict calls to the documented Sam's Club GET endpoints.

## Reference(s):

- [Sam's Club endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON returned from Crawlora API requests, with Markdown guidance and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Sam's Club catalog endpoints through Crawlora.]

## Skill Version(s):

1.0.6 (source: evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

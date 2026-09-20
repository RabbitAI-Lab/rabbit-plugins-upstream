## Description:

Researches Nike catalog categories, search results, product details, colorways, reviews, availability, recommendations, and nearby stores through the Crawlora API, returning normalized JSON instead of scraping nike.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to research Nike products, categories, reviews, availability, recommendations, and store locations via a scoped Crawlora API helper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nike lookup queries, product identifiers, and store-search coordinates are sent to Crawlora.

Mitigation: Use the skill only when sharing that research data with Crawlora is acceptable.

Risk: The Crawlora API key could be exposed if committed or passed through unsafe command usage.

Mitigation: Keep CRAWLORA_API_KEY as a secret environment variable and use the bundled helper for documented Nike endpoints.

## Reference(s):

- [nike-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and documented GET-only Nike endpoints.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

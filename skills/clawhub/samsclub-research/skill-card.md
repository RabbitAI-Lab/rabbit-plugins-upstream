## Description:

Researches Sam's Club catalog departments, categories, product details, related-item shelves, and curated content pages through the Crawlora API, returning normalized JSON instead of scraping samsclub.com directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to browse public Sam's Club departments and categories, retrieve product price, availability, rating, and item data, and inspect related products or curated landing pages through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Sam's Club lookup requests and the Crawlora API key to Crawlora.

Mitigation: Install only when that data flow is acceptable; keep CRAWLORA_API_KEY in the environment and never hardcode or commit it.

Risk: Endpoint parameters may disclose sensitive private data if a user supplies it.

Mitigation: Use the skill only for public Sam's Club catalog identifiers and avoid submitting sensitive private data as endpoint parameters.

Risk: Catalog results can vary by upstream availability and endpoint behavior, including zero-result, 404, or fallback related-item responses for unknown IDs.

Mitigation: Check response status and contents before relying on returned product, availability, or related-item data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/samsclub-research)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands; API responses are raw JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment; uses documented GET-only Crawlora routes for public Sam's Club catalog data.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Researches Sam's Club's catalog - department/category navigation, category product grids, product detail with pricing/availability/ratings, related-item shelves, and curated content pages - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse Sam's Club departments and categories, inspect product pricing, availability, ratings, related items, and curated content pages through Crawlora API responses instead of scraping samsclub.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can make authenticated Crawlora requests beyond the documented read-only Sam's Club lookup use.

Mitigation: Review the helper before installation and use only documented Sam's Club GET endpoints for catalog, category, product, related-item, and content lookups.

Risk: Crawlora API calls can consume third-party API quota and use a credential tied to the user's Crawlora account.

Mitigation: Use a Crawlora API key intended for these lookups, keep it in CRAWLORA_API_KEY, and avoid placing sensitive text in request bodies.

## Reference(s):

- [samsclub-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/samsclub-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns normalized JSON from Crawlora API calls.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

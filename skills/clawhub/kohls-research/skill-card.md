## Description:

Researches Kohl's catalog by browsing category taxonomy, pulling product reviews by web_id, finding nearby stores, and returning search-box typeahead suggestions through the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Kohl's catalog data, product reviews, store locations, and typeahead suggestions through Crawlora instead of scraping Kohls.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kohl's-related search terms, product IDs, review requests, and store-location searches to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, and prefer city or ZIP instead of a full home address for store lookups.

Risk: The skill depends on a Crawlora API key.

Mitigation: Keep the key in CRAWLORA_API_KEY and avoid hardcoding, committing, or passing it in query parameters.

## Reference(s):

- [Kohl's endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/kohls-research)

## Skill Output:

**Output Type(s):** [JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; product discovery is limited to category taxonomy and typeahead suggestions.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

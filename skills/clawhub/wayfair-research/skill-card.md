## Description:

Browses Wayfair categories and retrieves product grids or detailed product information, including price, brand, stock, rating, variants, and images, as clean JSON through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse public Wayfair categories, retrieve product grids, and look up W-prefixed product details. It supports product comparison workflows that need price, stock status, ratings, variants, images, and category pagination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends product research requests to Crawlora, a third-party API provider.

Mitigation: Use it only for public Wayfair product research and avoid sending private or unrelated data through the helper.

Risk: The helper requires a Crawlora API key.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode, commit, or pass it in URLs.

Risk: Category discovery is best-effort and does not include full-text search or review retrieval.

Mitigation: Use category pagination, rely on W-prefixed product IDs for detail lookups, and verify conclusions against the returned JSON fields.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/wayfair-research)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results are paginated and limited to category browsing and product detail.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

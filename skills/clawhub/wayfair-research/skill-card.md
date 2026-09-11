## Description:

Browses Wayfair category taxonomy and retrieves category product grids and product details through the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer Wayfair shopping and research requests by browsing category listings and retrieving public product details such as price, brand, stock status, ratings, variants, and images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper includes under-documented POST request-body support for caller-supplied text even though the documented Wayfair endpoints are GET-only.

Mitigation: Use the skill only for public Wayfair category and product lookups; do not place secrets, private prompts, environment values, or personal data in requests; prefer a helper version that rejects POST and -d and enforces documented GET-only schemas.

## Reference(s):

- [Wayfair endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/wayfair-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; responses are paginated and limited to documented Wayfair category and product endpoints.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

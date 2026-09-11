## Description:

Researches H&M's catalog, storefront categories, product listings, product detail, free-text search, and nearby physical stores using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse or search H&M catalog data, compare product details such as colors, sizes, pricing, reviews, and stock, and find nearby physical H&M stores without scraping hm.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends H&M lookup queries to Crawlora.

Mitigation: Use an appropriate Crawlora key, keep it in CRAWLORA_API_KEY, and avoid sensitive lookup or location queries.

Risk: Security evidence says the helper can send authenticated POST requests beyond the documented read-only API shape.

Mitigation: Review before execution and restrict use to documented H&M catalog routes until the helper is tightened to GET-only documented routes and numeric product IDs.

## Reference(s):

- [hm-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub hm-research skill page](https://clawhub.ai/crawlora-org/skills/hm-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns normalized JSON from Crawlora H&M endpoints.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

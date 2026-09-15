## Description:

Researches H&M's catalog - storefront categories, product listings, product detail, free-text search, and nearby physical stores - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse, search, and inspect public H&M product, category, review, stock, and store-location data through Crawlora instead of scraping hm.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-directed H&M search terms, product IDs, category choices, and store-location lookups are sent to Crawlora using the configured API key.

Mitigation: Keep the key in CRAWLORA_API_KEY, do not hardcode or commit it, and avoid entering sensitive personal information into search or store-location queries.

Risk: H&M catalog and store data can be incomplete, unavailable, paginated, or return empty results for unsupported categories, products, pages, or locations.

Mitigation: Use the documented endpoint behavior, check empty and 404 responses, and avoid presenting price, stock, review, or store availability as guaranteed.

## Reference(s):

- [hm-research endpoint reference](reference/endpoints.md)
- [hm-research ClawHub release](https://clawhub.ai/crawlora-org/skills/hm-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and documented Crawlora H&M endpoints; the helper prints raw JSON responses.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

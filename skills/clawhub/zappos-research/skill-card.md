## Description:

Researches Zappos's footwear and apparel catalog - the brand directory, product search, and product detail (pricing, images, ratings, fit feedback, color variants) - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to browse Zappos brands, search footwear and apparel, and retrieve product pricing, ratings, images, fit feedback, and color variants through Crawlora instead of scraping Zappos pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends Zappos search terms, brand identifiers, product identifiers, and the Crawlora API key to Crawlora.

Mitigation: Use approved queries and a managed Crawlora API key, and review Crawlora billing and terms before installation.

Risk: Catalog, pricing, ratings, and fit feedback can change over time and may not include every customer review.

Mitigation: Treat returned JSON as current catalog evidence for the requested lookup and re-query Crawlora before making purchase or recommendation decisions.

## Reference(s):

- [Zappos endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Zappos catalog data via Crawlora and requires CRAWLORA_API_KEY for API calls.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

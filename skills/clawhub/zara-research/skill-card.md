## Description:

Researches Zara's catalog - category taxonomy, category listings, product detail, keyword search, search suggestions, and nearby physical stores - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse Zara categories, search products, inspect product colors, sizes, stock, and images, and find nearby stores through Crawlora instead of scraping Zara directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends user-directed Zara search terms and store-location coordinates to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep CRAWLORA_API_KEY private, and review Crawlora and Zara terms for the intended use.

Risk: Catalog lookup results can reflect best-effort search behavior, including broader recommendations for obscure queries.

Mitigation: Treat product matches as candidates and verify important product, stock, and store details before relying on them.

## Reference(s):

- [Zara Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/zara-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns normalized public Zara catalog and store data from Crawlora.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

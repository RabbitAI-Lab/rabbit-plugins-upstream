## Description:

Researches Sam's Club catalog across departments, category product grids, product details, related items, and curated content pages through the Crawlora API, returning normalized JSON instead of scraped HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, shoppers, and developers use this skill to browse public Sam's Club departments and categories, check product price, availability, and rating details, inspect related products, and review curated content pages through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and the Sam's Club category, product, and content requests made through the skill.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid private or unrelated data in requests, and use the skill only for public Sam's Club catalog research.

Risk: Catalog values such as price, availability, ratings, and related products can change or differ by context.

Mitigation: Treat returned JSON as current lookup data and verify important commercial decisions against the relevant Sam's Club page or business process.

Risk: Unknown or stale identifiers have endpoint-specific behavior, including zero-result category responses, content 404s, and generic related-product shelves.

Mitigation: Handle empty results, 404 responses, and fallback related-item shelves explicitly before presenting conclusions.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/samsclub-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and documented Sam's Club endpoints; requests return public catalog data.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

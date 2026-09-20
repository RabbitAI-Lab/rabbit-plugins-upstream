## Description:

Researches Wish's marketplace categories, product search, product detail, related items, and reviews using the Crawlora API, returning clean JSON for comparison and product due diligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to search Wish products, inspect product details, compare prices and ratings, retrieve related items, and summarize customer reviews through Crawlora's normalized API rather than scraping Wish pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wish search terms, product IDs, and the Crawlora API key are sent to Crawlora when the helper is used.

Mitigation: Use the skill only when that disclosure is acceptable, keep CRAWLORA_API_KEY in the environment, and do not use it for private or account-specific Wish data.

Risk: Marketplace data such as price, availability, rating, inventory, and reviews can change or be incomplete.

Mitigation: Treat returned JSON as current research input and verify important purchase or recommendation decisions against the latest available product data.

Risk: The skill accesses public Wish marketplace data through a third-party API.

Mitigation: Use it for public product and category research only and follow the applicable Wish and Crawlora terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/wish-research)
- [Wish endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment and uses bounded GET routes for Wish categories, search, suggestions, product detail, related items, and reviews.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

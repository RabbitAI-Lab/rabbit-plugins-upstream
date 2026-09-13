## Description:

Researches Walmart products, prices, sellers, and reviews using the Crawlora API, returning clean JSON. Use when the user asks to find a product, compare prices, track listings, or pull reviews on Walmart \u2014 instead of scraping Walmart pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to search Walmart listings, compare prices and sellers, retrieve product details, and summarize review snapshots through Crawlora's Walmart API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends Walmart research requests to Crawlora.

Mitigation: Install only if third-party API use is acceptable; provide the key through CRAWLORA_API_KEY and do not commit it.

Risk: The helper can send broader authenticated API requests than the documented read-only Walmart endpoints require.

Mitigation: Review or tighten the helper before use if strict read-only behavior is required, especially by limiting it to documented GET routes and numeric item IDs.

## Reference(s):

- [walmart-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/walmart-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns normalized public Walmart product, search, and review data from Crawlora.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

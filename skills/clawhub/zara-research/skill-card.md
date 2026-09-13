## Description:

Researches Zara's catalog - category taxonomy, category listings, product detail, keyword search, search suggestions, and nearby physical stores - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping assistants use this skill to browse Zara categories, search Zara products, inspect product colors, sizes, images, and availability, and find nearby Zara stores through the Crawlora API instead of scraping zara.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Crawlora API key and sends Zara search terms or store-location coordinates to Crawlora.

Mitigation: Install only when this data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and never hardcode, commit, or pass the key in query parameters.

Risk: Undocumented POST or non-Zara routes could broaden what the helper sends to Crawlora beyond the documented research workflow.

Mitigation: Use the documented GET examples and the listed Zara endpoints; avoid POST or undocumented paths unless the publisher tightens helper validation.

Risk: Zara search results are best-effort and may return broader recommendations for obscure or nonsensical queries.

Mitigation: Treat search output as candidates, refine with suggestions when useful, and inspect product detail before making recommendations.

## Reference(s):

- [zara-research endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/zara-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora API site](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses contain normalized public Zara catalog, product, search, suggestion, and store data.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Researches Wish's marketplace - categories, product search, product detail, related items, and reviews - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to browse Wish categories, search products, inspect product detail, compare prices and ratings, find related items, and summarize reviews through Crawlora's API instead of scraping wish.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can send the Crawlora API key to arbitrary Crawlora paths or to an overridden API host.

Mitigation: Use a limited, revocable Crawlora key; restrict calls to the documented Wish endpoints; avoid setting CRAWLORA_API_BASE unless the destination is fully controlled.

Risk: The skill works with public Wish marketplace data and external API responses, which may be incomplete, unavailable, or subject to Wish's terms.

Mitigation: Use the output for research support, verify important product decisions against current source data, and respect Wish's terms.

## Reference(s):

- [Wish endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Wish marketplace data.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

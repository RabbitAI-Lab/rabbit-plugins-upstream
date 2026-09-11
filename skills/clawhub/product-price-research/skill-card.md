## Description:

Researches products, prices, sellers, availability, and reviews across major marketplaces and retailers with the Crawlora API, returning normalized JSON instead of scraping store pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to find products, compare prices and sellers, check availability, and summarize public marketplace or retailer reviews without scraping store pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product searches, product identifiers, ZIP codes, coordinates, and similar lookup parameters are sent to Crawlora.

Mitigation: Use the skill for non-sensitive product research and avoid sensitive personal, financial, health, or account data.

Risk: The Crawlora API key could be exposed if pasted into prompts, request bodies, command arguments, or committed files.

Mitigation: Keep CRAWLORA_API_KEY in the environment and use the provided helper so the key is supplied through a private curl config.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment; API results are paginated where supported.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

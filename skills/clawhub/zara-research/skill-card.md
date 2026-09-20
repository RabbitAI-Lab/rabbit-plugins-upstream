## Description:

Researches Zara's catalog - category taxonomy, category listings, product detail, keyword search, search suggestions, and nearby physical stores - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Zara catalog data, product details, keyword search results, search suggestions, and nearby physical stores through the Crawlora API instead of scraping Zara pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Crawlora as an intermediary for Zara research.

Mitigation: Install only when that intermediary use is acceptable for the task and user context.

Risk: A Crawlora API key could be exposed if hardcoded, committed, or passed directly in command text.

Mitigation: Set CRAWLORA_API_KEY through the environment and avoid placing the key in prompts, files, URLs, or command-line arguments.

Risk: Nearby-store lookup sends precise latitude and longitude to the Crawlora API.

Mitigation: Provide coordinates only when a nearby-store lookup is necessary.

Risk: Zara keyword search can return broad recommended results rather than exact keyword matches.

Mitigation: Check product detail and listing data before presenting search results as exact matches.

## Reference(s):

- [zara-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub zara-research skill](https://clawhub.ai/crawlora-org/skills/zara-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment; helper requests are limited to documented GET routes.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

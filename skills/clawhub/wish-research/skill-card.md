## Description:

Researches Wish marketplace categories, product search, product detail, related items, and reviews through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Wish marketplace categories, products, related items, and reviews, then compare prices, ratings, merchants, and buyer feedback without scraping wish.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wish search terms, product IDs, and requested review or detail lookups are sent to Crawlora under the user's Crawlora API key.

Mitigation: Do not include private information in Wish queries, and install only when this data sharing is acceptable.

Risk: The Crawlora API key could be exposed if copied into code, logs, or committed files.

Mitigation: Keep CRAWLORA_API_KEY in the environment and avoid hardcoding or committing it.

Risk: The skill works with public Wish marketplace data and may return empty or unavailable results for missing products, no reviews, or limited pagination.

Mitigation: Treat empty results as normal API outcomes and verify product identity with the documented 24-character Wish product ID.

## Reference(s):

- [wish-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/wish-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; helper calls are limited to documented Wish endpoints.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

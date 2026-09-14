## Description:

Researches Walmart products, prices, sellers, and reviews using the Crawlora API, returning clean JSON for product discovery, price comparison, listing tracking, and review lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Walmart product listings, prices, availability, sellers, and review summaries through Crawlora instead of scraping Walmart pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Walmart search terms and product identifiers are sent to Crawlora as an intermediary service.

Mitigation: Use the skill only for public product research and avoid private or sensitive search terms.

Risk: The skill requires a Crawlora API key.

Mitigation: Store the key only in CRAWLORA_API_KEY and keep it out of committed files and shared command text.

Risk: Review data is a single on-page snapshot rather than a complete paginated review feed.

Mitigation: Treat review summaries as point-in-time signals and verify important conclusions before business use.

## Reference(s):

- [walmart-research endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented Walmart GET endpoints for public product, search, and review data.]

## Skill Version(s):

1.0.16 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Researches Walmart products, prices, sellers, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search Walmart listings, compare product prices and availability, inspect product details, and summarize review snapshots through Crawlora's Walmart API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-directed Walmart product queries to Crawlora as a third-party API.

Mitigation: Install only when third-party Crawlora API use is acceptable, keep CRAWLORA_API_KEY private, and avoid sending sensitive personal data as search terms.

Risk: Results reflect public Walmart product and review data returned through Crawlora and may be incomplete, paginated, or limited to a review snapshot.

Mitigation: Use pagination for listing sweeps, treat review data as a snapshot, and review Crawlora and Walmart terms for the intended use.

## Reference(s):

- [Walmart endpoint reference](reference/endpoints.md)
- [Crawlora API service](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/walmart-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses from Crawlora API calls with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and supports documented GET endpoints for Walmart search, product detail, and product reviews.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

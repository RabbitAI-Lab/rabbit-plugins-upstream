## Description:

Compare short-term rental market supply, listing density, room mix, price distributions, and review signals using Crawlora Airbnb aggregates and selected live listings, with explicit sampling and freshness limits rather than occupancy or revenue estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, operators, and developers use this skill to build comparable short-term rental market panels from Crawlora Airbnb aggregates and optional sampled live listings while preserving scope, freshness, suppression, and price-basis limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a Crawlora API key and market-research queries, including locations and listing IDs, to Crawlora.

Mitigation: Keep the API key in the environment, use the skill only when Crawlora data sharing fits the user's policy, and avoid sensitive private locations unless approved.

Risk: Repeated collection can consume Crawlora credits or expand beyond the user's intended scope.

Mitigation: Bound requests to the stated market scope and credit budget, and save retrieval timestamps, query settings, source IDs, and pagination progress for resumable collection.

Risk: Aggregate, suppressed, or sampled live listing data can be overstated as occupancy, revenue, demand, legality, or property-level evidence.

Mitigation: Report sampling, freshness, suppression, price basis, and enrichment limits, and keep live listing examples separate from aggregate market statistics.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/short-term-rental-market-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell command examples and API result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns market comparisons with separate sampled listing examples.]

## Skill Version(s):

1.0.7 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

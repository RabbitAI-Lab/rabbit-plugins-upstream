## Description:

Compares observed local business supply, categories, attributes, hours, and review-sample themes across defined areas using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, and Yelp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to compare like-for-like observations of local businesses across matched areas. It supports coverage ledgers, business matrices, and cautious comparisons without making demand, revenue, market-share, or site-viability claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends the Crawlora API key plus business-search queries, locations, place IDs, and review/detail requests to Crawlora's API.

Mitigation: Keep the key in the environment, avoid logging it, and run bounded, user-directed searches.

Risk: Bounded map and directory results can omit relevant businesses or contain stale, unknown, or source-disagreed records.

Mitigation: Disclose source, retrieval date, geometry, pagination or limit bounds, unknown buckets, and source disagreements; avoid population, demand, revenue, market-share, and site-viability claims.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/local-competitive-landscape)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and tabular analysis structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces coverage ledgers, business matrices, and comparison narratives grounded in bounded API observations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

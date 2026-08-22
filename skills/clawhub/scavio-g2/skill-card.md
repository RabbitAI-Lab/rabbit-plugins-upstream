## Description:

Search G2, the B2B software review site, read a full product profile with pricing and features, and pull faceted reviews with exact per-star counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to search G2 software listings, inspect product profiles, compare alternatives, and analyze customer reviews for SaaS competitive intelligence and voice-of-customer research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Scavio API key.

Mitigation: Install only when the agent may use SCAVIO_API_KEY, keep the key in an environment variable or secret store, and avoid committing credentials.

Risk: G2 endpoint calls consume 5 Scavio credits per request, so multi-page review pulls can spend credits quickly.

Mitigation: State the planned credit spend before multi-call workflows and get approval before broad pagination.

Risk: Filtered review calls can return zero results because a filter matched nothing, not because a segment has no opinion.

Mitigation: Re-check unfiltered review data before reporting that a buyer segment has no reviews or sentiment.

Risk: External product, pricing, rating, and review data may be incomplete or unavailable for a requested product.

Mitigation: Report unavailable data directly and do not fabricate product names, ratings, review counts, pricing, or review text.

## Reference(s):

- [Scavio G2 Search documentation](https://scavio.dev/docs/g2-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses structured JSON API responses and requires SCAVIO_API_KEY for live endpoint calls.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

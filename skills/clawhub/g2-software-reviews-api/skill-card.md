## Description:

Search G2, the B2B software review site, read a full product profile with pricing and features, and pull faceted reviews with exact per-star counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search G2 for B2B software products, inspect product profiles, and mine structured customer-review data for competitive intelligence, vendor comparison, product research, pricing research, and voice-of-customer analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends G2 search, product, and review requests to Scavio and consumes paid Scavio credits.

Mitigation: Confirm the intended request count before running, especially for multi-page review pulls, and state the expected credit cost up front.

Risk: SCAVIO_API_KEY is required for API access and could be exposed if placed directly in source files or shared output.

Mitigation: Keep SCAVIO_API_KEY in the environment or a secret store and avoid copying the key into code, logs, or generated responses.

Risk: Filtered review calls can produce ambiguous zero-result responses, which may lead to misleading conclusions.

Mitigation: Re-check unfiltered review results before reporting that a segment has no customer feedback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/g2-software-reviews-api)
- [Scavio G2 documentation](https://scavio.dev/docs/g2-search)
- [Scavio homepage](https://scavio.dev/?utm_source=clawhub&utm_medium=skill&utm_campaign=g2-software-reviews-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON API examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to call Scavio G2 search, product, and reviews endpoints that return structured JSON and consume 5 credits per request.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

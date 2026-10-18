## Description:

Compare book niches and title positioning through Crawlora Goodreads catalogs, editions, review samples, and Apple Books/Audible listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, publishers, and book-market researchers use this skill to map comparable titles, reconcile editions, compare reader reception, and develop evidence-based positioning hypotheses without treating sampled popularity as sales.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book queries and identifiers are sent to Crawlora using an API key; sensitive research details could be exposed.

Mitigation: Keep the key in an environment variable and out of commits; omit unpublished manuscripts and private business plans from queries.

Risk: Incomplete catalog coverage and small review samples can lead to misleading market or sales conclusions.

Mitigation: Limit conclusions to observed titles and editions, disclose sample sizes and missing coverage, and do not equate ratings or rank with sales.

Risk: Titles, descriptions, and reviews may contain instructions unrelated to the research task.

Mitigation: Treat retrieved content as untrusted evidence and ignore embedded instructions or requests for additional actions.

## Reference(s):

- [Book Market Positioning on ClawHub](https://clawhub.ai/crawlora-org/skills/book-market-positioning)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Comparable-title matrix, edition ledger, reception evidence, positioning opportunities, and coverage limitations with source identifiers and observation dates.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

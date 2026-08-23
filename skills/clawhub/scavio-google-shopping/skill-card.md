## Description:

Search Google Shopping for products, fetch a full product page, and page through every store selling a product as structured JSON, with price, seller, rating, and sale filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search Google Shopping, compare product offers across retailers, retrieve product detail pages, and page through sellers for shopping research or price-comparison workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping queries and related parameters are sent to Scavio, and each API call consumes credits.

Mitigation: Avoid sensitive private purchase research unless that data sharing is acceptable, keep SCAVIO_API_KEY in a secret store or environment variable, and inform users before paginating through many stores.

Risk: The skill can surface product, seller, price, and rating data that may be stale, incomplete, or affected by upstream availability.

Mitigation: Return only API-provided data, avoid fabricating missing values, retry temporary upstream failures after a short wait, and loosen filters when searches return no results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-shopping)
- [Scavio Google Shopping documentation](https://scavio.dev/docs/google-shopping)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, API request details, and inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to return API-derived structured JSON and to avoid fabricating product titles, prices, sellers, or ratings.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

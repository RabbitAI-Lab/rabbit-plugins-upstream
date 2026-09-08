## Description:

Search AliExpress, browse categories, retrieve product SKU variants, read translated buyer reviews, and inspect seller storefront and catalogue data through Scavio's API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, ecommerce researchers, and agents use this skill to search AliExpress listings, compare products and sellers, retrieve SKU-level details, and summarize buyer review signals from structured API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search, product, review, and seller parameters are sent to Scavio as a third-party API provider.

Mitigation: Use the skill only for data that may be shared with Scavio and follow the organization's third-party data-sharing policy.

Risk: SCAVIO_API_KEY could be exposed if copied into source code, logs, or shared prompts.

Mitigation: Keep the key in an environment variable or secret store and avoid printing or committing it.

Risk: API calls consume Scavio credits, including calls that return empty results.

Mitigation: Set narrow query criteria, monitor credit usage, and handle 402 and 429 responses before retrying.

Risk: Buyer reviews may include user-authored personal content.

Mitigation: Summarize review themes and avoid profiling individual reviewers.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/aliexpress-product-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API request and response shapes, plus Python or curl examples when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY for authenticated Scavio API calls and returns structured JSON data; product and seller endpoints may need up to a 120 second timeout.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

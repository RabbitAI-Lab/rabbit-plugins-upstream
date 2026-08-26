## Description:

Search AliExpress, browse a category, pull one product with every SKU variant, read translated buyer reviews, and open a seller's storefront and catalogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and research agents use this skill to retrieve structured AliExpress product, review, seller, and catalogue data through Scavio's API for price comparison, product research, dropshipping research, and catalogue analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each API call consumes Scavio credits, including calls that return empty results.

Mitigation: Confirm request parameters before calling the API and widen or adjust filters before retrying repeated empty searches.

Risk: Requests send AliExpress lookup data to Scavio using the user's API key.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and avoid exposing it in source code, logs, or shared transcripts.

Risk: Buyer review data may contain information written by real people.

Mitigation: Summarize review trends and avoid identifying, profiling, or targeting individual buyers.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-aliexpress)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, text]

**Output Format:** [Markdown guidance with JSON API request and response details, Python snippets, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoints return structured JSON and consume Scavio credits.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Search AliExpress, browse a category, pull one product with every SKU variant, read translated buyer reviews, and open a seller's storefront and catalogue. 6 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce analysts, and agent builders use this skill to search AliExpress products, compare prices, inspect SKU variants, retrieve reviews, and review seller storefront data through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends AliExpress research queries to Scavio as a third-party API provider.

Mitigation: Use it only when third-party processing fits the user's data-sharing expectations, and avoid sending sensitive business queries unless approved.

Risk: The skill requires a Scavio API key and each endpoint call consumes credits.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store, keep it out of source control, and monitor credit usage.

Risk: Product, price, seller, and review details can be incomplete, unavailable, or source-dependent.

Mitigation: Return only data from the API response, handle empty and error responses, and do not fabricate prices, ratings, seller details, or review text.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/aliexpress-product-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API response handling examples, Python snippets, and curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to use structured JSON responses returned by Scavio's AliExpress endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Search AliExpress, browse a category, pull one product with every SKU variant, read translated buyer reviews, and open a seller's storefront and catalogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce researchers use this skill to query AliExpress product, category, review, and seller data through Scavio's structured API for market research, dropshipping analysis, price comparison, and catalogue inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key for AliExpress research.

Mitigation: Keep SCAVIO_API_KEY out of source control and provide it through the agent environment or secret store.

Risk: Each API call consumes disclosed Scavio credits, including empty results.

Mitigation: Confirm the user is comfortable with the credit costs before running broad searches or repeated pagination.

Risk: Buyer reviews may contain user-generated content tied to real purchasers.

Mitigation: Summarize review data in aggregate and avoid profiling individual buyers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/aliexpress-product-data)
- [Scavio AliExpress API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with bash, curl, and Python examples for JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; AliExpress endpoints cost 1 credit per call and product or seller lookups may take 20-60 seconds. Security review verdict: clean.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

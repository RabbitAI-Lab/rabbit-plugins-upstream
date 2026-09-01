## Description:

Search AliExpress, browse a category, pull one product with every SKU variant, read translated buyer reviews, and open a seller's storefront and catalogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce researchers use this skill to query AliExpress product, category, review, seller, and catalogue data through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AliExpress lookup parameters are sent to Scavio for processing.

Mitigation: Confirm the data-sharing posture is acceptable before installing or invoking the skill.

Risk: Each API call spends Scavio credits, including calls that return empty results.

Mitigation: Use focused queries and filters, monitor credit balance, and confirm intent before running broad or repeated lookups.

Risk: SCAVIO_API_KEY is required for all endpoint calls.

Mitigation: Store the key in the environment or a secret store, and avoid placing it in source files or shared transcripts.

## Reference(s):

- [Scavio AliExpress API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=aliexpress-product-data)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/aliexpress-product-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and inline Python or curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio AliExpress endpoints consume 1 credit per call and may require a 120 second timeout for product and seller lookups.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

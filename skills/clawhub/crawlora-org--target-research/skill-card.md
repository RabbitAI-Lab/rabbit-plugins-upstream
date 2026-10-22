## Description:

Searches Target products and categories through Crawlora to retrieve pricing, availability, product details, questions, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and shopping assistants use this skill to find and compare Target products, check store-specific pricing and availability, and review product questions and customer feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, product IDs, store IDs, and location inputs are sent to Crawlora.

Mitigation: Avoid sensitive personal information in queries unless you intend to share it with Crawlora.

Risk: Using the skill requires a Crawlora API key.

Mitigation: Keep the key in the environment and never include it in queries, source files, or shared output.

## Reference(s):

- [Target endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/target-research)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with JSON-derived product information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Catalog results are paginated; store-specific prices and availability require a store ID.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

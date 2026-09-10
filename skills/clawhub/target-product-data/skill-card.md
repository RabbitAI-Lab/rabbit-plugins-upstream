## Description:

Search Target.com, browse a category, read product detail by TCIN and pull reviews with the rating breakdown as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to search Target products, browse categories, retrieve TCIN-level product details, and summarize review data with store-aware pricing and availability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends Target lookup requests to Scavio with SCAVIO_API_KEY.

Mitigation: Keep the API key in an environment variable or secret store and avoid exposing it in prompts, logs, or source files.

Risk: Each endpoint consumes Scavio credits.

Mitigation: Check credit balance and rate limits before high-volume use.

Risk: Target prices and availability vary by store and can change after retrieval.

Mitigation: Pass the relevant store_id and include product URLs so users can verify current details.

Risk: Some Target calls can be slow or require retries.

Mitigation: Use long client timeouts or background execution for category and review requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/target-product-data)
- [Target search documentation](https://scavio.dev/docs/target-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Target category documentation](https://scavio.dev/docs/target-category?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Target product documentation](https://scavio.dev/docs/target-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Target reviews documentation](https://scavio.dev/docs/target-reviews?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls consume Scavio credits and return product data in a JSON envelope.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

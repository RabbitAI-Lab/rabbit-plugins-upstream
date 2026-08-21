## Description:

Search Target.com, browse a category, read product detail by TCIN and pull reviews with the rating breakdown as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and commerce analysts use this skill to query Scavio's Target endpoints for product search, category browsing, TCIN-level details, store-specific pricing and availability, and review summaries as structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Endpoint calls send requests to Scavio using SCAVIO_API_KEY and consume Scavio credits.

Mitigation: Keep the API key in an environment variable or secret store, and call the skill only when Target product, price, availability, or review data is needed.

Risk: Target endpoints can be slow, especially category and review calls.

Mitigation: Use long client timeouts and prefer asynchronous or background execution for user-facing workflows.

Risk: Prices, availability, seller fields, and returned review bodies can be store-dependent or partial.

Mitigation: Pass the relevant store_id, disclose the store context when reporting results, include product URLs for verification, and do not present returned review bodies as the complete review corpus.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/target-product-data)
- [Scavio Target Search Docs](https://scavio.dev/docs/target-search)
- [Scavio Target Category Docs](https://scavio.dev/docs/target-category)
- [Scavio Target Product Docs](https://scavio.dev/docs/target-product)
- [Scavio Target Reviews Docs](https://scavio.dev/docs/target-reviews)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash setup, JSON request examples, and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoint calls consume Scavio credits and may need long client timeouts.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Search Target.com, browse a category, read product detail by TCIN and pull reviews with the rating breakdown as structured JSON. 4 endpoints, 1 credit each, store-aware pricing via store_id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Target product search, category browsing, product detail, store-aware prices and reviews through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party service for Target product data and requires an API key.

Mitigation: Install only if comfortable using Scavio for this data flow, and keep SCAVIO_API_KEY in an environment variable or secret store rather than source control.

Risk: Documented endpoints consume credits and Target calls may take a long time to return.

Mitigation: Plan client timeouts and background execution around the documented latency and credit behavior.

Risk: Fabricated or overstated product, price, availability, TCIN, rating, or review data could mislead users.

Mitigation: Return only data provided by the API and include product URLs so users can verify the source listing.

Risk: Review body results are limited and should not be treated as the complete review corpus.

Mitigation: State that the reviews endpoint returns at most 8 review bodies while the rating breakdown covers all reviews.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/target-product-data)
- [Scavio Target Search Documentation](https://scavio.dev/docs/target-search)
- [Scavio Target Category Documentation](https://scavio.dev/docs/target-category)
- [Scavio Target Product Documentation](https://scavio.dev/docs/target-product)
- [Scavio Target Reviews Documentation](https://scavio.dev/docs/target-reviews)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline bash and Python examples plus structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; documented endpoints cost 1 credit each and may take a long time to return.]

## Skill Version(s):

1.0.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

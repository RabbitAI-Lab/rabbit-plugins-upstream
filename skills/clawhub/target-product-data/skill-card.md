## Description:

Search Target.com, browse a category, read product detail by TCIN, pull reviews with the rating breakdown, and check in-store stock at every Target near a ZIP as structured JSON. 5 endpoints, 1 credit each, store-aware pricing via store_id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Target products, inspect product details and reviews, and check store-specific prices and nearby store availability.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Shopping queries and supplied ZIP codes are sent to Scavio.

Mitigation: Use this skill only if you are comfortable sharing those details with Scavio.

Risk: API credentials and credit usage require care.

Mitigation: Keep the API key in an environment variable or secret store and monitor credit usage.

Risk: Prices and store availability should be confirmed for the intended product and store.

Mitigation: Verify prices and stock through the returned product links.

## Reference(s):

- [Target search API](https://scavio.dev/docs/target-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Target category API](https://scavio.dev/docs/target-category?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Target product API](https://scavio.dev/docs/target-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Target reviews API](https://scavio.dev/docs/target-reviews?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Target availability API](https://scavio.dev/docs/target-availability?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=target-product-data)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON API results with concise setup and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five Target endpoints; each call costs 1 credit.]

## Skill Version(s):

1.0.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

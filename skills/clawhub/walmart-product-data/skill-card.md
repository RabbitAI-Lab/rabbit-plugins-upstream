## Description:

Search Walmart and read product detail, reviews, category listings, buy-box offers, seller storefronts and a seller's catalog as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to search Walmart marketplaces, retrieve product details and reviews, inspect category listings, check buy-box data, and look up marketplace seller information through Scavio's Walmart API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and consumes credits when it queries Walmart data.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, monitor credit usage, and read credits_used in API responses.

Risk: Returned product prices, availability, seller data, and Walmart links may change after retrieval.

Mitigation: Verify returned Walmart links and current listing details before relying on availability, pricing, or purchase decisions.

Risk: Some endpoints have scoped behavior, such as buy-box-only offers, first-page seller catalog results, and country-specific support.

Mitigation: Follow the documented guardrails, avoid inventing unsupported pagination or full offer lists, and surface API warnings to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/walmart-product-data)
- [Scavio Walmart API documentation](https://scavio.dev/docs/walmart-api)
- [Scavio Walmart product documentation](https://scavio.dev/docs/walmart-product)
- [Scavio Walmart reviews documentation](https://scavio.dev/docs/walmart-reviews)
- [Scavio Walmart category documentation](https://scavio.dev/docs/walmart-category)
- [Scavio Walmart offers documentation](https://scavio.dev/docs/walmart-offers)
- [Scavio Walmart seller documentation](https://scavio.dev/docs/walmart-seller)
- [Scavio Walmart seller products documentation](https://scavio.dev/docs/walmart-seller-products)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline code blocks and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and consumes Scavio credits based on endpoint and request body.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

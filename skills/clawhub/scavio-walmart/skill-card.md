## Description:

Search Walmart and read product detail, reviews, category listings, buy-box offers, seller storefronts and a seller's catalog as structured JSON. 7 endpoints; cost depends on the body - 1 credit, or 2 when search or category targets walmart.com.mx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Walmart marketplaces, retrieve product and review data, inspect buy-box sellers, and look up seller storefronts and catalogs through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Walmart queries, product identifiers, and seller identifiers are sent to Scavio's API.

Mitigation: Use the skill only for data you are comfortable sharing with Scavio, and avoid sending sensitive or private identifiers.

Risk: Requests consume Scavio credits, and search or category calls against walmart.com.mx cost more than default US or Canada calls.

Mitigation: Read credits_used in each response and confirm the domain-specific cost rule before running broad searches or category requests.

Risk: Incorrect parameters can be ignored with warnings or rejected, which may produce misleading results if warnings are not surfaced.

Mitigation: Use only documented enum values, omit retired parameters, and report any warnings returned by the API.

Risk: The offers endpoint returns only the buy-box seller, not every seller for a Walmart item.

Mitigation: Describe offers results as buy-box data only and avoid claiming the API enumerates all offers.

## Reference(s):

- [Scavio Walmart API Documentation](https://scavio.dev/docs/walmart-api)
- [Scavio Walmart Product Documentation](https://scavio.dev/docs/walmart-product)
- [Scavio Walmart Reviews Documentation](https://scavio.dev/docs/walmart-reviews)
- [Scavio Walmart Category Documentation](https://scavio.dev/docs/walmart-category)
- [Scavio Walmart Offers Documentation](https://scavio.dev/docs/walmart-offers)
- [Scavio Walmart Seller Documentation](https://scavio.dev/docs/walmart-seller)
- [Scavio Walmart Seller Products Documentation](https://scavio.dev/docs/walmart-seller-products)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, text, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell and Python examples, plus structured JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses Scavio credits per request.]

## Skill Version(s):

3.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

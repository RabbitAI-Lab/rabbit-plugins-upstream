## Description:

Search Amazon, read full product detail by ASIN, and list every seller offer on an ASIN with the buy-box winner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping or ecommerce research agents use this skill to search Amazon products, inspect product details by ASIN, and compare seller offers across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon search terms and ASINs are sent to Scavio, and authenticated data endpoints may consume paid credits.

Mitigation: Use the skill only when sharing those queries with Scavio is acceptable, keep SCAVIO_API_KEY in an environment variable or secret store, and warn users before broad pagination or loops.

Risk: Product prices, availability, delivery estimates, seller offers, and review counts can be point-in-time or approximate depending on the endpoint.

Mitigation: Include product URLs and fetch timing, avoid presenting search-derived rounded review counts as exact, and re-check product or offer endpoints before making decisions.

Risk: Marketplace or sorting assumptions can produce misleading comparisons.

Mitigation: Validate marketplace codes against the documented options endpoint, state when sorting was performed locally, and avoid comparing prices across currencies without external conversion.

## Reference(s):

- [Scavio Amazon API Documentation](https://scavio.dev/docs/amazon-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=amazon-product-data)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/amazon-product-data)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Code, Guidance]

**Output Format:** [Markdown guidance with JSON API responses, shell commands, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY for billed Scavio Amazon API calls; the marketplace options endpoint is documented as free and keyless.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

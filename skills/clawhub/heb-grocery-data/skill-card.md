## Description:

HEB grocery data as structured JSON - product search, full item detail with pricing and nutrition, and store locator. 3 endpoints, 2 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search HEB products, retrieve product details such as pricing and nutrition, and find nearby HEB or Central Market stores. It supports grocery price comparisons and catalog enrichment using structured API data.

### Deployment Geography for Use:

United States, primarily Texas and nearby states; HEB store coverage also includes parts of northeast Mexico.

## Known Risks and Mitigations:

Risk: Search terms, product references, and supplied ZIP code or city are sent to Scavio, and requests consume API credits.

Mitigation: Avoid sending sensitive information, keep the API key private, and monitor credit usage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/scavio-ai/skills/heb-grocery-data)
- [HEB API overview](https://scavio.dev/heb-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB search documentation](https://scavio.dev/docs/heb-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB product documentation](https://scavio.dev/docs/heb-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB stores documentation](https://scavio.dev/docs/heb-stores?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)

## Skill Output:

**Output Type(s):** [JSON, API Calls]

**Output Format:** [Structured JSON data returned by the HEB endpoints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live API data; prices, availability, promotions, and store details may change.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

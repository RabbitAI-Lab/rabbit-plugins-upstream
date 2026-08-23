## Description:

Search Amazon, retrieve product details by ASIN, and compare seller offers with normalized product, pricing, availability, shipping, rating, review, and buy-box data across 22 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and retail analysts use this skill to search Amazon marketplaces, look up products by ASIN, compare seller offers, and prepare structured product-research outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches and ASIN lookups are sent to Scavio with SCAVIO_API_KEY and may consume paid or limited API credits.

Mitigation: Confirm the user intends to make the request, keep the API key in environment or secret storage, and avoid unnecessary product, offer, or pagination calls.

Risk: Invalid marketplace or country inputs can return plausible US storefront data instead of the intended marketplace.

Mitigation: Validate marketplace codes against the documented options endpoint before calling search, product, or offers endpoints.

## Reference(s):

- [Scavio Amazon API documentation](https://scavio.dev/docs/amazon-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/amazon-product-data)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with JSON API responses, shell commands, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY for paid or limited Scavio API calls; marketplace inputs should be validated before use.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

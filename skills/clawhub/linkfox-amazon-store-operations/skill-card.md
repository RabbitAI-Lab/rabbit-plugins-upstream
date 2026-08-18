## Description:

LinkFox Amazon Store Operations is a one-stop Amazon SP-API operations toolkit covering authorization, orders, listings, pricing, catalog, reports, feeds, customer feedback, uploads, A+ content, external fulfillment, and FBA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce operators, and agent developers use this skill to perform authenticated store operations through LinkFox, including data retrieval, report workflows, and explicit store changes.

### Deployment Geography for Use:

Amazon marketplaces supported by the skill, including United States, United Kingdom, Germany, Japan, France, Italy, and Spain; region must match the authorized store.

## Known Risks and Mitigations:

Risk: The skill can operate with broad Amazon seller-account access and includes high-impact write actions.

Mitigation: Install only for intended LinkFox-backed store operations and require explicit user confirmation before listing, feed, shipment, A+ content, upload, or fulfillment changes.

Risk: Tokens and saved response data may expose sensitive seller or buyer information if mishandled.

Mitigation: Keep gateway and base-url environment variables pinned to trusted LinkFox hosts, avoid sharing saved response directories, and delete old session data after use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-operations)
- [Amazon store authorization quick start](references/quick-start.md)
- [Amazon store authorization and management](references/linkfox-amazon-store-auth.md)
- [Amazon store orders](references/linkfox-amazon-store-orders.md)
- [Amazon store listings](references/linkfox-amazon-store-listings.md)
- [Amazon store pricing](references/linkfox-amazon-store-pricing.md)
- [Amazon store catalog](references/linkfox-amazon-store-catalog.md)
- [Amazon store reports](references/linkfox-amazon-store-report.md)
- [Amazon store feeds](references/linkfox-amazon-store-feeds.md)
- [Amazon store customer feedback](references/linkfox-amazon-store-customer-feedback.md)
- [Amazon store uploads](references/linkfox-amazon-store-uploads.md)
- [Amazon store A+ content](references/linkfox-amazon-store-aplus-content.md)
- [Amazon store external fulfillment](references/linkfox-amazon-store-external-fulfillment.md)
- [Amazon store FBA](references/linkfox-amazon-store-fba.md)
- [Report type reference](references/report-types.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON request or response artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts can save full LinkFox/SP-API responses as local JSON files and print summaries for large responses.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

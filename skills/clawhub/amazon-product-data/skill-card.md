## Description:

Search Amazon, read full product detail by ASIN, and list every seller offer on an ASIN with the buy-box winner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Amazon products, retrieve ASIN-level details, and compare seller offers across supported marketplaces using Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon search terms, ASINs, and the Scavio API key are sent to Scavio's service.

Mitigation: Use a user-provided SCAVIO_API_KEY, avoid sending sensitive searches, and explain this data flow before use.

Risk: Billable credits may be consumed by deep pagination, bulk ASIN lookup, or repeated offer checks.

Mitigation: Confirm user intent before loops or multi-page lookups and prefer the free options endpoint when validating marketplaces.

Risk: Marketplace typos, rounded search review counts, unavailable sort behavior, and first-page-only offers can lead to misleading conclusions.

Mitigation: Validate country codes, state when local sorting is applied, treat large search review counts as rounded, and disclose when offers are limited to the first page.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/amazon-product-data)
- [Scavio Amazon API documentation](https://scavio.dev/docs/amazon-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with JSON request and response examples, shell commands, and Python code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY for billable search, product, and offers calls; API responses are point-in-time product data.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

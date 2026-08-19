## Description:

Helps agents look up Amazon store catalog categories and catalog item data by ASIN, SKU, keywords, or identifiers through LinkFox-supported SP-API Catalog Items workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and Amazon store operators use this skill to retrieve catalog categories, search catalog items, and fetch item details for store catalog workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill can perform account login, API key issuance, paid order creation, and local plaintext response storage in addition to catalog reads.

Mitigation: Review the skill before installation, use it only in a trusted workspace, treat printed API keys as secrets, and confirm billing behavior before running onboarding purchase commands.

Risk: Endpoint override environment variables can redirect requests away from the default LinkFox gateway.

Mitigation: Set endpoint override variables only when the destination is controlled and expected.

Risk: Saved API responses may contain sensitive catalog or account-adjacent data.

Mitigation: Restrict workspace access and remove generated response files when they are no longer needed.

## Reference(s):

- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [Amazon SP-API listCatalogCategories](https://developer-docs.amazon.com/sp-api/reference/listcatalogcategories)
- [Amazon SP-API searchCatalogItems](https://developer-docs.amazon.com/sp-api/reference/searchcatalogitems)
- [Amazon SP-API getCatalogItem](https://developer-docs.amazon.com/sp-api/reference/getcatalogitem)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-catalog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell command examples, and JSON responses or summaries from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full API responses under the current workspace's linkfox date/session data directory and may print full JSON or a summary to stdout.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

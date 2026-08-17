## Description:

Helps agents manage Amazon store listings through LinkFox by retrieving, searching, updating, creating, deleting listings, checking listing restrictions, and fetching product type definitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and developers use this skill to inspect and manage Amazon listing data, validate listing restrictions, and obtain product type definitions before creating or changing listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact listing changes through PATCH, PUT, and DELETE operations.

Mitigation: Require explicit review of sellerId, SKU, marketplace, and payload before any agent-initiated write or delete action.

Risk: Generated LinkFox response files may contain sensitive Amazon seller listing or account data.

Mitigation: Treat saved files under ./linkfox/ as sensitive business data and clean them up according to the user's data handling policy.

Risk: Credentials and gateway configuration affect access to Amazon seller data and LinkFox account onboarding.

Mitigation: Use a dedicated, minimally scoped API key and leave gateway URL override environment variables unset unless the endpoint is trusted.

Risk: Account and payment onboarding may be triggered for authentication or billing failures.

Mitigation: Review onboarding prompts before providing phone, payment, or account information.

## Reference(s):

- [Amazon Store Listings API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-listings)
- [Amazon SP-API getListingsItem](https://developer-docs.amazon.com/sp-api/reference/getlistingsitem)
- [Amazon SP-API searchListingsItems](https://developer-docs.amazon.com/sp-api/reference/searchlistingsitems)
- [Amazon SP-API patchListingsItem](https://developer-docs.amazon.com/sp-api/reference/patchlistingsitem)
- [Amazon SP-API putListingsItem](https://developer-docs.amazon.com/sp-api/reference/putlistingsitem)
- [Amazon SP-API deleteListingsItem](https://developer-docs.amazon.com/sp-api/reference/deletelistingsitem)
- [Amazon SP-API getListingsRestrictions](https://developer-docs.amazon.com/sp-api/reference/getlistingsrestrictions)
- [Amazon SP-API searchDefinitionsProductTypes](https://developer-docs.amazon.com/sp-api/reference/searchdefinitionsproducttypes)
- [Amazon SP-API getDefinitionsProductType](https://developer-docs.amazon.com/sp-api/reference/getdefinitionsproducttype)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON stdout, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full responses under ./linkfox/<date>/<session>/data/ and summarize responses larger than 8 KB unless --inline is used.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

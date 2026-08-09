## Description:

This skill helps agents manage Amazon store listings through LinkFox SP-API workflows, including listing retrieval, search, updates, deletion, listing restrictions, and product type definitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers managing Amazon seller workflows use this skill to retrieve, search, create, update, or delete listings, check ASIN listing restrictions, and inspect product type definitions through LinkFox-authorized SP-API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete live Amazon listings.

Mitigation: Verify the SKU, marketplace, operation type, and request body before running PATCH, PUT, or DELETE commands.

Risk: The skill can run LinkFox login and payment-related onboarding flows.

Mitigation: Use a dedicated LinkFox API key and confirm authentication or billing prompts before continuing.

Risk: Full API responses are stored locally and may contain business-sensitive seller data.

Mitigation: Review and protect the local linkfox output directory, and avoid sharing saved response files unless they have been checked for sensitive data.

Risk: Gateway URL environment variables can redirect requests to a different endpoint.

Mitigation: Override gateway URL variables only when you control and trust the destination endpoint.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-listings)
- [Amazon Listings API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Amazon getListingsItem](https://developer-docs.amazon.com/sp-api/reference/getlistingsitem)
- [Amazon searchListingsItems](https://developer-docs.amazon.com/sp-api/reference/searchlistingsitems)
- [Amazon patchListingsItem](https://developer-docs.amazon.com/sp-api/reference/patchlistingsitem)
- [Amazon putListingsItem](https://developer-docs.amazon.com/sp-api/reference/putlistingsitem)
- [Amazon deleteListingsItem](https://developer-docs.amazon.com/sp-api/reference/deletelistingsitem)
- [Amazon getListingsRestrictions](https://developer-docs.amazon.com/sp-api/reference/getlistingsrestrictions)
- [Amazon searchDefinitionsProductTypes](https://developer-docs.amazon.com/sp-api/reference/searchdefinitionsproducttypes)
- [Amazon getDefinitionsProductType](https://developer-docs.amazon.com/sp-api/reference/getdefinitionsproducttype)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full LinkFox responses under ./linkfox/<date>/<session>/data and may print summaries for responses larger than 8 KB.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

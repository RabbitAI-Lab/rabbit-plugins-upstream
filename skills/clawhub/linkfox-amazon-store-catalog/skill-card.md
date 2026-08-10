## Description:

亚马逊店铺商品目录 Catalog（与 linkfox-amazon-store-auth / report / listings / pricing / orders / feeds 同系列），经 /spApi/developerProxy 调用 SP-API Catalog Items：v0 listCatalogCategories；v2022-04-01（默认）或 v2020-12-01 的 searchCatalogItems、getCatalogItem。当用户提到亚马逊目录、Catalog Items、listCatalogCategories、searchCatalogItems、getCatalogItem、按 ASIN 查目录、关键词搜商品目录、类目节点、includedData、summaries/images 时触发。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill to let an agent retrieve Amazon SP-API Catalog Items data through LinkFox, including category lookup, keyword or identifier search, and ASIN-level catalog item retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full API responses are saved locally and may contain catalog or account-related data.

Mitigation: Keep the generated linkfox data directory out of source control and inspect only the response fields needed for the task.

Risk: The onboarding helper can assist with LinkFox login, API-key generation, and paid credit purchase flows.

Mitigation: Require explicit user confirmation before running token-generation, plan selection, order creation, or payment-related commands.

Risk: Endpoint environment variables can redirect requests away from the default LinkFox gateway.

Mitigation: Verify LinkFox gateway and API environment variables before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-catalog)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [Amazon SP-API listCatalogCategories](https://developer-docs.amazon.com/sp-api/reference/listcatalogcategories)
- [Amazon SP-API searchCatalogItems](https://developer-docs.amazon.com/sp-api/reference/searchcatalogitems)
- [Amazon SP-API getCatalogItem](https://developer-docs.amazon.com/sp-api/reference/getcatalogitem)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON responses or summaries with full response files saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Catalog scripts save complete LinkFox API responses under the current working directory and summarize large responses on stdout unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

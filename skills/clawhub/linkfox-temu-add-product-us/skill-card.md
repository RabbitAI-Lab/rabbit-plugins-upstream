## Description:

Temu 美国站发品（Add Product）API，经 LinkFox 网关转发 Partner US 商品接口：V2发品(temu.local.goods.v2.add)、类目属性、规格、图片上传、商品列表/详情/编辑、类目映射、SKU库存、供货价等。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, marketplace operators, and developers use this skill to publish and manage Temu US product listings through LinkFox. It supports category attributes, variations, image upload, Add Product V2 submission, product queries and edits, category mapping, SKU inventory, and supply-price workflows.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill handles Temu seller tokens, LinkFox API keys, and saved response files that may contain sensitive shop or product data.

Mitigation: Use it only where LinkFox is trusted, avoid unmasked token commands, and restrict, review, or delete local token and response files when they are no longer needed.

Risk: Gateway or authentication URL override environment variables could send credentials and API requests to an unintended destination.

Mitigation: Leave override variables unset unless the destination is controlled and expected for the deployment.

Risk: The integration can perform broad product-management actions, including listing creation, edits, stock updates, and supply-price workflows.

Mitigation: Review the API type and request parameters before execution, and confirm user intent before actions that change listings, inventory, pricing, or account billing state.

## Reference(s):

- [API Reference](references/api.md)
- [Access Token Authorization](references/access-token.md)
- [Authorization Flow](references/authorization-flow.md)
- [Product Publish APIs](references/product-publish-apis.md)
- [Category, Attribute, and Specification APIs](references/category-spec-apis.md)
- [Product Query APIs](references/product-query-apis.md)
- [Product Edit APIs](references/product-edit-apis.md)
- [Stock and Price APIs](references/stock-price-apis.md)
- [Partner US Catalog](references/partner-us-catalog.md)
- [Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses, saved JSON files, and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Complete API responses are saved as JSON; large responses are summarized on stdout unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

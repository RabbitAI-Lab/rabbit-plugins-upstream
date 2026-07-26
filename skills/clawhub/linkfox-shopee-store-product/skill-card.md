## Description: <br>
Shopee store product management skill that helps agents call LinkFox-forwarded Shopee Open API Product endpoints for listing lookup, item creation, item updates, price and stock changes, boosting, comments, categories, attributes, and related catalog operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to let an agent inspect and manage authorized Shopee store listings through Product module APIs. It supports product listing workflows such as category and attribute lookup, item creation, updates, stock and price changes, unlisting, boosting, comments, SKU/model operations, and related product diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live Shopee store changes, including delete, unlist, price, stock, comment reply, boost, and bulk update actions. <br>
Mitigation: Require explicit human confirmation before any destructive, public-facing, pricing, inventory, reply, promotional, or bulk operation. <br>
Risk: Full Shopee API responses are persisted under local linkfox session data and may contain sensitive store data. <br>
Mitigation: Store outputs only in protected workspaces and periodically remove or restrict access to saved linkfox session JSON files. <br>
Risk: The server security evidence notes inconsistent credit or billing language and possible feedback calls that may send task context to LinkFox. <br>
Mitigation: Confirm expected cost behavior before repeated calls and prevent or approve feedback submissions before sending operational context. <br>


## Reference(s): <br>
- [Artifact API Reference](artifact/references/api.md) <br>
- [Shopee Product API: get_category](https://open.shopee.com/documents/v2/v2.product.get_category?module=89&type=1) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-product) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON responses saved to local files with stdout JSON or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials and an authorized Shopee store; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

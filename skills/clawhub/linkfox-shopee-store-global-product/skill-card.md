## Description: <br>
Provides agent-facing commands for managing Shopee cross-border GlobalProduct catalog workflows through LinkFox's Shopee developer proxy, including category lookup, global item and SKU operations, publishing, price, and stock updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and ecommerce operators use this skill to inspect and manage authorized Shopee merchant GlobalProduct data, including global item creation, SKU management, publishing to local shops, and price or stock updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Shopee merchant products through delete, update, publish, price, and stock operations. <br>
Mitigation: Require explicit user confirmation before any write, delete, publish, price, or stock operation. <br>
Risk: Full Shopee API responses may be stored locally and can include merchant or product data. <br>
Mitigation: Use only in workspaces where local plaintext Shopee merchant data is acceptable, and verify the output directory behavior before use. <br>
Risk: The skill contains contradictory credit guidance. <br>
Mitigation: Assume API calls may consume credits until the publisher or service confirms the actual charging behavior. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-global-product) <br>
- [Bundled GlobalProduct API reference](artifact/references/api.md) <br>
- [Shopee Open Platform GlobalProduct documentation](https://open.shopee.com/documents/v2/v2.global_product.get_category?module=90&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON files plus stdout JSON or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are written under a linkfox session data directory; small responses print in full, while larger responses print a summary unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

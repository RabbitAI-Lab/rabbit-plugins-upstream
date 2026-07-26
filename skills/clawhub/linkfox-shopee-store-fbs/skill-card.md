## Description: <br>
Queries Shopee Brazil FBS shop enrollment, invoice error, shop block, and SKU block status through LinkFox's Shopee developer proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers with authorized Shopee Brazil shops use this skill to check FBS enrollment, invoice error, shop block, and SKU block status. It is useful when an agent needs to retrieve status data through provided Python scripts and inspect the resulting JSON. <br>

### Deployment Geography for Use: <br>
Global, for Shopee Brazil FBS stores <br>

## Known Risks and Mitigations: <br>
Risk: Full authenticated Shopee business API responses are saved locally, which can expose store status data in shared workspaces or repository directories. <br>
Mitigation: Run the skill in a private workspace, keep generated linkfox data out of source control, restrict file access, and delete generated response files after use. <br>
Risk: Repeated queries may have billing or credit implications depending on the active LinkFox/Shopee policy. <br>
Mitigation: Confirm the applicable billing policy before repeated runs and avoid automatic retries or broad exploratory querying. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-fbs) <br>
- [API reference](references/api.md) <br>
- [Shopee FBS shop enrollment status API](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_enrollment_status?module=126&type=1) <br>
- [Shopee FBS shop invoice error API](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_invoice_error?module=126&type=1) <br>
- [Shopee FBS shop block status API](https://open.shopee.com/documents/v2/v2.fbs.query_br_shop_block_status?module=126&type=1) <br>
- [Shopee FBS SKU block status API](https://open.shopee.com/documents/v2/v2.fbs.query_br_sku_block_status?module=126&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, files, shell commands, guidance] <br>
**Output Format:** [JSON responses saved to local files, with stdout JSON for small responses or a text summary for large responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are written under a linkfox date/session data directory; --inline can force full stdout output.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

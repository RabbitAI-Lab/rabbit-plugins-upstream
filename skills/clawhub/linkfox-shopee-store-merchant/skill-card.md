## Description: <br>
Helps agents query authorized Shopee cross-border merchant information, shop lists, warehouse data, eligible shops, and prepaid accounts through LinkFox's Shopee Merchant API tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and commerce operators use this skill to retrieve Shopee merchant profile details, linked shops, warehouse information, and prepaid account data for authorized cross-border seller accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Complete Shopee merchant API responses may be saved locally and can contain sensitive account or store data. <br>
Mitigation: Install only where local retention is acceptable, review and manage generated linkfox data directories, and avoid highly sensitive accounts unless this storage is approved. <br>
Risk: The skill uses LinkFox/Shopee merchant credentials and may involve point consumption for repeated API calls. <br>
Mitigation: Use appropriate credentials, confirm point consumption before repeated calls, and avoid automated retries or broad probing. <br>


## Reference(s): <br>
- [Skill API Reference](references/api.md) <br>
- [Shopee Merchant get_merchant_info](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1) <br>
- [Shopee Merchant get_shop_list_by_merchant](https://open.shopee.com/documents/v2/v2.merchant.get_shop_list_by_merchant?module=93&type=1) <br>
- [Shopee Merchant get_merchant_warehouse_list](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_warehouse_list?module=93&type=1) <br>
- [Shopee Merchant get_merchant_warehouse_location_list](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_warehouse_location_list?module=93&type=1) <br>
- [Shopee Merchant get_warehouse_eligible_shop_list](https://open.shopee.com/documents/v2/v2.merchant.get_warehouse_eligible_shop_list?module=93&type=1) <br>
- [Shopee Merchant get_merchant_prepaid_account_list](https://open.shopee.com/documents/v2/v2.merchant.get_merchant_prepaid_account_list?module=93&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts emit JSON responses or summaries and save full responses as local JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox/Shopee merchant credentials. Evidence indicates complete merchant API responses may be saved locally, so users should manage generated linkfox data directories and clarify point consumption before repeated calls.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

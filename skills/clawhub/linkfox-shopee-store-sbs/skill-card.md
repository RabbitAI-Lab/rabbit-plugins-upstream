## Description: <br>
Provides Shopee SBS warehouse and inventory queries for authorized stores through LinkFox's Shopee developer proxy, covering bound warehouses, current inventory, expiry reports, stock aging, and stock movement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators working with authorized Shopee stores use this skill to retrieve SBS warehouse, inventory, aging, expiry, and stock-movement data. It is intended for store-specific operational analysis where the user has valid LinkFox and Shopee authorization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Complete Shopee merchant API responses are saved on the local machine, which may expose store inventory or warehouse data if the workspace is shared. <br>
Mitigation: Use the skill only in a private workspace and review or delete generated linkfox data folders after use. <br>
Risk: Inline output can place large or sensitive SBS responses directly into the agent transcript. <br>
Mitigation: Avoid inline output for large or sensitive results and inspect saved JSON files selectively with tools such as jq. <br>
Risk: Repeated SBS queries may have unclear point-cost behavior despite conflicting artifact notes about cost. <br>
Mitigation: Confirm point-cost behavior with the publisher before repeated queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-sbs) <br>
- [Shopee SBS get_bound_whs_info documentation](https://open.shopee.com/documents/v2/v2.sbs.get_bound_whs_info?module=124&type=1) <br>
- [Shopee SBS get_current_inventory documentation](https://open.shopee.com/documents/v2/v2.sbs.get_current_inventory?module=124&type=1) <br>
- [Shopee SBS get_expiry_report documentation](https://open.shopee.com/documents/v2/v2.sbs.get_expiry_report?module=124&type=1) <br>
- [Shopee SBS get_stock_aging documentation](https://open.shopee.com/documents/v2/v2.sbs.get_stock_aging?module=124&type=1) <br>
- [Shopee SBS get_stock_movement documentation](https://open.shopee.com/documents/v2/v2.sbs.get_stock_movement?module=124&type=1) <br>
- [Artifact API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [JSON responses saved to local files with stdout JSON or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes complete API responses under a local linkfox data directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

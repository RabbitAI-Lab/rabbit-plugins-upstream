## Description: <br>
Helps agents manage authorized Shopee Shop Flash Sale campaigns through LinkFox scripts for time-slot lookup, creation, listing, item management, updates, and deletion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace operators, and developers use this skill to administer Shop Flash Sale activity for already authorized Shopee stores. It is suited for retrieving eligible time slots and campaign details, adding or updating sale items, and deleting campaigns or items when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, add to, or delete Shopee Shop Flash Sale campaigns for an authorized store. <br>
Mitigation: Confirm every write or delete action, including target shop, campaign, item list, and requested payload, before running the corresponding script. <br>
Risk: Full API responses may be persisted locally and can include operational store or campaign data. <br>
Mitigation: Use a controlled workspace and periodically delete generated linkfox response archives, especially on shared, backed-up, or reused machines. <br>


## Reference(s): <br>
- [Skill API Reference](references/api.md) <br>
- [Shopee Shop Flash Sale API](https://open.shopee.com/documents/v2/v2.shop_flash_sale.get_time_slot_id?module=123&type=1) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop-flash-sale) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON responses saved to local files with stdout summaries or full inline JSON when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts may call LinkFox gateway APIs for an authorized Shopee store and write response archives under a local linkfox directory.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

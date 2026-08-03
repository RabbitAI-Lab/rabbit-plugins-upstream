## Description: <br>
Helps agents retrieve authorized TikTok Shop stores and warehouse lists for ERP logistics workflows using LinkFox's TikTok Shop integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and developers use this skill to select authorized TikTok Shop stores, resolve shop ciphers, and retrieve warehouse IDs and warehouse status for product inventory workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generic logistics proxy can make credentialed calls beyond the named warehouse-list workflow. <br>
Mitigation: Use get_warehouse_list and get_authorized_shops for normal work; reserve logistics_proxy.py for reviewed advanced cases. <br>
Risk: Gateway URL overrides can redirect credentialed calls to an unexpected endpoint. <br>
Mitigation: Do not override the gateway URL unless the endpoint is controlled and approved for the deployment. <br>
Risk: Shop and warehouse outputs can include operational identifiers, addresses, or contact details. <br>
Mitigation: Show only the fields needed for the task, redact unnecessary contact details, and never expose full access tokens. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-logistics) <br>
- [TikTok Shop ERP Logistics API Reference](references/api.md) <br>
- [Get Authorized Shops](references/apis/get_authorized_shops.md) <br>
- [Get Warehouse List](references/apis/get_warehouse_list.md) <br>
- [TikTok Shop Get Warehouse List Documentation](https://partner.tiktokshop.com/docv2/page/get-warehouse-list-202309) <br>
- [TikTok Shop Get Authorized Shops Documentation](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) <br>
- [TikTok Shop Seller Authorization Guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [JSON responses and concise Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include shop and warehouse identifiers, names, warehouse types, status fields, and address summaries; should not expose full access tokens.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

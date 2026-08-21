## Description:

Helps agents call LinkFox-backed TikTok Shop ERP logistics APIs to discover authorized shops, resolve shop ciphers, and retrieve shop warehouse lists for inventory and logistics workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to list TikTok Shop warehouses, obtain warehouse IDs, and prepare downstream product or inventory updates. It depends on a separate LinkFox TikTok Shop auth skill for store selection and token handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broader LinkFox ERP access than warehouse lookup alone through shop discovery and a generic logistics/authorization proxy.

Mitigation: Install only when that scope is acceptable; prefer a narrower release that removes the generic proxy or limits allowed paths to the warehouse endpoint.

Risk: Gateway and token handling rely on a LinkFox service and a separate authentication skill.

Mitigation: Confirm the auth dependency is installed, keep access tokens out of agent-visible output, and review gateway errors before retrying operations.

Risk: Warehouse IDs and status fields may affect downstream product inventory decisions.

Mitigation: Validate warehouse type, effect_status, and default status with the seller before using returned IDs for listing or stock updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-logistics)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [TikTok Shop ERP Logistics API Reference](references/api.md)
- [Get Authorized Shops](references/apis/get_authorized_shops.md)
- [Get Warehouse List](references/apis/get_warehouse_list.md)
- [TikTok Shop Get Authorized Shops documentation](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Get Warehouse List documentation](https://partner.tiktokshop.com/docv2/page/get-warehouse-list-202309)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include warehouse IDs, shop ciphers, warehouse type/status fields, address summaries, and gateway error details.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

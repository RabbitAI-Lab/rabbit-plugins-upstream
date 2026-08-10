## Description:

Shopee（虾皮）SBS 仓储服务（与 linkfox-shopee-store-auth 同系列），经 /shopee/developerProxy 转发 Shopee Open API SBS 模块全部 5 个接口：get_bound_whs_info、get_current_inventory、get_expiry_report、get_stock_aging、get_stock_movement。当用户提到 Shopee SBS、仓储库存、绑定仓库、get_bound_whs_info、库龄报表、效期报表、库存变动 时触发。即使未明确提及"SBS"，只要涉及已授权 Shopee 店铺的 SBS 仓储与库存数据查询，也应触发。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to query authorized Shopee SBS warehouse and inventory data, including bound warehouses, current inventory, expiry reports, stock aging, and stock movement. It is intended for workflows that already use LinkFox Shopee store authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends API-key-authenticated requests through LinkFox-controlled endpoints and supports configurable gateway URLs.

Mitigation: Review LINKFOX_TOOL_GATEWAY, SHOPEE_API_BASE_URL, LINKFOX_AGENT_API_URL, LINKFOX_LOGIN_API_URL, and LINKFOX_AGENT_USER_API_URL before use, and keep API keys in environment variables only.

Risk: SBS responses may include sensitive warehouse, stock, expiry, or movement data and are saved as plaintext JSON files.

Mitigation: Store the workspace in an appropriate access-controlled location and delete generated linkfox response files when they are no longer needed.

Risk: Auth, billing, order, and API-key issuance flows may be invoked when credentials are missing or quota errors occur.

Mitigation: Confirm user intent before account, billing, or payment actions and review all onboarding output before applying configuration changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-sbs)
- [SBS API Reference](artifact/references/api.md)
- [Onboarding and Billing Guidance](artifact/references/onboarding.md)
- [Shopee get_bound_whs_info Documentation](https://open.shopee.com/documents/v2/v2.sbs.get_bound_whs_info?module=124&type=1)
- [Shopee get_current_inventory Documentation](https://open.shopee.com/documents/v2/v2.sbs.get_current_inventory?module=124&type=1)
- [Shopee get_expiry_report Documentation](https://open.shopee.com/documents/v2/v2.sbs.get_expiry_report?module=124&type=1)
- [Shopee get_stock_aging Documentation](https://open.shopee.com/documents/v2/v2.sbs.get_stock_aging?module=124&type=1)
- [Shopee get_stock_movement Documentation](https://open.shopee.com/documents/v2/v2.sbs.get_stock_movement?module=124&type=1)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses saved to local files, with stdout JSON or summaries and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LinkFox API-key authentication; scripts can emit full responses with --inline and otherwise summarize large responses after saving them.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

查询医疗器械品牌、设备型号和耗材相关招中标数据，并返回设备中标单价、参数、采购单位、供应商和市场分析结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sourcing, sales, and market-analysis users can use this skill to search Chinese medical-device and consumables bidding records, compare purchasers and suppliers, inspect company profiles, and analyze brand or model price trends. It is also useful for account balance checks tied to the vendor API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated procurement queries are sent to a third-party vendor service.

Mitigation: Review the vendor service before use and configure your own ZLBX_API_KEY when possible.

Risk: Optional trial registration can transmit device-derived fields and write an API key to local configuration.

Mitigation: Use auto-registration only after explicit user consent; prefer a preconfigured environment variable for managed environments.

Risk: Company contact lookup may expose or process business contact data.

Mitigation: Use contact-related queries only for legitimate business purposes and avoid unnecessary retrieval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON request examples, REST API calls, and summarized procurement-data results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY for authenticated vendor API requests and may store an API key in ~/.zlbx/config.json after user-approved trial registration.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

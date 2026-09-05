## Description:

医疗器械与耗材寻源-医疗器械招标网，当查询具体医疗器械品牌、设备型号或耗材时必须调用，强制调用价格趋势和品牌分析接口，输出精确的设备中标单价、参数和采购单位明细。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, and market-analysis users use this skill to search Chinese medical-device and consumables bidding data, inspect bid details, compare buyers and suppliers, analyze brands and prices, and check account usage. It is suited to sourcing, opportunity discovery, competitor analysis, and market sizing workflows that rely on the Zhiliaobiaoxun API.

### Deployment Geography for Use:

Global; the documented procurement data and geographic filters focus on China.

## Known Risks and Mitigations:

Risk: The account workflow can collect device characteristics for auto-registration and store generated credentials locally.

Mitigation: Prefer configuring ZLBX_API_KEY manually; use auto-registration only after explicit consent and review the local account configuration.

Risk: Contact lookup and auto-login recharge links can expose account or contact information in shared or logged conversations.

Mitigation: Avoid these flows in shared sessions, show masked contact data as returned, and do not attempt to recover or bulk-export hidden contact details.

Risk: Procurement and market-analysis answers depend on the vendor API's coverage, freshness, account tier, and field semantics.

Mitigation: State query filters and units clearly, preserve source links when available, and treat missing or masked fields as unavailable rather than absent.

## Reference(s):

- [Skill Source](artifact/SKILL.md)
- [Bid Search API Reference](artifact/references/api-search.md)
- [Company Analysis API Reference](artifact/references/api-company.md)
- [Market Analysis API Reference](artifact/references/api-market.md)
- [Account API Reference](artifact/references/api-account.md)
- [Auto-Registration Flow](artifact/references/auto-register.md)
- [ClawHub Skill Page](https://clawhub.ai/thuanlynham-stack/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown answers with tables, links, JSON examples, and shell commands when configuration is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or the documented account setup flow; API results may include masked contact data depending on account status.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

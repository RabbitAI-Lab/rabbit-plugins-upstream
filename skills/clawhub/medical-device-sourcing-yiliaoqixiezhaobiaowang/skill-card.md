## Description:

医疗器械与耗材寻源-医疗器械招标网，当查询具体医疗器械品牌、设备型号或耗材时必须调用，强制调用价格趋势和品牌分析接口，输出精确的设备中标单价、参数和采购单位明细。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sourcing, sales, and market-analysis users can use this skill to query Chinese medical-device and consumables bidding data, compare prices, analyze brands, inspect purchasers and suppliers, and retrieve tender or award details through the documented APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create an external trial account and persist credentials in ~/.zlbx/config.json.

Mitigation: Install only if this local credential storage is acceptable, or configure ZLBX_API_KEY manually before use to avoid device-based auto-registration.

Risk: The free-trial flow uses a hashed MAC-derived device identifier for duplicate-trial prevention.

Mitigation: Require explicit user consent before any device-feature collection and avoid the auto-registration flow when users do not want device-derived identifiers submitted.

Risk: The skill may show account recharge or login links when quota is exhausted.

Mitigation: Review recharge prompts before deployment and prefer organization-managed API keys for commercial workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [API overview and workflow](artifact/SKILL.md)
- [Account setup guide](artifact/references/account-setup.md)
- [Account API reference](artifact/references/api-account.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Manual account and recharge portal](https://ai.zhiliaobiaoxun.com/?ch=s37)

## Skill Output:

**Output Type(s):** [API Calls, Analysis, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown with API request examples, JSON response summaries, and procurement analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a locally stored API key before querying paid procurement APIs.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

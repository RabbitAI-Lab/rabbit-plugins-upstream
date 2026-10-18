## Description:

帮助用户检索招投标商机，并结合企业、竞对和历史中标数据研判项目与市场。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

采购和投标团队使用该技能查找中国招投标项目、分析采购方与供应商，并参考历史价格和企业信息评估机会。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service receives authenticated tender queries and account usage data.

Mitigation: Use only if you trust the service with these requests and review account activity.

Risk: Trial registration collects a device fingerprint and stores a credential locally.

Mitigation: Prefer your own ZLBX_API_KEY; decline registration without informed consent and review ~/.zlbx/config.json after use.

Risk: Embedded instructions request authenticated account and version checks.

Mitigation: Review the skill's account-check behavior before enabling it and do not disclose API keys in responses.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/tender-opportunity-biaobiaoda)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API](artifact/references/api-search.md)
- [Company analysis API](artifact/references/api-company.md)
- [Company registry data guidance](artifact/references/api-registry.md)
- [Market analysis API](artifact/references/api-market.md)
- [Account API](artifact/references/api-account.md)
- [Trial registration guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated queries require a service API key; some queries consume credits.]

## Skill Version(s):

2.0.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

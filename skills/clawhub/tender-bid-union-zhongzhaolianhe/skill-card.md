## Description:

通过知了标讯的招投标数据，协助分析市场规模、采购趋势、主要参与者及历史中标价格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

市场研究人员、采购团队及企业分析师可查询中国招投标记录，汇总地区和行业趋势、领先采购方与供应商、品牌份额及历史中标价格。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration collects device platform, architecture and a hashed MAC address.

Mitigation: Obtain informed user consent before registration; offer manual signup if declined.

Risk: An auto-issued API key is stored on the device and used for external requests.

Mitigation: Review local credential storage and restrict access to ~/.zlbx/config.json; use an existing key when preferred.

Risk: API requests may consume quota, and account balance and update checks may run automatically.

Mitigation: Review these automatic calls and acknowledgement behavior before use; limit data queries to those requested and monitor quota.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/tender-bid-union-zhongzhaolianhe)
- [知了标讯 Skill 文档](https://ai.zhiliaobiaoxun.com/docs/skill)
- [市场分析接口说明](artifact/references/api-market.md)
- [自动注册与隐私说明](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available service records and may consume API quota.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

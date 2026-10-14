## Description:

帮助查询和分析招投标公告、企业信息与采购市场数据，默认检索江苏省并尊重用户指定的地区。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购、投标与市场分析人员可查询招标和中标公告、项目进展、企业工商与中标记录、竞争格局及历史成交价格；江苏省是默认检索范围，用户可指定其他地区。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an API key and may read or create a local configuration file containing it.

Mitigation: Configure your own ZLBX_API_KEY if preferred; protect ~/.zlbx/config.json and do not disclose the key in responses.

Risk: Optional trial-account registration sends limited device characteristics to zhiliaobiaoxun.com.

Mitigation: Seek informed consent before registration; configure an API key manually to avoid device-based registration.

Risk: Some data queries consume account credits.

Mitigation: Run only user-requested queries, avoid automatic pagination or extra lookups, and check account balance when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-jiangsu)
- [知了标讯](https://ai.zhiliaobiaoxun.com/?ch=s151)
- [标讯查询 API 说明](artifact/references/api-search.md)
- [企业数据 API 说明](artifact/references/api-company.md)
- [市场分析 API 说明](artifact/references/api-market.md)
- [首次注册说明](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States the applied search scope and distinguishes returned records from total matches.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

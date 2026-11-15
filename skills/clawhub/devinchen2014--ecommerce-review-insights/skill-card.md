## Description:

当用户需要归纳商品评价中的优缺点、购买顾虑和改进建议时使用。支持各平台提供的评价文本或表格，也可通过小红书商品链接或sku_id在线分析评价。输出带原话依据、评价条数与范围说明的主题表；已有资料可直接分析。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要了解商品体验的消费者、运营人员和产品团队，基于提供的评价文本、表格或支持的小红书商品数据，归纳评价主题、购买顾虑和可核查的改进建议，并说明样本范围与证据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes the mutable `socialdatax-skills@latest` CLI release, which may use API credentials; the security scan was partial.

Mitigation: Review and trust the CLI package and its updates before use. Keep SOCIALDATAX_API_KEY in the designated private environment, and never place the key in chat, logs, command history, skill files, or project files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-review-insights)
- [SocialDataX API information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown theme table with supporting quotes, sample counts, scope notes, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses available review records and identifies sample limits; preserves row numbers or review IDs when available.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

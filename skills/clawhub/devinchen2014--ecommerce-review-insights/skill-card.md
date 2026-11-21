## Description:

当用户需要归纳商品评价中的优缺点、购买顾虑和改进建议时使用。支持各平台提供的评价文本或表格，也可通过小红书商品链接或sku_id在线分析评价。输出带原话依据、评价条数与范围说明的主题表；已有资料可直接分析。来自社媒数据助手 SocialDataX。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要了解商品体验的用户和团队，分析已有评价文本或表格，也可按商品链接或 sku_id 获取小红书商品评价。整理优缺点、顾虑和改进建议，并附样本范围、条数和原话依据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly invokes a mutable latest-version CLI; a compromised release could expose credentials or local files.

Mitigation: Review the CLI release, use a fixed version, and apply dependency integrity controls before installation or use. Treat the scan as incomplete because some referenced paths were missing.

## Reference(s):

- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown summary and theme table with sample counts, evidence excerpts, limitations, and improvement suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites review row numbers or IDs where available; reports sample scope and avoids unsupported population-wide claims.]

## Skill Version(s):

1.0.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

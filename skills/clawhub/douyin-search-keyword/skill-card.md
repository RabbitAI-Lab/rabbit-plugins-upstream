## Description:

抖音公开数据只读：支持关键词搜索、博主作品、作品详情、评论和热榜查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

短视频运营、品牌团队、内容分析人员和产品运营人员可用它查询抖音公开内容，跟踪热点与对标账号，并分析单条作品和评论中的受众反馈。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to www.guaikei.com, and the remote service's data handling and billing have not been independently verified.

Mitigation: Use a dedicated provider token, send only queries you are comfortable sharing, and check API charges.

Risk: Query results may be saved in local logs.

Mitigation: Remove saved result logs when they are no longer needed.

## Reference(s):

- [Demand mining guidance](references/demand-mining.md)
- [Command options](references/options.md)
- [抖音数据技能官网](https://www.guaikei.com)
- [ClawHub skill release](https://clawhub.ai/um-why/skills/douyin-search-keyword)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON results with concise analytical summaries in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A consistent JSON envelope contains command results; result details vary by query type. Results may be saved locally in the skill's logs directory. Summaries should highlight key fields rather than reproduce full records.]

## Skill Version(s):

1.4.2 (source: SKILL.md frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

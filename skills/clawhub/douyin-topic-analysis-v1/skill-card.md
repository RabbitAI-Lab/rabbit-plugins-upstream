## Description:

帮助内容运营者通过抖音公开数据搜索视频与账号、查看热榜和作品详情、分析评论，为选题与竞品研究整理结构化数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

内容运营者、创作者及品牌研究人员可用此技能查询抖音公开视频、账号、热榜和评论数据，并据此整理选题、竞品与舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and supplied Douyin links or IDs are sent to guaikei.com, and the skill requires a service API token.

Mitigation: Use the service only when the user intends to share those query details with it, and configure the token through the environment as documented.

Risk: ClawScan reports a benign verdict with medium confidence, flags keyword-based account discovery as an undeclared capability, and fully scanned only 31 of 53 components.

Mitigation: Review the account-search behavior and remaining unverified components before enabling the skill.

## Reference(s):

- [抖音选题分析技能页面](https://clawhub.ai/why20261/skills/douyin-topic-analysis-v1)
- [抖音数据服务](https://www.guaikei.com)
- [需求挖掘指南](artifact/references/demand-mining.md)
- [公域获客指南](artifact/references/customer-acquisition.md)
- [输出契约](artifact/references/contract.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis, Markdown]

**Output Format:** [Structured JSON data with agent-written summaries or tables as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a configured API token to retrieve public Douyin data; queries and supplied links are sent to the third-party service.]

## Skill Version(s):

1.5.0 (source: artifact/SKILL.md frontmatter, artifact/package.json, artifact/references/changelog.md, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

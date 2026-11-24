## Description:

提供抖音公开内容搜索、账号作品与评论查询及实时热榜数据，供选题、竞品和舆情分析使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

内容运营人员可用此技能搜索抖音公开视频、查询账号作品与评论并查看热榜，用于选题研究、竞品分析和舆情梳理。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account search is available, and requests may send supplied keywords, links, or identifiers to the external guaikei.com service.

Mitigation: Make the external request clear before running it, confirm the requested account-search scope, and provide only the public identifiers needed for the query.

Risk: The security review reports medium confidence and partial inspection, so some files were not fully inspected.

Mitigation: Review the packaged skill files and confirm the requested public-data operations before installation and use.

## Reference(s):

- [意图路由](references/routing.md)
- [输出契约](references/contract.md)
- [需求挖掘](references/demand-mining.md)
- [公域获客](references/customer-acquisition.md)
- [错误处理](references/errors.md)
- [服务与令牌配置](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON data with concise analysis or guidance when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public Douyin search, account, post, comment, detail, and hot-list data; results can support topic, competitor, sentiment, and demand analysis.]

## Skill Version(s):

1.5.0 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

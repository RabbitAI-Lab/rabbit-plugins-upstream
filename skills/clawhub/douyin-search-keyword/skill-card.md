## Description:

读取抖音公开内容，执行关键词与用户搜索、作品和评论查询及热榜跟踪，并返回结构化 JSON，供竞品、舆情与需求分析使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营、品牌与增长团队可检索抖音公开视频、账号、作品、评论和热榜，并整理竞品、舆情、选题、需求或公域线索分析所需的结构化数据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence: 22 of 54 components were only partially inspected, and the guidance notes a third-party data-sharing concern.

Mitigation: Use only non-sensitive public keywords and links; consider whether sending them to guaikei.com and the remaining scan uncertainty are acceptable before use.

## Reference(s):

- [Service and API access](https://www.guaikei.com)
- [Output contract](artifact/references/contract.md)
- [Command options](artifact/references/options.md)
- [Intent routing](artifact/references/routing.md)
- [Demand mining guidance](artifact/references/demand-mining.md)
- [Customer acquisition guidance](artifact/references/customer-acquisition.md)
- [FAQ and setup](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON results with concise summaries for agent use]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fields vary by Douyin query; a cost estimate may be included. Results are not saved by default.]

## Skill Version(s):

1.5.1 (source: server-resolved release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

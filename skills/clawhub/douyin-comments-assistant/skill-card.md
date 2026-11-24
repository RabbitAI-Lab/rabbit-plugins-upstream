## Description:

查询抖音公开视频、图文、创作者作品、热榜与评论，并返回结构化数据供内容研究和分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

内容运营人员和分析师可用它检索抖音公开内容与账号、查看作品指标和评论，支持选题研究、竞品观察和舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and Douyin links or IDs may be sent to a third-party API, and the skill supports keyword-based account discovery.

Mitigation: Use account discovery only when intended, avoid sensitive search terms or identifiers, and review the provider's data-handling terms before querying.

Risk: The security review reports medium confidence and incomplete file inspection.

Mitigation: Review the skill's behavior and source files before installation if that inspection gap affects your decision.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-comments-assistant)
- [Guaikei service website](https://www.guaikei.com)
- [Data and output contract](artifact/references/contract.md)
- [Comment analysis guide](artifact/references/demand-mining.md)
- [Customer acquisition guide](artifact/references/customer-acquisition.md)
- [FAQ](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public Douyin search results, creator and post details, trend data, and comments; an agent can use these records for summaries and analysis.]

## Skill Version(s):

1.5.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

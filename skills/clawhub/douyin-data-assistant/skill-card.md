## Description:

检索抖音公开视频、用户、作品详情、评论与热榜，并返回结构化 JSON，供内容和账号分析使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

短视频运营者、内容分析人员和营销团队可用它检索抖音公开作品与账号、查看作品和评论并追踪热点，再将结构化数据用于选题、竞品研究和舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports an additional keyword-based account-search capability and incomplete static analysis; using the skill sends supplied Douyin links or IDs to a third-party API.

Mitigation: Review the account-search behavior and decide whether the supplied links or IDs are appropriate to share with the API provider before use.

## Reference(s):

- [Output contract](artifact/references/contract.md)
- [Command options](artifact/references/options.md)
- [Command routing](artifact/references/routing.md)
- [Errors and limits](artifact/references/errors.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are structured records; the results field may be an array or an object depending on the command.]

## Skill Version(s):

1.5.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

查询抖音公开视频、图文、创作者作品、作品详情、评论和实时热榜，并返回结构化数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

面向短视频运营、品牌、增长和内容分析人员，用于发现抖音热点、检索公开内容与创作者，并分析作品互动和评论。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and supplied Douyin links or IDs are sent to the third-party GUAIKEI API.

Mitigation: Only submit public data and inputs you are comfortable sharing with GUAIKEI; avoid private or sensitive identifiers.

Risk: Some artifact content was only partially analyzed, so scan coverage is incomplete.

Mitigation: Review the skill's behavior and API calls before use; a benign scan verdict is not a guarantee of zero risk.

Risk: Query results are saved in the skill's logs directory for most commands.

Mitigation: Review the local log contents and storage location, and remove result files when they are no longer needed.

## Reference(s):

- [GUAIKEI service and API access](https://www.guaikei.com)
- [Output contract](references/contract.md)
- [Command options](references/options.md)
- [Error handling](references/errors.md)
- [ClawHub release listing](https://clawhub.ai/why20261/skills/douyin-real-hot-rise)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON records, with concise summaries or analysis for the requested data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be arrays or objects depending on the query; detailed records can include public content, creator, engagement, and comment data.]

## Skill Version(s):

1.5.0 (source: artifact/SKILL.md frontmatter, artifact/references/changelog.md, artifact/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

查询微信视频号作品评论，支持分页获取评论及展开二级回复。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员可查询指定微信视频号作品的评论和回复，整理反馈并导出较大的结果集。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt global, unpinned qhkit installation or local Node setup.

Mitigation: Review and approve dependency installation and PATH changes; prefer a pinned qhkit version.

Risk: The service requires an API token and charges credits for comment lookups.

Mitigation: Configure the token deliberately and approve each paid call and its estimated credit cost before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-comments)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise comment summary with optional tabular export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports paginated comments and replies; results with 10 or more records are delivered as a table file.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

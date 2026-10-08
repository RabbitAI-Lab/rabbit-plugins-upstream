## Description:

帮助中国中小学教师设计分层、限时的作业任务卡，并提供评分标准与反馈模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中国大陆中小学教师用它根据班级学情设计分层作业、预计完成时间、评分标准和反馈模板；没有分层数据时只提供基础版草稿，正式布置前须由教师审定。

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Class or student information could be exposed through inappropriate workspace permissions or consent settings.

Mitigation: Confirm class-workspace permissions and consent settings against school policy before use; keep shared feedback de-identified.

Risk: AI-generated questions may contain errors if assigned without review.

Mitigation: Have teachers check and verify generated questions before formally assigning them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [作业评分标准模板](artifact/references/assignment-rubric.md)
- [AI-generated question checks](artifact/shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown task cards, scoring rubrics, and feedback templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes estimated time per question; does not automatically grade student work.]

## Skill Version(s):

2.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

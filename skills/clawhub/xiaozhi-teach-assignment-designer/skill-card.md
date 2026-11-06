## Description:

为教师生成按难度分层、标注预计用时的作业任务卡、评分标准和反馈模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

教师使用此技能设计有难度梯度、可批改且时长可控的课后作业，并生成评分标准与学生反馈。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated questions and time estimates may be inaccurate.

Mitigation: Review questions and timing suggestions before assigning the work to students.

Risk: Homework records may contain student information.

Mitigation: Use aliases and aggregate results, confirm consent before sharing, and use the session opt-out when records should not be accessed or saved.

Risk: Active examination questions or answer keys may be confidential.

Mitigation: Do not provide exam materials before all relevant sessions are complete; use approved source material or teacher-created practice instead.

Risk: Host storage protections and separately installed companion skills were not verified.

Mitigation: Check the host's storage protections and companion-skill safeguards before using student records across tools.

## Reference(s):

- [作业设计师（ClawHub release）](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-assignment-designer)
- [发布者 qizhitang](https://clawhub.ai/user/qizhitang)
- [作业评分标准与分层任务卡模板](artifact/references/assignment-rubric.md)
- [AI 生成题目自检指南](artifact/shared/ai-item-check.md)
- [危机例外处置指南](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language task cards, scoring rubrics, feedback templates, and completion summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include per-task time estimates and tiered versions when class information is available; generated questions require teacher review.]

## Skill Version(s):

2.12.6 (source: SKILL.md frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

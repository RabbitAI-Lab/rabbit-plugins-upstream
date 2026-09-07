## Description:

帮独立教师把作业从收上来变成跟到底：登记作业、追踪七档状态、归纳错因，并输出下节课预诊断与跟进建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to register assigned homework, track submission and correction status, classify recurring error causes, and prepare concise next-lesson follow-up guidance. It is intended for low-sensitivity homework metadata and keeps grading, parent messaging, and lesson logging in separate workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Irreversible deletion of homework tracking records can remove evidence needed for follow-up.

Mitigation: Require explicit teacher confirmation and deletion scopes such as student alias plus date range or assignment before deleting records.

Risk: Homework tracking may expose student information if platforms share data too broadly.

Mitigation: Use student aliases, store only limited homework metadata, avoid original homework answers, and enforce consent checks before cross-skill or parent-facing sharing.

Risk: Weak-point labels may be over-applied from repeated homework errors.

Mitigation: Keep threshold hits as evidence first and update confirmed student weaknesses only after teacher approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [作业完成度追踪视图模板](references/completion-tracking-views.md)
- [错题回流清单模板](references/error-reflow-checklist-template.md)
- [下节课预诊断输出模板](references/pre-diagnosis-output-template.md)
- [学员作业画像模板](references/student-homework-profile-template.md)
- [全库统一词表](shared/vocab.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured field updates for homework tracking records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should use student aliases, avoid original homework answers, and require teacher confirmation before irreversible deletion or weak-point updates.]

## Skill Version(s):

2.1.12 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

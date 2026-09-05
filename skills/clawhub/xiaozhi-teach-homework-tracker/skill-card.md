## Description:

帮独立教师把作业从"收上来"变成"跟到底"：登记、追状态、归错因、导出下节课讲什么。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to track assigned homework, completion status, error categories, repeated weaknesses, and next-lesson focus while keeping final judgments and family communication under teacher control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Homework follow-up records can become sensitive if teachers enter real names, answer text, or family details.

Mitigation: Use aliases, avoid real names and answer text, and keep records limited to homework status, error categories, knowledge points, submission timing, and follow-up actions.

Risk: Incorrectly labeling a student's persistent weakness could affect later reports or family communication.

Mitigation: Store threshold hits as evidence first and write student-card weaknesses only after explicit teacher confirmation.

Risk: Sharing homework status or student observations with parents without consent could expose student information.

Mitigation: Check parent-communication and cross-skill sharing consent before parent-facing output, and use the delete, pause, export, and sharing controls described in the artifact.

Risk: Generated practice items used for follow-up may contain errors if accepted without review.

Mitigation: Apply the bundled AI item self-check and label generated items as requiring teacher verification before they are stored or sent to students.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [ClawHub Publisher Profile](https://clawhub.ai/user/qizhitang)
- [作业完成度追踪视图模板](references/completion-tracking-views.md)
- [错题回流清单模板](references/error-reflow-checklist-template.md)
- [顽固弱项档案模板](references/persistent-weakness-file-template.md)
- [下节课预诊断输出模板](references/pre-diagnosis-output-template.md)
- [学员作业画像模板](references/student-homework-profile-template.md)
- [全库统一词表](shared/vocab.md)
- [独立教师工作空间 Schema](shared/solo-teacher-workspace.schema.json)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured workspace record fields and teacher-facing templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces homework status views, error-reflow checklists, persistent-weakness evidence, next-lesson diagnosis, and alias-based records with teacher confirmation gates.]

## Skill Version(s):

2.1.6 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

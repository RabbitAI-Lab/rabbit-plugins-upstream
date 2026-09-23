## Description:

帮独立教师把作业从“收上来”变成“跟到底”：登记、追状态、归错因、导出下节课讲什么。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 independent teachers use this skill to track assigned homework, submission status, error dimensions, repeated weaknesses, and next-lesson follow-up priorities. The skill is designed for teacher-controlled records and analysis, not for grading, messaging families, or replacing teacher judgment.

### Deployment Geography for Use:

Global, with localization required before use outside mainland China

## Known Risks and Mitigations:

Risk: The skill handles K12 learner homework records and repeated-weakness labels that may affect student or guardian perceptions.

Mitigation: Use aliases and low-sensitivity fields only, keep raw homework text and answers out of persistent records, and require teacher confirmation before writing repeated weaknesses to student cards.

Risk: Default crisis referral numbers, curriculum assumptions, and consent rules are designed for mainland China.

Mitigation: Localize crisis channels, curriculum mappings, and minor-data consent requirements before deployment in other regions.

Risk: Generated follow-up questions or validation items could contain mistakes.

Mitigation: Apply the bundled AI item self-check and mark generated items for teacher verification before they are stored or used with learners.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [作业完成度追踪视图模板](artifact/references/completion-tracking-views.md)
- [错题回流清单模板](artifact/references/error-reflow-checklist-template.md)
- [顽固弱项档案模板](artifact/references/persistent-weakness-file-template.md)
- [下节课预诊断输出模板](artifact/references/pre-diagnosis-output-template.md)
- [学员作业画像模板](artifact/references/student-homework-profile-template.md)
- [全库统一词表](artifact/shared/vocab.md)
- [SoloTeacherWorkspace schema](artifact/shared/solo-teacher-workspace.schema.json)
- [危机例外](artifact/shared/crisis-exception.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports, teacher-facing guidance, and structured workspace field updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses aliases and low-sensitivity homework fields; repeated-weakness writebacks require teacher confirmation.]

## Skill Version(s):

2.2.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

把独立教师的讲义、题目、讲评话术和错因案例整理成可检索、可标注版权状态并可复用的教学资源库。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to save, search, adapt, and reuse teaching materials while tracking tags, copyright status, AI-generated item verification, and privacy-safe student-case notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent learner-linked education records can expose minor-student data if field permissions are broader than the skill needs.

Mitigation: Require field-level permissions only for the stated read fields and the resourceLibraryIndex write path before installation.

Risk: usageNotes examples that include student aliases or exact dates can create reidentification risk.

Mitigation: Revise examples so usageNotes contain only aggregate, resource-level use facts without aliases, exact dates, scores, or individual weak-point histories.

Risk: Cross-skill sharing can disclose learner or resource context without explicit consent.

Mitigation: Make sharing deny-by-default unless an explicit cross-skill consent value is available and true.

Risk: AI-generated exercises can be incorrect or unsuitable if reused before teacher verification.

Mitigation: Keep aiGenerated items marked as unverified and exclude them from student-use candidates until a teacher has checked and marked verifiedByTeacher true.

## Reference(s):

- [资源五大类：用途、入库要求与示例](artifact/references/resource-entry-examples.md)
- [资源标签、检索与脱敏](artifact/references/resource-categorization.md)
- [版权标注模板](artifact/references/copyright-annotation-template.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [全库统一词表](artifact/shared/vocab.md)
- [SoloTeacherWorkspace schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured resource-entry fields, checklist items, and copyright or verification annotations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include resource tags, match rationale, copyright status, AI-generated verification notices, and privacy-safe usage notes.]

## Skill Version(s):

2.1.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

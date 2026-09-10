## Description:

A Chinese-language teaching guide that helps language arts teachers design writing assignments, set essay review criteria, plan review lessons, and maintain class writing records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese language arts teachers use this skill to design authentic writing tasks, guide drafting and revision, apply rubric-based essay review, diagnose writing patterns, and plan class review lessons. It supports teacher decision-making rather than replacing teacher grading or student writing.

### Deployment Geography for Use:

China mainland by default; other regions require localized emergency contacts, curriculum alignment, and review of minor-data consent requirements.

## Known Risks and Mitigations:

Risk: Class writing records or writing-style profiles could be persisted or shared without the expected teacher confirmation and consent controls.

Mitigation: Install only where teachers are expected to manage class writing records and confirm the platform enforces consent checks, sharing controls, and teacher confirmation before persistent writes.

Risk: Student writing may disclose self-harm, bullying, serious despair, family safety issues, or other crisis signals.

Mitigation: Pause the writing-teaching workflow, follow the crisis referral protocol with localized emergency resources, and retain only the referral fact in long-term records.

Risk: Writing prompts or source material could reproduce copyrighted exam-prep, textbook, or past-paper content without authorization.

Mitigation: Require each prompt to carry a copyrightStatus value and keep restricted sources as index-only references unless reuse is authorized.

Risk: Generated feedback could be mistaken for final grading or could drift into writing essays for students.

Mitigation: Use the skill for standards, diagnostics, and review-lesson design; final grading remains with the teacher and original drafting remains with the student.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-writing-guide)
- [作文批改标准：等级描述式（一至四类文）+ 三维观察 15 项](references/three-dim-rubric.md)
- [写作任务设计模板](references/writing-task-template.md)
- [真实情境写作任务设计样板卡](references/task-design-sample-card.md)
- [批改样板模板](references/correction-sample-template.md)
- [讲评话术库](references/review-lesson-scripts.md)
- [学员写作风格档案模板](references/style-dna-profile-template.md)
- [学员写作风格长期记录模板](references/style-dna-record.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外处置](shared/crisis-exception.md)
- [AI 生成题目自检](shared/ai-item-check.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or structured text with rubric guidance, lesson scripts, writing-task templates, and teacher-confirmed class-record fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable output; persistent class or student record updates should remain teacher-confirmed.]

## Skill Version(s):

2.1.12 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

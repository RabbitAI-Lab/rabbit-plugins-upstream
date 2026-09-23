## Description:

面向语文老师的作文教学与批改标准工具，支持写作任务设计、过程引导、等级批改、三维观察诊断、讲评设计和班级写作力记录，同时限制为教师提供标准与讲评设计，不代替教师逐篇精批或为学员代写作文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language K12 writing teachers use this skill to design writing assignments, guide drafting and revision, apply rubric-based assessment, diagnose class writing patterns, and prepare review lessons. It is intended for teacher-facing planning and feedback workflows, with final grading, student-facing use, and parent communication reviewed by the teacher.

### Deployment Geography for Use:

Global, with guidance to localize student-data rules and crisis/help resources for the deployment region.

## Known Risks and Mitigations:

Risk: The skill may involve student writing records or parent-sharing decisions in K12 contexts.

Mitigation: Confirm school student-data rules before long-term records, use aliases, obtain required consent for write-back or parent sharing, and honor the skill's view, correct, delete, pause, sharing-control, and export controls.

Risk: Crisis signals such as self-harm, bullying, severe despair, or family safety issues can appear in student writing.

Mitigation: Stop ordinary writing-feedback workflows, avoid storing sensitive details, and follow the crisis referral protocol with localized emergency and help resources.

Risk: AI-generated or copied writing prompts can create copyright or suitability issues.

Mitigation: Require copyrightStatus labeling, keep textbook and exam prompts as index-only references, and run the AI item self-check before assigning generated prompts.

Risk: Automated feedback may be mistaken for final grading or direct student instruction.

Mitigation: Use outputs as teacher-reviewed drafts and standards only; the teacher makes final grading, student-facing, and parent-facing decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-writing-guide)
- [作文批改标准：等级描述式（一至四类文）+ 三维观察 15 项](references/three-dim-rubric.md)
- [写作任务设计模板](references/writing-task-template.md)
- [真实情境写作任务设计样板卡](references/task-design-sample-card.md)
- [批改样板模板](references/correction-sample-template.md)
- [学员写作风格档案模板](references/style-dna-profile-template.md)
- [学员写作风格长期记录模板](references/style-dna-record.md)
- [讲评话术库](references/review-lesson-scripts.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机例外（共享片段）](shared/crisis-exception.md)
- [平台能力约定与降级路径（全库共享）](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text templates for teacher review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable payload; outputs are teacher-facing guidance, rubrics, lesson-review scripts, records, and policy-controlled templates.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

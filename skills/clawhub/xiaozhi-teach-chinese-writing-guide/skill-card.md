## Description:

面向语文老师的作文教学与批改标准工具。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Chinese-language teachers use this skill to design writing assignments, define grading rubrics, plan review lessons, and track pseudonymous class writing patterns for upper-primary and middle-school learners.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle pseudonymous student writing records and class-level observations.

Mitigation: Use the disclosed view, correct, delete, pause, sharing-control, and export controls; keep student identifiers pseudonymous and store only teacher-confirmed records.

Risk: Writing samples can reveal self-harm, abuse, bullying, severe despair, or other student safety concerns.

Mitigation: Follow the crisis exception workflow immediately and, outside mainland China, replace or supplement the listed crisis resources with local emergency and mental-health contacts.

Risk: Generated writing prompts or copied source prompts could introduce copyright or suitability problems.

Mitigation: Require copyrightStatus labels for prompts, keep third-party question-bank and exam prompts as indexes only, and run AI-generated prompts through the bundled item self-check before teacher approval.

Risk: AI-generated rubrics, grading bands, or comments could be mistaken for final assessment decisions.

Mitigation: Keep outputs as teacher-facing drafts; the skill explicitly leaves final grading, class use, and record persistence to teacher confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-writing-guide)
- [作文批改标准：等级描述式（一至四类文）+ 三维观察 15 项](references/three-dim-rubric.md)
- [写作任务设计模板](references/writing-task-template.md)
- [真实情境写作任务设计样板卡](references/task-design-sample-card.md)
- [批改样板模板](references/correction-sample-template.md)
- [讲评话术库](references/review-lesson-scripts.md)
- [学员写作风格档案模板](references/style-dna-profile-template.md)
- [学员写作风格长期记录模板](references/style-dna-record.md)
- [ClassTeachingWorkspace schema](shared/class-teaching-workspace.schema.json)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外处理协议](shared/crisis-exception.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are teacher-facing guidance and draft records that require teacher confirmation before classroom use or storage.]

## Skill Version(s):

2.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

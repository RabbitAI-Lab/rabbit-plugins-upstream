## Description:

A Chinese writing instruction skill for teachers that helps design writing tasks, guide drafting and revision, create grading rubrics, diagnose class writing patterns, plan review lessons, and maintain writing records without writing essays for students or replacing teacher judgment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to plan upper-primary and middle-school Chinese writing instruction, including prompt design, process guidance, rubric-based review, writing style observation, and class review lesson design. It outputs standards, templates, and teaching guidance while leaving final grading and student writing to the teacher and learner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authoritative security summary reports a permission-scope mismatch around reading class weakness records.

Mitigation: Align the schema and declared read paths before broad deployment, or install only where the host strictly enforces field-level permissions.

Risk: Class weakness and student tier data may be used when planning writing tasks and lessons.

Mitigation: Make this data use visible to teachers and keep generated workspace updates as teacher-confirmed proposals.

Risk: Student writing can contain sensitive personal or crisis signals.

Mitigation: Use aliases or numbered samples, avoid sharing full student essays, and follow the bundled crisis exception protocol when safety signals appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-writing-guide)
- [写作任务设计模板](references/writing-task-template.md)
- [作文批改标准：等级描述式（一至四类文）+ 三维观察 15 项](references/three-dim-rubric.md)
- [学员写作风格长期记录模板](references/style-dna-record.md)
- [真实情境写作任务设计样板卡](references/task-design-sample-card.md)
- [批改样板模板](references/correction-sample-template.md)
- [学员写作风格档案模板](references/style-dna-profile-template.md)
- [讲评话术库](references/review-lesson-scripts.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机例外（共享片段）](shared/crisis-exception.md)
- [平台能力约定与降级路径（全库共享）](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown and structured teaching templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include class workspace update proposals that require teacher confirmation before persistence.]

## Skill Version(s):

2.1.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

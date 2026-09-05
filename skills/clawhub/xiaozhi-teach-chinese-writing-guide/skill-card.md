## Description:

面向语文老师的作文教学与批改标准工具，帮助设计真实情境写作任务、制定批改与讲评标准、观察学员写作风格，并维护班级写作力记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese language teachers use this skill to plan writing assignments, guide drafting and revision, create rubric-based grading guidance, design review lessons, and track writing-style development for upper-primary and middle-school classes.

### Deployment Geography for Use:

China mainland by default; localize crisis resources and privacy/legal assumptions before use elsewhere.

## Known Risks and Mitigations:

Risk: Classroom-memory features can involve student writing profiles and learning records.

Mitigation: Use student aliases, confirm consent settings, and review privacy controls before profile writeback or any parent-visible sharing.

Risk: Crisis referral contacts and privacy assumptions are designed around a mainland China K12 setting.

Mitigation: Before use elsewhere, localize emergency resources, school support pathways, and privacy/legal assumptions.

Risk: AI-generated writing prompts may be unsuitable, unclear, or too close to restricted source material.

Mitigation: Run the included AI item self-check, mark AI-generated prompts, and require teacher review before classroom use or resource-bank storage.

Risk: The skill could be overused for ghostwriting or automated final grading.

Mitigation: Keep outputs to teaching guidance, rubrics, and review design; do not generate student essays, and leave final grading decisions to the teacher.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-writing-guide)
- [作文批改标准：等级描述式（一至四类文）+ 三维观察 15 项](artifact/references/three-dim-rubric.md)
- [写作任务设计模板](artifact/references/writing-task-template.md)
- [真实情境写作任务设计样板卡](artifact/references/task-design-sample-card.md)
- [批改样板模板](artifact/references/correction-sample-template.md)
- [讲评话术库](artifact/references/review-lesson-scripts.md)
- [学员写作风格长期记录模板](artifact/references/style-dna-record.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [危机例外](artifact/shared/crisis-exception.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese Markdown guidance, templates, rubrics, and structured classroom-record update guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing outputs; final grading, parent sharing, and resource-bank writes require teacher or consent checks described by the skill.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

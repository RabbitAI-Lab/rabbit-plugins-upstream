## Description:

Helps math teachers design math assessments with blueprints, two-way specification tables, item selection and copyright labels, item-level statistics, and teacher-confirmed writeback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Math teachers use this skill to plan diagnostic, formative, or summative math assessments, build two-way specification tables, select or draft candidate items with source and copyright status, and summarize item-level P/D, reliability, and knowledge-point scoring after teacher confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student assessment data may be handed to another skill without an explicit cross-skill sharing consent check.

Mitigation: Require confirmation of crossSkillSharing consent before any handoff, and transfer only the minimum fields needed for the receiving skill.

Risk: The shared schema may expose individual tier assignments or diagnostic weakness fields beyond the skill's stated need.

Mitigation: Narrow or enforce the accessible schema so the agent can use only the stated subfields for assessment design and item-level statistics.

Risk: AI-drafted candidate math items may contain errors or unsuitable wording if used directly.

Mitigation: Keep AI-generated items out of final exams until a teacher has verified the solution, uniqueness, conditions, numbers, and grade-level fit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [数学测评设计流程](references/exam-design-process.md)
- [双向细目表模板](references/blueprint-template.md)
- [双向细目表样板](references/blueprint-sample.md)
- [难度比例样板](references/difficulty-gradient-sample.md)
- [数学测评题目统计模板](references/result-analysis-rubric.md)
- [测评题目统计报告模板（班级）](references/class-report-sample.md)
- [测评统计卡模板（学员）](references/student-report-sample.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [ClassTeachingWorkspace schema](shared/class-teaching-workspace.schema.json)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance, tables, templates, and teacher-confirmed structured field updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce assessment blueprints, item selection notes, item-statistics summaries, handoff fields, and candidate item drafts that require teacher verification before use.]

## Skill Version(s):

2.1.6 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

教案设计器 helps Chinese-language teachers turn lesson-planning requests into UbD-based, observable lesson plans with assessment evidence, competency-aligned objectives, time matrices, question-chain drafts, and differentiated A/B/C outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and teachers use this skill to draft single-lesson or unit lesson plans from curriculum goals, class profile, and available learning-history summaries. It structures objectives, evidence, timing, classroom questions, differentiated tasks, and lesson-plan records for teacher review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lesson planning may use student tier or weakness data from classroom records.

Mitigation: Confirm the workspace uses aliases instead of real student names, review sharing settings, and keep lesson-plan summaries aggregated or pseudonymous.

Risk: AI-generated examples, variations, or classroom practice questions may be incorrect or unsuitable.

Mitigation: Run the bundled AI item self-check and have the teacher manually verify generated questions before using them in lessons, resource banks, or assessments.

Risk: The skill may produce differentiated tasks without enough student-tier evidence.

Mitigation: When studentTiers are unavailable, output a basic lesson plan marked as lacking learning-history context instead of inventing A/B/C groupings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-planner)
- [教案模板与示例](artifact/references/lesson-plan-template.md)
- [同一节课的三层教案示例](artifact/references/layered-lesson-example.md)
- [ClassTeachingWorkspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown lesson plans, question-chain drafts, task cards, and structured lesson-plan records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses classroom aliases or aggregated data when student context is present; AI-generated questions are flagged for teacher verification.]

## Skill Version(s):

2.1.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

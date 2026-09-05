## Description:

数学教师的备课工具：把一节数学课的概念建构路径、例题示范与变式训练排成可上的教案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Math teachers use this skill to plan Chinese middle-school math lessons, including concept construction, worked-example demonstration, variation practice, classroom summaries, and error-case records aligned to 2022 curriculum competency goals.

### Deployment Geography for Use:

China Mainland by default; localize curriculum alignment, crisis referrals, and minor-data requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: Generated math questions or variations may contain incorrect answers, impossible conditions, or unsuitable difficulty.

Mitigation: Require teacher review and the packaged AI item self-check before any generated question is stored, assigned, or reused.

Risk: Classroom planning data may include student-level information.

Mitigation: Use aliases, enforce the declared workspace paths, and require consent checks before student writeback or parent sharing.

Risk: The skill is scoped to math lesson planning and may be inappropriate for exam design, scoring workflows, non-math lesson plans, or unsupported regions.

Mitigation: Route out-of-scope tasks to the appropriate skill and localize curriculum, crisis referrals, and minor-data requirements before deployment outside China Mainland K12 settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-lesson-planner)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [数学概念建构四步模板](references/concept-build-template.md)
- [变式训练设计模板](references/variation-design.md)
- [数学错因分类表（教案层）](references/error-pattern-rubric.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [ClassTeachingWorkspace schema](shared/class-teaching-workspace.schema.json)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [markdown, configuration, guidance]

**Output Format:** [Markdown lesson-planning guidance and structured teaching-plan entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce draft lesson plans, concept-building paths, example demonstrations, variation exercises, classroom summaries, and error-case records for teacher review.]

## Skill Version(s):

2.1.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

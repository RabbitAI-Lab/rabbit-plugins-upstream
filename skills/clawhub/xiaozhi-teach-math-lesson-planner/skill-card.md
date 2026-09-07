## Description:

数学教师的备课工具：把一节数学课的概念建构路径、例题示范与变式训练排成可上的教案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese middle-school math teachers use this skill to plan math lessons around concept building, example demonstration, variation training, class summaries, and error records aligned to 2022 curriculum goals.

### Deployment Geography for Use:

Mainland China by default; use in other regions requires localized crisis contacts and minor-data consent rules.

## Known Risks and Mitigations:

Risk: Teacher-facing records may include student aliases, tier labels, weaknesses, and lesson interaction notes.

Mitigation: Confirm consent settings before student-profile writeback and keep unapproved notes in the class workspace only.

Risk: AI-generated math items may be incorrect or unsuitable for the grade level.

Mitigation: Run the included item self-check and require teacher verification before adding generated items to a resource library or test.

Risk: Crisis-support contact details and minor-data consent rules may not apply outside mainland China.

Mitigation: Localize emergency contacts and consent handling before deploying the skill in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-lesson-planner)
- [数学概念建构四步模板](references/concept-build-template.md)
- [变式训练设计模板](references/variation-design.md)
- [数学错因分类表](references/error-pattern-rubric.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [班级教学工作空间 Schema](shared/class-teaching-workspace.schema.json)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown lesson-plan guidance with structured class workspace entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include teacher-facing lesson frameworks, concept-building paths, example and variation designs, class-summary notes, and teacher-confirmed workspace writeback proposals.]

## Skill Version(s):

2.1.12 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

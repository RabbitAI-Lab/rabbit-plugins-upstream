## Description:

用 UbD 逆向设计把经验型备课转化为可观测的教学设计，生成预期结果、评估证据、核心素养目标、课堂时间矩阵、提问链草案和 A/B/C 分层教案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to draft Chinese K12 lesson plans from learning outcomes backward into assessments, classroom segments, question-chain drafts, and differentiated task cards. It is intended for teacher-facing lesson planning, not standalone student analytics, exam generation, or classroom facilitation.

### Deployment Geography for Use:

Global, with localization required outside Mainland China for curriculum alignment, minor-data requirements, and emergency-help references.

## Known Risks and Mitigations:

Risk: Lesson plans may draw on class workspace data, including student tiers and weakness summaries.

Mitigation: Confirm workspace permissions before use, avoid real student names, and use aliases, seat numbers, or aggregated class data in outputs.

Risk: Curriculum assumptions and emergency-help references are designed for Mainland China.

Mitigation: Localize curriculum standards, minor-data requirements, and emergency-help channels before deployment in other regions.

Risk: AI-generated examples, variants, or practice questions may contain errors.

Mitigation: Apply the bundled AI item check protocol and require teacher verification before adding generated items to a resource bank, worksheet, or exam.

Risk: The skill could be misapplied as a student analytics, exam-generation, or classroom-execution tool.

Mitigation: Use it for teacher-facing lesson planning and route analytics, exam generation, and classroom facilitation to the appropriate specialized skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-planner)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Lesson plan template](references/lesson-plan-template.md)
- [Layered lesson example](references/layered-lesson-example.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI item check protocol](shared/ai-item-check.md)
- [Platform conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown lesson plans, task cards, question-chain drafts, and structured workspace entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be teacher-reviewed, avoid real student names, and mark AI-generated questions for human verification before reuse.]

## Skill Version(s):

2.1.10 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

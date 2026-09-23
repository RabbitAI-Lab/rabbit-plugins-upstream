## Description:

This skill helps Chinese junior-high physics teachers draft lesson plans organized around concept building, physics-law instruction, model building, application practice, classroom summaries, differentiation, and question chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to draft Chinese junior-high physics lesson plans for a specific topic, including concept-building sequences, lesson timing, teacher prompts, differentiation, and experiment placeholders. It is not for standalone problem tutoring, exam design, or executable lab setup; outputs are teacher-reviewed drafts.

### Deployment Geography for Use:

Mainland China Chinese-language K12 contexts

## Known Risks and Mitigations:

Risk: Lesson-plan experiment placeholders could be mistaken for complete lab procedures.

Mitigation: Keep experiment content at the lesson-design level, include safetyLevel triage, and route equipment lists, operating steps, safety procedures, and emergency handling to the dedicated experiment-coach workflow and school lab rules.

Risk: Classroom profile data may include student-related learning information.

Mitigation: Use student aliases, confirm writeback before saving, respect view/correct/delete/pause/export controls, and review any lesson-plan writeback before it is stored.

Risk: Generated questions or materials may contain mistakes.

Mitigation: Label generated items as AI-generated and require teacher verification before classroom or repository use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-lesson-planner)
- [教案里的实验位模板](artifact/references/lab-design-template.md)
- [物理概念图谱](artifact/references/physics-concepts-map.md)
- [模型建构示例](artifact/references/model-examples.md)
- [班级物理档案模板](artifact/references/student-physics-profile-template.md)
- [实验安全约定](artifact/shared/lab-safety.md)
- [班级教学工作区数据契约](artifact/shared/class-teaching-workspace.schema.json)
- [平台约定](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown lesson-plan drafts and structured teaching notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts require teacher review, especially class-data writeback and experiment placeholders.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

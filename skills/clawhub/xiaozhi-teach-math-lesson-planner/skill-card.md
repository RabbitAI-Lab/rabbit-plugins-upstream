## Description:

数学教案设计 helps math teachers turn a math topic into a teachable lesson plan with concept building, example demonstration, variation practice, classroom summary, and error-record components aligned to 2022 curriculum goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External math teachers use this skill to draft classroom-ready lesson structures for middle-school math concepts, including objective wording, concept-construction flow, guided examples, differentiated variation practice, and follow-up error records. It is intended to support teacher preparation, not to replace teacher judgment or provide unreviewed standard answers.

### Deployment Geography for Use:

China Mainland by default; localize curriculum alignment, privacy requirements, and crisis-support channels before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can work with student aliases, class weak points, and teacher-confirmed records.

Mitigation: Keep consent controls enabled, use aliases rather than real names, and require teacher confirmation before writing lesson plans, interaction logs, or student writebacks.

Risk: Generated math questions, examples, or variations may be incorrect or unsuitable for the target grade.

Mitigation: Apply the bundled self-check protocol, label AI-generated teacher-side items for manual verification, and avoid adding generated items to resource libraries or exams before review.

Risk: The skill is designed around China Mainland Chinese K12 curriculum, privacy assumptions, and crisis-support routing.

Mitigation: Before deployment elsewhere, localize curriculum mappings, consent rules, and emergency or youth-support channels.

Risk: Broad teaching prompts may invoke this math lesson-planning skill when an exam, error-analysis, or non-math lesson skill is more appropriate.

Mitigation: Keep routing prompts narrow and hand off exam design, class error statistics, and non-math lesson planning to the specialized skills named in the artifact.

## Reference(s):

- [数学概念建构四步模板](references/concept-build-template.md)
- [变式训练设计模板](references/variation-design.md)
- [数学错因分类表](references/error-pattern-rubric.md)
- [概念建构样板](references/concept-build-sample.md)
- [例题示范样板](references/example-demo-sample.md)
- [变式训练样板](references/variation-training-sample.md)
- [错例档案样板](references/error-case-file-sample.md)
- [班级教学工作空间 Schema](shared/class-teaching-workspace.schema.json)
- [AI 出题自检协议](shared/ai-item-check.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外](shared/crisis-exception.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown lesson-planning guidance with structured text blocks and JSON-schema-aligned field names when class workspace records are discussed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should mark AI-generated questions for teacher verification, use student aliases for records, and create teacher-confirmed draft entries before any writeback.]

## Skill Version(s):

2.1.10 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

数学教师的班级错因分析：把作业与试卷的错题变成"下节数学课讲什么"。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External math teachers use this skill to turn assignment or exam error data into class-level misconception analysis, knowledge-point heat maps, selected student error profiles, and teaching intervention suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reference may direct an out-of-scope update to a persistent student weakness counter.

Mitigation: Remove or override the stubbornCount instruction before publication and enforce the bundled workspace schema so undeclared fields are rejected at runtime.

Risk: Classroom error analysis can expose sensitive student learning records.

Mitigation: Keep aliases, consent checks, and parent-sharing controls enabled; do not publish real student names with wrong-answer details.

Risk: Generated practice items may be incorrect if reused without review.

Mitigation: Require teacher confirmation and manual calculation checks before generated exercises are entered into assignments, tests, or resource libraries.

Risk: Student safety signals can appear while discussing learning difficulty or frustration.

Mitigation: Use the crisis exception protocol: stop ordinary analysis, state AI boundaries, and route the student to trusted adults or local emergency resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [Class error report template](references/class-error-report-template.md)
- [Error classification rubric](references/error-classification-rubric.md)
- [Error knowledge link template](references/error-knowledge-link-template.md)
- [Intervention design template](references/intervention-design.md)
- [Intervention report template](references/intervention-report-template.md)
- [Knowledge map template](references/knowledge-map-template.md)
- [Student error profile template](references/student-error-profile-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [AI item check protocol](shared/ai-item-check.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports and structured text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses aliases for students, labels sampled versus full-class evidence, and requires teacher review before generated exercises are reused.]

## Skill Version(s):

2.1.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

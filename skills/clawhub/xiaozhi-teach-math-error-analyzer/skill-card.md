## Description:

Helps math teachers turn homework and test errors into class-level error analysis, knowledge-gap mapping, individual error profiles, and next-lesson intervention suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Teachers use this skill to analyze middle-school math errors from homework or assessment data, identify common causes and weak knowledge points, and plan targeted class or student interventions. It is intended to support teacher review and planning, not replace grading or final teaching decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A bundled reference may direct the agent to update a persistent student weakness counter outside the intended scope.

Mitigation: Deploy only with schema or field-level permissions that prevent this skill from updating stubbornCount.

Risk: Student error analysis can expose sensitive educational records or detailed diagnostic labels.

Mitigation: Use aliases, confirm teacher writebacks, avoid exporting detailed labels to student-facing systems, and verify consent before profile updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Class error report template](references/class-error-report-template.md)
- [Error classification rubric](references/error-classification-rubric.md)
- [Error-knowledge link template](references/error-knowledge-link-template.md)
- [Intervention design template](references/intervention-design.md)
- [Intervention report template](references/intervention-report-template.md)
- [Knowledge map template](references/knowledge-map-template.md)
- [Student error profile template](references/student-error-profile-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Shared vocabulary](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports, structured text templates, and JSON-compatible workspace field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses anonymized class and student identifiers; AI-generated practice items require teacher verification before reuse.]

## Skill Version(s):

2.1.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

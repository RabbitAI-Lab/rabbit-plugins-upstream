## Description:

Analyzes Chinese K–12 math classwork and exam errors to identify shared misconceptions, map weak knowledge areas, and suggest teacher-reviewed instructional interventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Math teachers use students' de-identified item-level responses to identify recurring error patterns, prepare class and individual learning summaries, and plan the next lesson. The skill provides draft analysis and suggestions, not grading or autonomous teaching decisions.

### Deployment Geography for Use:

Chinese mainland; use elsewhere requires localization of curriculum, language, emergency contacts, and consent practices.

## Known Risks and Mitigations:

Risk: Student work and individual error profiles can expose minors' personal information.

Mitigation: Provide de-identified classwork, respect consent and sharing controls, and have teachers confirm any record updates.

Risk: Small samples or AI-generated exercises may lead to misleading teaching decisions.

Mitigation: Label sampled findings with sample size, avoid percentages for very small samples, and have teachers check analyses and exercises before use.

Risk: Curriculum, emergency contacts, and consent defaults may be unsuitable outside Chinese mainland schools.

Mitigation: Localize curriculum, language, crisis resources, and consent rules before use in another region.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [Error classification rubric](artifact/references/error-classification-rubric.md)
- [Class error report template](artifact/references/class-error-report-template.md)
- [Intervention design guidance](artifact/references/intervention-design.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Teaching guidance]

**Output Format:** [Markdown reports, student error profiles, knowledge-area summaries, and suggested teaching interventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes sampled findings from whole-class counts; teacher review is required before using generated exercises or recording changes.]

## Skill Version(s):

2.6.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

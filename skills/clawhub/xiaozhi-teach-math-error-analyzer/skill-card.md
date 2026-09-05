## Description:

Helps junior-middle-school math teachers turn homework and test errors into class-level error analysis, knowledge-point heat maps, student profiles, and teaching intervention suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External math teachers use this skill to analyze specific homework or test errors, identify common class-level causes, map weak knowledge points, and prepare next-lesson interventions. It is designed for teacher review and does not replace grading, ranking, or instructional decisions.

### Deployment Geography for Use:

Mainland China by default; use in other regions requires localization of curriculum assumptions, emergency support channels, and minor-data consent rules.

## Known Risks and Mitigations:

Risk: Classroom error analysis may expose student learning records or identifiable student-error details.

Mitigation: Use pseudonymized classroom data, enforce consent controls, and avoid publishing real student names with specific wrong answers.

Risk: Invalid item-score data can distort error rates, p-values, and downstream teaching recommendations.

Mitigation: Validate imported scores before analysis, including maxScore > 0 and score <= maxScore.

Risk: Generated writebacks or practice items may be inaccurate or unsuitable for classroom use.

Mitigation: Require teacher review before confirming writebacks, and manually verify AI-generated practice items before adding them to assignments or tests.

Risk: The skill includes Mainland China curriculum, safety-channel, and minor-consent assumptions.

Mitigation: Localize curriculum alignment, emergency contacts, and consent requirements before use in other regions.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Class error report template](references/class-error-report-template.md)
- [Error classification rubric](references/error-classification-rubric.md)
- [Intervention design](references/intervention-design.md)
- [Knowledge map template](references/knowledge-map-template.md)
- [Student error profile template](references/student-error-profile-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown reports, structured tables, and JSON-compatible workspace updates for teacher review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses pseudonymized classroom data and teacher-confirmed writebacks; generated practice items require human verification.]

## Skill Version(s):

2.1.6 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Guides Chinese secondary-school students through biology charts, diagrams, pedigrees, tables, and source-based questions by identifying visual evidence before applying textbook concepts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese mainland middle- and high-school biology students use this tutor to interpret a specific chart or source-based question and support their answers with evidence. It adapts the depth of high-school examples to whether a student studies biology for the elective examination.

### Deployment Geography for Use:

China (mainland); localize curriculum, emergency contacts, and minor-consent requirements before use elsewhere

## Known Risks and Mitigations:

Risk: Curriculum assumptions, emergency contacts, and minor-consent rules may be unsuitable outside mainland China.

Mitigation: Localize these elements for the student's school system and location before deployment; confirm location before giving crisis contacts.

Risk: Student profile sharing or reminders without intentional consent could expose or retain student information.

Mitigation: Keep the default interaction limited to the current question; enable memory, cross-skill sharing, and reminders only after the relevant student or guardian opt-in.

Risk: Educational discussion of physiology charts could be mistaken for interpretation of a student's medical results.

Mitigation: Do not interpret personal test results or diagnose; direct the student to a parent or guardian and a clinician.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-chart-reader)
- [Biology chart-reading guide](references/biology-chart-guide.md)
- [Required high-school biology charts](references/biology-hs-charts-required.md)
- [Elective high-school biology charts](references/biology-hs-charts-elective.md)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Chinese-language Markdown with stepwise questions and explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional error-log and review-reminder handoffs require separate student consent.]

## Skill Version(s):

2.10.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

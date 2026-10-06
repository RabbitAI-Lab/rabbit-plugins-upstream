## Description:

Turns classroom assessment results into knowledge-gap analysis and actionable teaching adjustments for teachers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 teachers use student-level item scores to identify classwide knowledge gaps, draft individual diagnosis cards and class reports, and plan differentiated teaching. Teachers review any student- or parent-facing material before use.

### Deployment Geography for Use:

Mainland China; localize curriculum, consent requirements, and crisis-support guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Student assessment records could expose identifiable or sensitive information if retained or shared inappropriately.

Mitigation: Configure platform persistence and sharing controls before use, use student aliases, check consent before parent-facing output or student-record writeback, and let teachers control deletion and sharing.

Risk: Incomplete item scores or small samples could produce misleading knowledge-gap and student-level conclusions.

Mitigation: Limit total-score-only inputs to score distributions, flag insufficient evidence, avoid trend claims without repeated assessments, and have teachers review recommendations.

Risk: Mainland China curriculum, consent practices, and crisis-support guidance may not fit other regions.

Mitigation: Localize these settings before deployment outside mainland China and confirm the learner's location before giving emergency contacts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis framework](artifact/references/analysis-framework.md)
- [Class report template](artifact/references/class-report-template.md)
- [Student diagnosis card template](artifact/references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown reports, knowledge-point tables, and student diagnosis cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses aliases for students; reports data gaps and uncertainty; teacher review required before sharing.]

## Skill Version(s):

2.10.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

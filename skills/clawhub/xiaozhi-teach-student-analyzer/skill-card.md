## Description:

Helps teachers turn class assessment results into knowledge-gap analysis, student diagnostics, and actionable teaching adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

K–12 teachers use this skill to analyze class and question-level scores, identify shared learning gaps, prepare individual and class reports, and choose differentiated teaching adjustments. It does not create exams, lesson plans, or revision schedules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student scores and identifiers may be retained or shared beyond the intended audience.

Mitigation: Use student aliases where possible, confirm sharing consent, and use pause or delete controls when records should not persist.

Risk: Stored class data may be changed outside the skill's permitted scope.

Mitigation: Enforce the skill's field-level access permissions before allowing record updates.

Risk: School, privacy, and emergency guidance may not match the deployment locale.

Mitigation: Confirm the locale and adapt local requirements and referral information before use.

## Reference(s):

- [ClawHub release listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis framework](references/analysis-framework.md)
- [Class report template](references/class-report-template.md)
- [Student diagnosis card template](references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown reports, diagnosis cards, and teaching recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include knowledge-point summaries, de-identified student analyses, and consent-gated class records.]

## Skill Version(s):

2.11.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

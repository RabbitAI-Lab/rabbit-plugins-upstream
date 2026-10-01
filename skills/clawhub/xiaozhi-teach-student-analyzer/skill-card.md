## Description:

Turns class assessment results into knowledge-gap analysis, student support summaries, and actionable teaching adjustments for teachers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers analyze item-level class assessment data to identify shared knowledge gaps, prepare de-identified student diagnosis cards and class reports, and plan differentiated instruction. Student- or parent-facing material requires teacher review and applicable consent.

### Deployment Geography for Use:

Mainland China by default; localize crisis referral information before use elsewhere.

## Known Risks and Mitigations:

Risk: Student assessment data and parent-facing summaries can expose sensitive student information.

Mitigation: Use seat numbers or aliases, avoid names in shared reports, confirm before saving records, and check parent/student consent before parent-facing output.

Risk: Sparse assessments or flawed questions can lead to misleading ability labels or teaching decisions.

Mitigation: Mark insufficient evidence, avoid trend or tier conclusions from fewer than three assessments, and review suspect items before treating them as knowledge gaps.

Risk: Crisis referral details may be inappropriate outside the default region.

Mitigation: Confirm the user's region and use local emergency and youth-support channels rather than reusing mainland China contact numbers.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis framework](references/analysis-framework.md)
- [Class report template](references/class-report-template.md)
- [Student diagnosis card template](references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown reports, knowledge-point heatmaps, student diagnosis cards, and teaching recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Classroom records are proposed for teacher confirmation before saving; reports avoid real student names.]

## Skill Version(s):

2.9.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

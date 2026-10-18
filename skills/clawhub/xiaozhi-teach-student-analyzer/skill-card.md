## Description:

Analyzes classroom assessment results to identify knowledge gaps and draft actionable teaching adjustments for teachers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to analyze class and individual assessment data, spot knowledge gaps, and draft class reports, student diagnosis cards, and differentiated teaching suggestions for teacher review.

### Deployment Geography for Use:

Global (defaults to mainland China; localize crisis referrals elsewhere)

## Known Risks and Mitigations:

Risk: Student performance data or persistent class records may expose sensitive information.

Mitigation: Use only with authorized class data, use aliases or seat numbers, and review records before saving.

Risk: Parent-facing output or student-profile writeback may disclose information without consent.

Mitigation: Verify the relevant sharing or writeback consent and have a teacher review material before release.

Risk: Uploading live confidential exam materials could compromise exam security.

Mitigation: Do not upload unreleased exam materials; analyze post-exam scores and question-to-topic mappings instead.

Risk: Thin assessment history may produce misleading trend or student-level conclusions.

Mitigation: Flag insufficient evidence and avoid stable trend claims or lasting labels from fewer than three assessments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis framework](artifact/references/analysis-framework.md)
- [Class report template](artifact/references/class-report-template.md)
- [Student diagnosis card template](artifact/references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Reports, Guidance]

**Output Format:** [Markdown and text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed reports; optional class-record updates where authorized.]

## Skill Version(s):

2.11.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

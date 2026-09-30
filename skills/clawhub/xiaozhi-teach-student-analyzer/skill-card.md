## Description:

Helps teachers turn Chinese K–12 assessment results into class and student diagnoses, knowledge-gap summaries, and actionable teaching adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers analyze class assessment data to identify shared knowledge gaps, review individual progress, and plan differentiated instruction. Reports and any parent-facing material require teacher review.

### Deployment Geography for Use:

Mainland China by default; deployments elsewhere require localized crisis referral information.

## Known Risks and Mitigations:

Risk: Sensitive student performance records could identify children or reach unintended recipients.

Mitigation: Use aliases or seat numbers, keep public reports aggregated, and check consent before parent-facing output or student-record writeback.

Risk: Assessment summaries or student groupings may be misleading when evidence is incomplete or a test is flawed.

Mitigation: Have teachers review conclusions, flag insufficient samples, and avoid knowledge-point or trend claims without the required item-level or historical data.

Risk: Shared teaching records can expose assessment data to other installed skills.

Mitigation: Review cross-skill workspace access, honor sharing controls, and confirm proposed writes before saving.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis framework](references/analysis-framework.md)
- [Class report template](references/class-report-template.md)
- [Student diagnosis card template](references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown class reports, student diagnosis cards, and teaching recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Knowledge-point heatmaps and item statistics require per-question scores; limited data must be labeled accordingly.]

## Skill Version(s):

2.8.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

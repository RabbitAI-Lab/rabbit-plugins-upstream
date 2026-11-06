## Description:

把班级成绩表变成可执行的教学调整。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to analyze class and item-level assessment scores, identify topic-level learning needs, and plan differentiated teaching adjustments. It can prepare student- or parent-facing drafts for teacher review.

### Deployment Geography for Use:

China (mainland; K–12 teaching context)

## Known Risks and Mitigations:

Risk: Student score data could be exposed or shared without the required permissions if the host platform does not enforce consent, sharing, and deletion controls.

Mitigation: Use only student data approved for the platform, prefer aliases, verify that the platform enforces those controls, and review proposed record changes and parent-facing drafts.

Risk: Confidential or unreleased exam materials could be disclosed through analysis inputs.

Mitigation: Keep confidential exam materials out; for post-exam analysis, use item scores and question-to-topic mappings.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis framework](artifact/references/analysis-framework.md)
- [Class report template](artifact/references/class-report-template.md)
- [Student diagnosis card template](artifact/references/student-diagnosis-card-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Structured text and Markdown reports with tables and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Class-level and per-item score summaries, topic heatmaps, student diagnoses, and differentiated teaching suggestions; parent-facing drafts require teacher review.]

## Skill Version(s):

2.12.6 (source: SKILL.md frontmatter; server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

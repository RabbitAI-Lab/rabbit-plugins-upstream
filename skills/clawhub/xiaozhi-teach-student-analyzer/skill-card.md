## Description:

Turns class assessment score tables into actionable teaching adjustments, including class profiles, knowledge-point heatmaps, student tiers, and teacher-facing recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to analyze class assessment data, identify common knowledge-point weaknesses, prepare individual diagnosis cards, and turn evidence into differentiated teaching adjustments. It is intended for upper-primary and middle-school contexts, with privacy controls for student records and parent-facing summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student assessment records may be stored or shared across a class-teaching workspace.

Mitigation: Use student aliases where possible, confirm writes before saving, and review sharing plus parent-consent settings before generating parent-facing material.

Risk: Crisis referral guidance may not match every user's country or region.

Mitigation: Adapt emergency and crisis-resource guidance to the user's actual location before deployment.

Risk: Small samples, total-score-only data, or missing item-to-knowledge mappings can make detailed trends and heatmaps unreliable.

Mitigation: Limit output to supported analyses, mark insufficient evidence clearly, and avoid stable trend or knowledge-point conclusions when required data is missing.

Risk: Generated example or practice items may contain errors if reused without review.

Mitigation: Run the included AI item self-check and require teacher verification before adding generated items to a resource bank or assessment.

## Reference(s):

- [analysis-framework.md](artifact/references/analysis-framework.md)
- [class-report-template.md](artifact/references/class-report-template.md)
- [student-diagnosis-card-template.md](artifact/references/student-diagnosis-card-template.md)
- [class-teaching-workspace.schema.json](artifact/shared/class-teaching-workspace.schema.json)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports and structured classWorkspace entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses student aliases where possible and generates teacher-confirmed record updates.]

## Skill Version(s):

2.1.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

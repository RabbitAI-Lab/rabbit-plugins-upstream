## Description:

学情分析师把班级逐题成绩表转化为班级画像、知识点热力图、分层诊断和教学调整建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to analyze Chinese K-12 class assessment data, locate weak knowledge points, identify class tiers, and draft evidence-based teaching adjustments or parent-facing summaries for teacher review.

### Deployment Geography for Use:

Mainland China Chinese K-12 contexts; localize curriculum assumptions, consent rules, language, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill processes class assessment data and may include student-level learning records.

Mitigation: Install it only where teachers are allowed to process this data, use student aliases where possible, and review pending writebacks before saving.

Risk: Parent-facing summaries or student diagnostics could disclose sensitive academic or emotional information.

Mitigation: Check the skill's consent controls before parent sharing, keep teacher review in the loop, and avoid sharing records with other skills when the teacher opts out.

Risk: The artifact is designed for Mainland China Chinese K-12 assumptions.

Mitigation: Localize language, curriculum assumptions, consent rules, and crisis contacts before using it in other regions or school systems.

Risk: Assessment conclusions can become misleading when data is incomplete or sample sizes are too small.

Mitigation: Use the skill's documented data-completeness checks, avoid knowledge-point heatmaps without item-level scores and blueprint mapping, and label insufficient evidence conservatively.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis Framework](artifact/references/analysis-framework.md)
- [Class Report Template](artifact/references/class-report-template.md)
- [Student Diagnosis Card Template](artifact/references/student-diagnosis-card-template.md)
- [Platform Conventions](artifact/shared/platform-conventions.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, configuration, guidance]

**Output Format:** [Markdown reports and structured class-workspace update guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include class summaries, item statistics, weakness rankings, student tiers, parent communication drafts, and pending teacher-confirmed writebacks.]

## Skill Version(s):

2.3.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

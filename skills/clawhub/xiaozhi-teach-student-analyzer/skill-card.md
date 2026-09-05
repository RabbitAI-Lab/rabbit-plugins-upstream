## Description:

Turns class assessment data into actionable teaching adjustments through item-level score intake, class profiles, knowledge-point heatmaps, student tiers, and targeted recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to analyze class assessment data, locate shared knowledge-point weaknesses, generate class and individual diagnosis reports, and turn the results into differentiated teaching adjustments. It is designed for Chinese K12 classroom assessment workflows using anonymized student aliases or seat numbers.

### Deployment Geography for Use:

China mainland by default; other regions require localization of crisis resources, curriculum alignment, and minor-data consent rules before deployment.

## Known Risks and Mitigations:

Risk: The skill handles sensitive classroom assessment records, aliases, tiers, weakness rankings, and adjacent teaching context.

Mitigation: Install it only where teachers understand the data use and the platform enforces read/write permissions plus delete and export controls.

Risk: Parent-facing material or student-profile writeback could expose sensitive performance or emotional context without the right consent.

Mitigation: Check parentSharingConsent, emotionSharingWithParent, and teacherWritebackConsent before parent-facing output or writeback.

Risk: Statistical conclusions can be misleading when only total scores, missing knowledge-point mappings, or small samples are available.

Mitigation: Limit output to total-score analysis when inputs are incomplete, label sample limitations, and avoid stable trend conclusions when data is insufficient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Analysis framework and templates](references/analysis-framework.md)
- [Class report template](references/class-report-template.md)
- [Student diagnosis card template](references/student-diagnosis-card-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Platform conventions](shared/platform-conventions.md)
- [Shared vocabulary](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports and structured classroom workspace updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate class profiles, item statistics, weakness rankings, student tiers, parent-facing summaries, and teacher-confirmed writeback entries when required data and consent are present.]

## Skill Version(s):

2.1.6 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

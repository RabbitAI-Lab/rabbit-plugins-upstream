## Description:

This skill helps teachers turn class assessment tables into actionable learning analysis, including class profiles, knowledge-point heat maps, student tiers, and teaching adjustment suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Teachers use this skill to analyze class assessment results, locate common weak knowledge points, produce individual diagnosis cards, and generate practical next-step teaching recommendations. It is intended for Chinese K12 classroom analysis workflows that use anonymized student identifiers and teacher-confirmed data.

### Deployment Geography for Use:

China mainland by default; other regions require localized curriculum, privacy/legal, and crisis-referral settings before student-facing use.

## Known Risks and Mitigations:

Risk: Student assessment data may include identifiable or sensitive information.

Mitigation: Use student aliases or seat numbers, avoid unnecessary real names, and confirm consent controls before parent-facing summaries or cross-skill sharing.

Risk: Analysis can be misleading when only total scores are available, item-to-knowledge mappings are missing, samples are small, or a test item may be flawed.

Mitigation: Limit conclusions to the available evidence, label sample limitations, skip unsupported heat maps or reliability statistics, and require teacher review of suspected item issues.

Risk: Student safety or crisis signals could be hidden if they are converted into routine learning summaries.

Mitigation: Stop the normal analysis workflow when crisis signals appear and follow the bundled crisis referral protocol with localized emergency guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-analyzer)
- [Analysis framework](references/analysis-framework.md)
- [Class report template](references/class-report-template.md)
- [Student diagnosis card template](references/student-diagnosis-card-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured data, Guidance]

**Output Format:** [Markdown and text reports with structured class-workspace entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses teacher-provided assessment data and should avoid real student names in outputs.]

## Skill Version(s):

2.1.12 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

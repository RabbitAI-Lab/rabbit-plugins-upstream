## Description:

智能错题本 helps Simplified Chinese K12 tutoring agents archive concrete wrong-answer cases, classify root causes across four dimensions, count repeated weak points, and coordinate authorized handoffs to subject-specific learning skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External tutoring agents, students, guardians, and education operators use this skill to capture specific wrong-answer events, guide analysis without prematurely giving answers, generate review sets or term reports, and update weak-point records with consent-aware cross-skill sharing.

### Deployment Geography for Use:

Mainland China for the default Simplified Chinese K12 tutoring release; localize curriculum assumptions, consent rules, and crisis support resources before use elsewhere.

## Known Risks and Mitigations:

Risk: Use outside the intended Simplified Chinese, Mainland China K12 tutoring context could provide unsuitable curriculum, consent, or crisis-support guidance.

Mitigation: Localize curriculum assumptions, consent rules, and crisis resources before deployment outside the default setting.

Risk: The skill handles longitudinal student learning records and can coordinate cross-skill sharing, reminders, and parent-visible summaries.

Mitigation: Review and configure profile memory, cross-skill sharing, parent visibility, reminder consent, and data control actions before enabling the workflow.

Risk: Students may ask for help during active exams or assessments.

Mitigation: Follow the artifact's exam boundary: do not explain, hint, record, or notify parents during an active exam; resume only after the student says the exam is over.

Risk: Student messages may include crisis signals beyond academic tutoring.

Mitigation: Stop the wrong-answer workflow, avoid diagnostic labels, prompt contact with a trusted adult, and use localized emergency or support channels according to the crisis exception protocol.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error analysis framework](references/error-analysis-framework.md)
- [Unified vocabulary and consent controls](shared/vocab.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Platform conventions and localization guidance](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration]

**Output Format:** [Conversational guidance, Markdown-style wrong-answer reports, and structured JSON handover/profile/reminder records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a concrete wrong-answer input; image capture degrades to text entry, and memory, reminder, parent visibility, and cross-skill sharing depend on configured consent.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

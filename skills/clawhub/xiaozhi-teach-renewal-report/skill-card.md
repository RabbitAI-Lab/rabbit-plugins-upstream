## Description:

阶段报告与续课助手 helps independent teachers turn one named student's real lesson records, homework follow-ups, progress evidence, course-package status, and consent fields into evidence-based progress reports, renewal suggestions, and parent communication drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent K12 teachers use this skill to prepare Chinese-language stage reports and renewal conversations from a single student's recorded learning history. The skill keeps the teacher in control of review, consent checks, and any parent-facing message sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads sensitive longitudinal learning records for minors.

Mitigation: Use it only where the teacher is allowed to access the relevant student records; confirm the named student before reading data and limit reading to records needed for the requested report.

Risk: Parent-facing reports or renewal scripts could disclose information without the right consent.

Mitigation: Check parentCommunicationAllowed before generating parent-facing content, check emotionSharingWithParent when classroom state is included, and keep all sending under teacher control.

Risk: Progress claims or renewal recommendations could mislead families if they are not grounded in records.

Mitigation: Require each number and claim to trace back to workspace records, avoid unsupported estimates or score promises, and have the teacher review the draft before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Stage report templates](references/stage-report-templates.md)
- [Renewal communication scripts](references/renewal-communication-scripts.md)
- [Shared vocabulary](shared/vocab.md)
- [Platform conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown report drafts, renewal recommendations, and parent communication script drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed output; parent-facing content is consent-gated and manually sent by the teacher.]

## Skill Version(s):

2.3.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

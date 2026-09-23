## Description:

This skill turns a student's weekly learning activity into an evidence-based weekly review with self-reflection, a focused next step, consent-controlled family sharing, and optional reminder or profile handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 learners use this skill to summarize a week of study into a student-facing review, identify the highest-priority next action, and optionally prepare a family-visible summary when consent allows. It is intended for weekly learning reflection rather than monthly reporting or single-question error analysis.

### Deployment Geography for Use:

China Mainland Chinese K12 deployments by default; other regions require localization of safety referral channels, consent language, and family-sharing expectations.

## Known Risks and Mitigations:

Risk: Weekly reviews can expose student learning history or prepare family-visible summaries.

Mitigation: Review profile, cross-skill sharing, parent sharing, emotion sharing, and reminder consent before generating summaries or handoffs.

Risk: Safety referral content is written for the Chinese K12 context and includes China Mainland emergency resources.

Mitigation: Localize crisis and referral channels before deployment outside China Mainland, and ask for the user's region before giving phone numbers when location is uncertain.

Risk: Sparse or unavailable memory/statistics can make trend claims unreliable.

Mitigation: Mark low-data conclusions as provisional and avoid historical counts or completion-rate claims when the required platform capability is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Weekly review report template](references/review-report-template.md)
- [Grade-band parameters](shared/grade-bands.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese Markdown/text weekly review, optional family summary, and structured handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires current-week learning evidence; profile writeback, reminders, cross-skill sharing, and family sharing require the relevant student consent settings.]

## Skill Version(s):

2.2.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

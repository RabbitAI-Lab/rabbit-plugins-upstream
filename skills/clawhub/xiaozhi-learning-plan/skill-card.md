## Description:

Generates Chinese-language weekly or 30-day study plans from a learner's goals, grade band, available time, and authorized learning profile data, with consent-gated follow-up and parent dashboard outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language students, parents or guardians, and learning-assistant deployments use this skill to turn study goals, exams, weak areas, and available time into actionable plans. It is intended for upper primary, middle-school, and high-school planning workflows, with parent-facing views only after the required consent checks.

### Deployment Geography for Use:

Mainland China by default; deployments elsewhere should replace or gate the crisis referral instructions with region-appropriate emergency guidance before use with minors.

## Known Risks and Mitigations:

Risk: Crisis referral instructions are localized for Mainland China and may be inappropriate for minors in other regions.

Mitigation: Use the skill only in appropriately localized Chinese-language deployments, or replace and gate crisis referral instructions with region-specific emergency guidance before use.

Risk: Parent dashboards and reminder queues may expose student profile, progress, or emotion-related information without sufficient consent.

Mitigation: Require explicit consent for parent sharing, emotion sharing, and reminder enqueueing; when consent is absent, provide the content to the student only.

Risk: Study plans can become misleading if historical memory, date awareness, or cross-session statistics are unavailable.

Mitigation: Fall back to current-session information, ask the learner for missing dates or approximate history, and avoid fabricating historical completion statistics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Plan templates](references/plan-templates.md)
- [Grade-band parameters](shared/grade-bands.md)
- [Shared vocabulary](shared/vocab.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [AI item self-check protocol](shared/ai-item-check.md)
- [Platform conventions](shared/platform-conventions.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [JSON Schema draft 2020-12](https://json-schema.org/draft/2020-12/schema)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text study plans, review summaries, parent dashboard text, and structured handover guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include consent-gated parent-facing summaries and localized crisis referral language; reminder content is prepared for a separate reminder workflow rather than sent directly.]

## Skill Version(s):

2.1.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

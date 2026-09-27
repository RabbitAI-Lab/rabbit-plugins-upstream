## Description:

Helps Chinese K–12 students record wrong answers across subjects, identify likely causes, track recurring weaknesses, and prepare targeted review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their educators use the skill to review specific missed questions, classify errors, track recurring weak points, and generate practice sets or term reports. With consent, it coordinates subject-specific follow-up and study reminders.

### Deployment Geography for Use:

Mainland China by default; other regions require localized language, curriculum, minor-consent rules, and crisis resources.

## Known Risks and Mitigations:

Risk: Persistent wrong-answer profiles and cross-skill or parent sharing can expose a minor's study history.

Mitigation: Confirm profile, sharing, parent-view, and reminder consent settings before use; honor review, correction, deletion, and no-memory controls.

Risk: Chinese-language curriculum and mainland China crisis contacts may be unsuitable elsewhere.

Mitigation: Localize curriculum, language, consent rules, and crisis resources before deployment outside the intended Chinese K–12 setting.

Risk: An incomplete question or missing student reasoning can lead to an unreliable diagnosis of the error.

Mitigation: Ask for the student's process, label insufficient evidence, and avoid saving unverified conclusions to the long-term profile.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error analysis framework](artifact/references/error-analysis-framework.md)
- [Shared error and weakness definitions](artifact/shared/vocab.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Cross-skill handover schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational feedback, study reports and practice questions in text or Markdown; structured study records and handoffs in JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tracks errors over a rolling 28-day window; record updates, sharing, and reminders are subject to user controls.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

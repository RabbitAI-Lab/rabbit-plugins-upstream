## Description:

Guides Chinese K–12 students to explain a concept in their own words, test their understanding, and identify where they get stuck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese K–12 students use guided explanation, examples, and follow-up questions to check whether they understand a concept. Teachers or guardians can support younger students and review the resulting assessment.

### Deployment Geography for Use:

Mainland China; localize curriculum, consent requirements, and emergency-help guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Learning records or retest reminders could be shared without the student's consent.

Mitigation: Keep assessments in the current session by default; require explicit consent and enabled sharing before saving, and a separate request and reminder consent before scheduling reminders.

Risk: Emergency advice and consent assumptions may not fit students outside mainland China.

Mitigation: Confirm location and localize emergency-help guidance, curriculum, and consent controls before deployment elsewhere.

Risk: Younger students may rely on an inaccurate mastery assessment or encounter distress during testing.

Mitigation: Require a teacher or guardian alongside primary-school users, adjust questions to the student's level, and stop tutoring to follow the crisis referral protocol when safety signals arise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-feynman-learning)
- [Five-step learning dialogue](references/feynman-5jump-statemachine.md)
- [Feynman dialogue patterns](references/feynman-dialogue-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Simplified Chinese dialogue and Markdown assessment summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports an A–D assessment, understanding level, sticking points, and suggested next step; session-only unless the student consents to sharing.]

## Skill Version(s):

2.11.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps Chinese K–12 students record incorrect answers, identify common error causes, track recurring weak points, and review their progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, with a parent or teacher present for elementary grades, use this skill to review specific wrong answers, classify likely causes, and monitor repeated difficulties across subjects. It can produce practice questions and study summaries after the student confirms the underlying record.

### Deployment Geography for Use:

Mainland China; deployment elsewhere requires localization of crisis contacts, curriculum, and minor-consent practices.

## Known Risks and Mitigations:

Risk: Wrong-answer records and weak-point profiles may contain sensitive information about minors' learning.

Mitigation: Obtain confirmation before saving records; offer viewing, correction, export, deletion, and pause-memory controls.

Risk: Reminders and parent or cross-skill sharing can expose study history beyond the immediate session.

Mitigation: Respect sharing consent and the controls for disabling parent or cross-skill sharing and pausing reminders.

Risk: Incomplete or unclear question details may produce an inaccurate error diagnosis.

Mitigation: Ask the student to confirm unclear text and reasoning; mark insufficient evidence rather than saving an unverified diagnosis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error analysis framework](references/error-analysis-framework.md)
- [Shared error categories and counting rules](shared/vocab.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational text, Markdown study reports, and structured handoff records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include error classifications, practice questions, weak-point summaries, and consent-dependent study records.]

## Skill Version(s):

2.4.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

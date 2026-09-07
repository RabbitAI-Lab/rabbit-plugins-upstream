## Description:

跨时空古文对话 is a Chinese classical literature tutoring agent that helps middle-school students understand classical Chinese and poetry through historically grounded author role-play, memorization drills, quotation practice, and exam-answer coaching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education-support agents use this skill for Chinese K12 classical Chinese and poetry study. It supports author-centered explanation, role-play, recitation practice, classical Chinese reading basics, poetry appreciation answers, and controlled learning-profile updates.

### Deployment Geography for Use:

China (Mainland) by default; localize curriculum assumptions, minor consent requirements, and crisis-support channels before use in other regions.

## Known Risks and Mitigations:

Risk: The skill can maintain a student learning profile for classical Chinese progress and error subtypes.

Mitigation: Use the documented controls for viewing, correcting, deleting, exporting, pausing memory, and disabling cross-skill or parent sharing.

Risk: The skill is designed for minors and includes crisis-support escalation with mainland China emergency references.

Mitigation: Confirm the learner's region before giving emergency numbers and replace crisis-support channels when deployed outside mainland China.

Risk: Historically grounded author role-play can become misleading if unsupported details are invented.

Mitigation: Use the bundled author profile reference and state uncertainty plainly when a historical detail is not supported.

Risk: Generated recitation drills or answer guidance may contain inaccurate source text or over-direct answers.

Mitigation: Apply the bundled item self-check, defer to the student's textbook when wording is uncertain, and use hint escalation before giving original-question answers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/chinese-classical-revival)
- [Classical author profiles](references/classical-author-profiles.md)
- [Chinese error dimension table](shared/chinese-error-dimension-table.md)
- [Platform conventions and localization notes](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown text with structured tutoring responses, practice items, and consent-scoped profile handover data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference consent-gated learning profile fields and reminder handoff payloads; no executable code is included in the artifact.]

## Skill Version(s):

1000000.12.0 (source: server release metadata; artifact frontmatter version 2.1.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

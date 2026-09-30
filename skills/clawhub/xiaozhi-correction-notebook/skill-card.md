## Description:

Helps Chinese K–12 students catalog missed questions, identify broad causes of errors, track recurring weak areas, and plan targeted review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese K–12 students use the skill to review specific wrong answers, spot repeated mistakes, and assemble practice sets and term summaries. Primary-school students use it with a parent or teacher present.

### Deployment Geography for Use:

Mainland China; localize curriculum, minor-data consent, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: Student study records may be retained or shared with other skills or parents without appropriate consent.

Mitigation: Confirm long-term profile, cross-skill sharing, parent-sharing, and reminder settings before enabling; honor the student's pause, correction, deletion, and sharing controls.

Risk: Incorrect error diagnoses or generated practice questions may mislead students.

Mitigation: Verify the original question and the student's reasoning, label insufficient evidence, and check generated questions before presenting them.

Risk: A student in crisis may receive ordinary study guidance or the wrong regional emergency contacts.

Mitigation: Stop the study workflow for crisis signals, direct the student to a trusted adult and local help, and localize contacts before deployment outside mainland China.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error analysis framework](references/error-analysis-framework.md)
- [Shared error and consent vocabulary](shared/vocab.md)
- [Generated-question quality checks](shared/ai-item-check.md)
- [Crisis referral and localization guidance](shared/crisis-exception.md)
- [Cross-skill handover schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language study guidance and Markdown reports; structured JSON handoffs when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term records, cross-skill sharing, and reminders depend on consent and platform capabilities.]

## Skill Version(s):

2.8.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

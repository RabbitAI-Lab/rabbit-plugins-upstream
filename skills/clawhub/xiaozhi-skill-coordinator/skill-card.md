## Description:

Routes Chinese K–12 learning requests to the appropriate skill, prevents duplicate handoffs, and assembles an on-request monthly learning overview from authorized summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians or teachers use this skill to coordinate learning tools, check how the learning system is working, and request a five-part monthly overview. Primary-school students require adult accompaniment.

### Deployment Geography for Use:

Chinese K–12 learning environments; crisis referrals must be localized outside Mainland China.

## Known Risks and Mitigations:

Risk: Student records or summaries could be shared with other skills, parents, or teachers without appropriate permission.

Mitigation: Confirm student or guardian consent for each sharing path and use only the minimum fields needed for the current request.

Risk: Reminder handoffs could expose learning details or produce unwanted notifications.

Mitigation: Queue reminders only when the corresponding reminder consent is enabled; honor requests to pause sharing or reminders.

Risk: Mainland China crisis contacts may not apply to students elsewhere.

Mitigation: Confirm location and provide locally appropriate emergency and crisis resources before use outside Mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week coordination example](artifact/references/one-week-linkage-record.md)
- [Handover protocol](artifact/schemas/handover-protocol.schema.json)
- [Consent and shared terminology](artifact/shared/vocab.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational text and structured monthly report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes and summarizes only the minimum consented information; does not teach, generate questions, or send reminders itself.]

## Skill Version(s):

2.6.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

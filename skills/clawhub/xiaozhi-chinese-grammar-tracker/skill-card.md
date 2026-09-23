## Description:

Chinese K-12 grammar coach that classifies six common sentence-error types, guides students through corrections, and, with consent, tracks recurring grammar-error patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, parents, and teachers use this skill for Chinese sentence-error practice, guided correction, and progress review for upper-primary and junior-secondary learners. Profile storage, parent sharing, cross-skill sharing, and reminders require explicit consent.

### Deployment Geography for Use:

Mainland China by default; other regions require localized crisis contacts, curriculum alignment, and minor-data consent review before student use.

## Known Risks and Mitigations:

Risk: The skill may store a student's recurring grammar-error profile.

Mitigation: Keep profile storage, cross-skill sharing, parent sharing, and reminders disabled unless the student or required guardian explicitly consents.

Risk: The bundled safety contacts and curriculum assumptions are designed for Mainland China.

Mitigation: Localize crisis-referral contacts, curriculum expectations, and minor-data consent rules before deploying outside Mainland China.

Risk: Students could ask for help during an active exam or restricted assessment.

Mitigation: Do not analyze the item or provide hints during an active exam; invite the student to return after the assessment for review.

Risk: Grammar-profile summaries could be shared beyond the student's intended audience.

Mitigation: Check consent before parent-visible output or cross-skill sharing, and share only the minimum grammar-profile fields needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Six-category grammar-error reference library](references/grammar-error-library.md)
- [Chinese error dimension table](shared/chinese-error-dimension-table.md)
- [Learning profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown guidance with optional JSON handoff snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversational coaching output; profile and handoff data are consent-gated; no executable code or shell commands are shipped.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

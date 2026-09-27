## Description:

在明确授权下管理学生的长期学习档案，支持查看、更正、导出和删除，并按独立同意管理情绪、兴趣及共享信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians use this skill to manage a consent-based learning profile for personalized tutoring and to review, correct, export or delete its records. Educators may contribute only when the relevant permissions are enabled.

### Deployment Geography for Use:

Mainland China; use elsewhere requires localized crisis contacts and consent rules.

## Known Risks and Mitigations:

Risk: A student's sensitive learning profile could be exposed or changed without proper authorization.

Mitigation: Use a platform that isolates student profiles, verifies identity, enforces consent fields and supports export and deletion.

Risk: Optional emotion records or profile sharing could reveal sensitive information about a minor.

Mitigation: Keep emotion tracking, teacher writeback, parent sharing, reminders and cross-skill sharing off unless the student or guardian clearly enables each feature.

Risk: Crisis referrals or consent handling may not fit users outside Mainland China.

Mitigation: Localize crisis contacts and legal consent rules before use in other regions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile template](artifact/references/dna-template.md)
- [Growth milestone criteria](artifact/references/growth-milestones.md)
- [Crisis referral protocol](artifact/references/crisis-referral-protocol.md)
- [Profile data schema](artifact/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Conversational text and structured learning-profile records; text export on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile access and updates require the appropriate identity checks and consent; optional sharing and emotion tracking are off by default.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

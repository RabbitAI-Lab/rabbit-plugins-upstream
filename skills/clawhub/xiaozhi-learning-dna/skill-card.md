## Description:

在明确授权下管理学生的长期学习档案，支持查看、更正、导出、删除和有限共享学习记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and authorized guardians use this skill to manage a consent-based learning profile for personalized tutoring, including progress, learning preferences, and optional sensitive observations.

### Deployment Geography for Use:

Mainland China (Chinese K–12); localize consent rules, curriculum, language, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: Student profiles contain sensitive minors' learning and optional emotional information.

Mitigation: Deploy only where student identity, guardian consent when required, field-level access, auditability, export, correction, deletion, and pause controls are enforced.

Risk: Parent, teacher, or other-skill access could disclose private student information.

Mitigation: Keep sharing permissions off by default and disclose only the minimum authorized fields after confirming the speaker's identity.

Risk: Crisis guidance and minor-consent assumptions may not fit other regions.

Mitigation: Localize crisis contacts, language, curriculum, and minor-consent rules before deployment outside mainland China.

## Reference(s):

- [ClawHub release: 学习DNA](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile template](artifact/references/dna-template.md)
- [Growth milestones](artifact/references/growth-milestones.md)
- [Crisis referral protocol](artifact/references/crisis-referral-protocol.md)
- [Profile schema and consent model](artifact/schemas/README.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Conversational text, text exports, and structured learning-profile records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sensitive fields and cross-skill sharing require separate consent; ordinary tutoring does not read the profile by default.]

## Skill Version(s):

2.4.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

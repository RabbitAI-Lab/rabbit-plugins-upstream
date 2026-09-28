## Description:

A Chinese-language learning-profile skill that helps K–12 students manage consent-based records of academic progress and personalized learning needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 students use this skill to create, inspect, correct, export, or delete their learning profiles with appropriate consent. Authorized guardians and educators can participate within the skill's separate sharing and writeback permissions.

### Deployment Geography for Use:

Mainland China; use elsewhere requires localization of curricula, minor-consent rules, and crisis contacts.

## Known Risks and Mitigations:

Risk: Sensitive student records or learning-emotion details could be exposed to another person or shared without permission.

Mitigation: Enable long-term profiles only where student identity, guardian consent when required, field-level access, and deletion/export controls can be enforced; require separate opt-ins for emotion tracking, parent sharing, teacher writeback, and cross-skill sharing.

Risk: Crisis referrals could offer inappropriate help if a student's location is unknown or outside mainland China.

Mitigation: Confirm location before giving regional emergency contacts and localize referral channels before deployment outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile template](references/dna-template.md)
- [Growth milestones](references/growth-milestones.md)
- [Learning profile schema and consent model](schemas/README.md)
- [Crisis referral protocol](references/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Chinese-language profile summaries and structured learning-profile data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile access and sharing depend on verified identity and separate consent settings.]

## Skill Version(s):

2.7.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

维护经授权的学生长期学习档案，支持查看、更正、导出和删除学习画像与成长记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, and educators use this skill to maintain a consent-based learning profile and request relevant, limited sharing for personalized tutoring. It does not activate for routine question answering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive student profiles could be accessed or shared without the right person's authorization.

Mitigation: Deploy only where student identities are separated, guardian consent is enforced when required, and field-level permissions limit access and sharing.

Risk: Export or deletion requests may leave student data behind if the host does not implement them.

Mitigation: Require working host-platform export and deletion controls; do not treat the skill as a standalone privacy layer.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile template](artifact/references/dna-template.md)
- [Learning profile schema documentation](artifact/schemas/README.md)
- [Crisis referral protocol](artifact/references/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational responses and structured learning-profile data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile access and sharing require appropriate consent; exports and deletion require host-platform support.]

## Skill Version(s):

2.10.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

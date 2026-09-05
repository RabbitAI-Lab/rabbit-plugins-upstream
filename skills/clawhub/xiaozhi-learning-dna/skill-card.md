## Description:

学生长期学习档案系统：在明确授权下建立、查看、更正、导出、删除学生档案，包括学科强弱、错误模式、学习风格、成长轨迹，以及需单独开关的学习情绪、兴趣信号、家长可见输出、老师写回、跨 Skill 共享和危机转介事实。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, educators, and learning-support agents use this skill to manage a consent-based long-term learning profile for personalized tutoring continuity. It is intended as the storage and authorization layer for learning records, not as a general tutoring or diagnostic agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores sensitive long-term learning profiles about minors.

Mitigation: Deploy only where student identity separation, explicit student or guardian consent, export/delete controls, and field-level access controls are enforced.

Risk: Emotional and motivational inferences can create privacy or safety concerns.

Mitigation: Keep emotion tracking opt-in, require separate sharing consent for parent-visible emotional content, and review whether emotional inference should be enabled for the deployment.

Risk: Cross-skill writebacks could persist unsupported or overbroad profile updates.

Mitigation: Require clear provenance, validate handover payloads, and persist writebacks only after user-visible confirmation.

Risk: Crisis-related handling may depend on local requirements and support channels.

Mitigation: Use localized legal and crisis guidance and record only the minimal crisis referral facts authorized by the safety protocol.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Crisis Referral Protocol](references/crisis-referral-protocol.md)
- [Cross-Subject Connections](references/cross-subject-connections.md)
- [DNA Template](references/dna-template.md)
- [Growth Milestones](references/growth-milestones.md)
- [DNA Profile Schema](schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance and structured JSON profile records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve consent status, identity separation, export/delete controls, and field-level sharing boundaries.]

## Skill Version(s):

2.1.6 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

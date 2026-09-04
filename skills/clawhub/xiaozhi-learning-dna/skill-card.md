## Description:

Builds, reviews, updates, exports, pauses, and deletes a student learning profile only after explicit consent, covering subject strengths and weaknesses, error patterns, learning preferences, growth milestones, and controlled sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External education agents, students, and guardians use this skill to maintain a consent-controlled long-term learning profile for personalized tutoring continuity. It is intended for learning support workflows that need profile access, correction, deletion, export, cross-skill sharing limits, and crisis-escalation boundaries.

### Deployment Geography for Use:

Global; crisis referral resources and minor consent handling should be localized before deployment.

## Known Risks and Mitigations:

Risk: The skill handles sensitive student learning, emotion, sharing, and crisis records, including data about minors.

Mitigation: Deploy only where per-student identity, guardian consent where required, explicit emotion and interest tracking opt-in, and export, correction, deletion, and pause controls are enforced.

Risk: Cross-skill sharing and teacher writeback could expose more profile data than a task requires.

Mitigation: Limit sharing to the minimum necessary profile fields, require the relevant consent flags, and enforce teacher writeback boundaries before accepting updates.

Risk: Crisis handling and minor-consent expectations may vary by locale.

Mitigation: Localize crisis resources and legal consent workflows before production deployment, and record only crisis referral actions rather than sensitive event details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning DNA template](artifact/references/dna-template.md)
- [Growth milestone standards](artifact/references/growth-milestones.md)
- [Cross-subject concept connection templates](artifact/references/cross-subject-connections.md)
- [Crisis referral protocol](artifact/references/crisis-referral-protocol.md)
- [Learning DNA JSON Schema](artifact/schemas/dna-profile.schema.json)
- [Schema overview](artifact/schemas/README.md)
- [Shared vocabulary and consent flags](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON profile fields, consent-control language, and profile update instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be treated as sensitive student-profile material and should honor explicit consent, pause, export, correction, deletion, and sharing controls.]

## Skill Version(s):

2.1.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

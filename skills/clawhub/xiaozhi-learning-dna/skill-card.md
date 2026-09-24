## Description:

学习DNA manages a consent-based long-term learning profile for K-12 students, covering strengths, weak points, learning style, growth history, opt-in learning-emotion signals, family-facing summaries, teacher writeback, cross-skill sharing, and crisis-referral facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External education agents and K-12 learning platforms use this skill to create, inspect, update, export, or delete a student's learning profile only after the required identity and consent checks. It is intended as a storage and authorization layer for personalized tutoring workflows, not as a general answer engine or psychological record.

### Deployment Geography for Use:

China mainland by default; deployments elsewhere require localization of crisis resources, curriculum assumptions, and minor-consent requirements.

## Known Risks and Mitigations:

Risk: Sensitive student profiles may be exposed or changed if a shared chat treats self-declared identity as sufficient.

Mitigation: Bind profiles to authenticated student accounts and require step-up verification before profile reads, export, deletion, or consent changes.

Risk: Cross-skill sharing, teacher writeback, and parent-visible summaries can over-share student data without server-side controls.

Mitigation: Enforce field-level access on the host platform and keep consent gates separate for profile use, emotion tracking, parent sharing, teacher writeback, and cross-skill sharing.

Risk: Crisis referral and minor-consent guidance can be wrong outside the intended regional context.

Mitigation: Localize crisis resources, legal guidance, curriculum assumptions, and minor-consent rules before deployment outside China mainland.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [SKILL.md](artifact/SKILL.md)
- [Learning DNA schema README](artifact/schemas/README.md)
- [DNA profile JSON schema](artifact/schemas/dna-profile.schema.json)
- [Crisis referral protocol](artifact/references/crisis-referral-protocol.md)
- [Platform conventions and localization requirements](artifact/shared/platform-conventions.md)
- [Learning DNA first-profile template](artifact/references/dna-template.md)
- [Growth milestones reference](artifact/references/growth-milestones.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, configuration, guidance]

**Output Format:** [Natural-language guidance plus structured JSON profile and handover records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be constrained by identity confirmation, consent state, field-level access, and regional crisis-localization rules.]

## Skill Version(s):

2.3.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

学习DNA is a student learning-profile skill that, with explicit authorization, helps agents create, inspect, correct, export, and delete long-term learning records covering strengths, weak points, learning style, growth milestones, consent-gated learning emotions, interest signals, parent-visible summaries, teacher writeback, cross-skill sharing, and crisis referral facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External education agents and supervised student-support deployments use this skill to manage consent-controlled student learning profiles for personalized tutoring continuity. It is intended for environments that can enforce student identity separation, guardian consent where required, field-level authorization, and localized crisis-support handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive minors' learning data.

Mitigation: Use it only where the platform enforces per-student identity, guardian consent, field-level access control, and runtime authorization.

Risk: Crisis referral records and support flows need clear storage boundaries.

Mitigation: Resolve the crisis-record rule so support can proceed without consent while persistent storage follows one clear authorized condition.

Risk: Teacher writeback can affect a student's long-term profile.

Mitigation: Require explicit teacher-writeback consent and review each proposed writeback before it is stored.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [DNA profile schema](schemas/dna-profile.schema.json)
- [DNA template](references/dna-template.md)
- [Growth milestones](references/growth-milestones.md)
- [Cross-subject connections](references/cross-subject-connections.md)
- [Crisis referral protocol](references/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or plain text with JSON-compatible profile and handoff fields when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are consent-gated and should be limited to the minimum profile fields needed for the current learning task.]

## Skill Version(s):

2.1.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

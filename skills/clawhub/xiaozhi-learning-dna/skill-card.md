## Description:

A consent-controlled learning-profile skill for creating, reviewing, correcting, exporting, and deleting student records, with optional emotion tracking and growth milestones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning assistants use this skill to manage consent-controlled learning profiles for personalized academic support and growth tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting guardian-consent checks could allow a younger student's record to be saved before required approval.

Mitigation: Use session-only mode until age and guardian-consent checks are consistent; enable persistent profiles only where student isolation, sharing controls, and deletion are enforced, and keep emotion tracking and family sharing separate choices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [DNA profile template](references/dna-template.md)
- [Crisis referral protocol](references/crisis-referral-protocol.md)
- [Profile schema documentation](schemas/README.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured JSON learning profiles and concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Student-specific records; persistence and sensitive sharing require explicit consent.]

## Skill Version(s):

2.12.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

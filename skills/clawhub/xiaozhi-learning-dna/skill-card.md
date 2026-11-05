## Description:

Guides consent-aware management of long-term student learning profiles, including review, correction, export, deletion, and growth milestones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and guardians use this skill to manage a student's learning profile when they choose to create, review, update, export, or delete it. It supports continuity across learning sessions while keeping profile categories subject to separate consent choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting guardian-consent instructions could allow sensitive profiles for younger students to be saved without the promised approval.

Mitigation: Keep long-term storage disabled until the consent instructions are consistent. Before enabling profiles, verify that the host enforces student isolation, required approvals, sharing permissions, and deletion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile schema overview](schemas/README.md)
- [Growth milestones guidance](references/growth-milestones.md)
- [Crisis referral protocol](references/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Text]

**Output Format:** [JSON profile records and concise conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sensitive student data; storage and access controls depend on the host platform.]

## Skill Version(s):

2.12.5 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

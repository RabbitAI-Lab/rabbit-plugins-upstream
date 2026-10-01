## Description:

Maintains a consent-controlled learning profile for students, including progress, study preferences, and optional sensitive observations, with options to review, correct, export, or delete records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and authorized guardians use the skill to manage a long-term learning profile and track learning progress. Educators can contribute limited updates only when the required permissions are in place; routine tutoring does not require profile access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A student profile could expose sensitive minor data to the wrong person or to other skills.

Mitigation: Require confirmed student identity, guardian consent where required, field-level sharing controls, and cross-skill allowlists; otherwise limit use to the current session without long-term storage.

Risk: Stored observations may outlast consent or contain information the student wants corrected or removed.

Mitigation: Keep optional tracking off by default and support requests to review, correct, export, pause, or delete the profile.

## Reference(s):

- [ClawHub release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile template](artifact/references/dna-template.md)
- [Growth milestones](artifact/references/growth-milestones.md)
- [Crisis referral protocol](artifact/references/crisis-referral-protocol.md)
- [Profile schema and consent model](artifact/schemas/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational summaries and profile exports in text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile access and sensitive-field sharing require the applicable consent; users can request corrections, exports, pauses, and deletion.]

## Skill Version(s):

2.9.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

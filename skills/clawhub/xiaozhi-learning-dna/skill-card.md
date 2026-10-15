## Description:

Manages consent-based, long-term learning profiles for Chinese K–12 students, including viewing, correcting, exporting, and deleting records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and authorized educators use this skill to maintain a controlled learning profile for personalized tutoring, with separate permissions for sensitive observations and sharing.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: Sensitive records about minors could be accessed, retained, or shared without appropriate authorization.

Mitigation: Enforce per-student identity, guardian consent where required, separate field-level permissions, and student-controlled viewing, export, correction, and deletion.

Risk: Crisis referrals or consent practices may be inappropriate outside the intended locale.

Mitigation: Scope deployment to Chinese-language K–12 use; replace emergency contacts, school and legal assumptions, and consent rules before use elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile template](references/dna-template.md)
- [Growth milestone criteria](references/growth-milestones.md)
- [Crisis referral protocol](references/crisis-referral-protocol.md)
- [Learning profile schema and consent model](schemas/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and structured learning-profile summaries or exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile access and sharing require the relevant consent; ordinary tutoring does not read the profile by default.]

## Skill Version(s):

2.11.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

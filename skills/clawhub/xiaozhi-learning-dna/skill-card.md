## Description:

With explicit consent, this skill maintains a student's learning profile and supports viewing, correcting, exporting, and deleting it, with separate controls for sensitive records and sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and guardians use this skill to manage a consented long-term learning profile, including learning strengths, preferences, and growth. Connected learning skills can update limited fields with approval; emotional records and sharing require separate consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting onboarding instructions could lead to long-term storage of a younger student's records without consistently confirmed guardian approval.

Mitigation: Confirm age and required guardian approval before enabling long-term storage; otherwise keep storage disabled and use only current-session information.

Risk: Sensitive student records could be exposed if the host does not enforce student isolation, field permissions, and deletion.

Mitigation: Use a host that enforces these controls, and enable emotional records or sharing only after separate agreement.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile template](artifact/references/dna-template.md)
- [Crisis referral protocol](artifact/references/crisis-referral-protocol.md)
- [Learning profile schema](artifact/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured learning-profile JSON and concise text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term storage and sharing are consent-controlled; emotional records require separate consent.]

## Skill Version(s):

2.12.6 (source: release evidence, artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

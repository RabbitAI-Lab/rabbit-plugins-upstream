## Description:

Analyzes Chinese middle- and high-school biology mistakes across six dimensions to identify root causes and report learning weaknesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this skill to pinpoint recurring biology misconceptions, plan targeted practice, and request weakness reports. Initial mistake intake and repeat counts remain with the general correction notebook.

### Deployment Geography for Use:

Chinese-language K–12 learning-profile settings; crisis referrals must match the student's location.

## Known Risks and Mitigations:

Risk: The bundled handover schema is inconsistent about who may send wrong-answer data.

Mitigation: Review the handover schema before production installation and accept initial wrong-answer intake only from the correction notebook.

Risk: Student learning profiles may expose sensitive educational data through retention or cross-skill and parent sharing.

Mitigation: Enforce consent, deletion and export controls, and limits on cross-skill and parent sharing.

Risk: Learning distress or health questions can require support beyond educational guidance.

Mitigation: Use location-appropriate crisis referrals for safety signals and avoid medical diagnosis or treatment advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-error-dna)
- [Biology error dimension table](references/biology-error-dimension-table.md)
- [Learning profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language guidance and on-request weakness reports; structured handovers and profile updates when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports depend on available mistakes; persistent records and sharing require consent.]

## Skill Version(s):

2.8.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

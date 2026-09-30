## Description:

Analyzes children's images or videos for signs of distress and provides emotion reports, alerts, and guidance for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and childcare staff use the skill to review children's images or videos for possible distress, receive analysis reports and alerts, and retrieve historical reports. Its findings support, but do not replace, direct adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's images, videos, and report history may be sent to cloud services.

Mitigation: Use only with appropriate caregiver or institutional consent and agreed retention and deletion practices for the configured service.

Risk: The skill may silently create or reuse persistent identities and store service tokens locally, risking account mix-ups or unauthorized access.

Mitigation: Keep caregiver accounts separate and protect local tokens and access to historical reports.

Risk: Emotion assessments may be misleading if treated as definitive evidence of a child's state or safety.

Mitigation: Have a caregiver review findings and respond in person when needed; do not substitute the skill for adult supervision.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured emotion analysis reports and historical report lists with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be printed or saved to a file.]

## Skill Version(s):

1.0.29 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

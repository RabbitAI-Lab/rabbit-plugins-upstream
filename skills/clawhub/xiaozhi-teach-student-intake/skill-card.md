## Description:

Helps independent teachers plan diagnostic trial lessons, document observations, and create minimal student learning profiles after guardian consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent K–12 teachers use this skill to interview families, assess a prospective student's starting point, design a trial lesson, draft teacher-reviewed follow-ups, and create a consent-based student profile and course-package record upon enrollment.

### Deployment Geography for Use:

Mainland China (K–12 independent-teacher context)

## Known Risks and Mitigations:

Risk: Saving a minor's teaching record without guardian consent.

Mitigation: Confirm guardian consent before saving any profile or teaching record; offer session-only guidance if consent is unavailable.

Risk: Identifying or contacting a child through stored records.

Mitigation: Use pseudonyms and keep real names, contact details, and emergency contacts outside the workspace.

Risk: Inappropriate or misleading family-facing follow-up drafts.

Mitigation: Have the teacher review drafts and send messages personally; do not automate contact.

Risk: Student records or enrollment ledger entries persisting beyond their intended use.

Mitigation: Review stored course-package fields and honor the consent, retention, and deletion controls for student profiles.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Student basic information form](artifact/references/student-basic-info-form.md)
- [5W needs interview checklist](artifact/references/needs-interview-5w-checklist.md)
- [Diagnostic assessment card](artifact/references/diagnosis-card-template.md)
- [Five-part trial lesson structure](artifact/references/trial-lesson-5-segment-structure.md)
- [Trial observation record](artifact/references/trial-observation-record.md)
- [Trial follow-up scripts](artifact/references/followup-scripts-trial-conversion.md)
- [Formal student profile template](artifact/references/formal-student-profile-template.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Chinese-language lesson plans, interview and observation notes, follow-up drafts, and structured student profiles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profiles and course-package ledger entries may be persisted after consent; messages to families require teacher review.]

## Skill Version(s):

2.11.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

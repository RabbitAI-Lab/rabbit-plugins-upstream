## Description:

把试听从"体验课"变成一次双向诊断，并按最小化原则给新学员建档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to run a diagnostic trial lesson intake flow, collect only necessary student learning information, draft limited trial-to-enrollment follow-up wording, and create a learner profile when consent is confirmed.

### Deployment Geography for Use:

China Mainland; localization and legal review are required before use in other regions.

## Known Risks and Mitigations:

Risk: Minor-related student intake and trial-lesson records may be stored without sufficiently enforceable consent and retention controls.

Mitigation: Require consent and retention fields before any student card is saved, and confirm the runtime can read and enforce those fields.

Risk: Single-trial observations can be mistaken for durable conclusions about a student.

Mitigation: Do not persist single-trial observations marked insufficient_sample as long-term conclusions; keep them as limited trial evidence unless later confirmed.

Risk: Student records may become more sensitive if direct identifiers or contact details are captured.

Mitigation: Use aliases, avoid real names and contact details, and keep family contact information outside the skill-managed workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Student basic information form](references/student-basic-info-form.md)
- [Needs interview 5W checklist](references/needs-interview-5w-checklist.md)
- [Needs profile card](references/needs-profile-card.md)
- [Diagnosis card template](references/diagnosis-card-template.md)
- [Trial lesson 5-segment structure](references/trial-lesson-5-segment-structure.md)
- [Trial observation record](references/trial-observation-record.md)
- [Trial conversion follow-up scripts](references/followup-scripts-trial-conversion.md)
- [Formal student profile template](references/formal-student-profile-template.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Shared vocabulary](shared/vocab.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured workspace fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce studentCards, coursePackageLedger, and progressEvidence entries for user-confirmed storage; avoids contact details and other unnecessary identifying data.]

## Skill Version(s):

2.1.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

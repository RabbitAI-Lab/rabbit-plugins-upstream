## Description:

Helps independent teachers run a diagnostic trial lesson and create a minimized student profile after confirming guardian consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to structure trial lessons as diagnostic sessions, collect only teaching-relevant intake data, draft trial-to-enrollment follow-up language, and create a student profile for later teaching workflows.

### Deployment Geography for Use:

Mainland China for the bundled K12 curriculum, consent defaults, safety routing, and Simplified Chinese teaching scripts; other regions require localization before student-facing use.

## Known Risks and Mitigations:

Risk: The skill handles minor students' learning profiles in persistent platform memory.

Mitigation: Confirm guardian consent before profile creation, keep cross-skill and parent-sharing controls explicit, and use retention, export, and deletion controls.

Risk: Users may try to enter identifying or contact information during intake.

Mitigation: Use aliases and teaching-relevant fields only; do not store real names, contact details, addresses, school or class, birthdates, or family information.

Risk: A single trial lesson can lead to overconfident long-term judgments about a student.

Mitigation: Mark trial observations as insufficient sample evidence and record only observed facts, not personality or ability labels.

Risk: The bundled shared workspace schema is broader than this intake workflow needs.

Mitigation: Limit writes to the fields used for student cards, initial course package ledgers, and trial diagnostic evidence.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [Student Basic Information Form](artifact/references/student-basic-info-form.md)
- [Needs Interview 5W Checklist](artifact/references/needs-interview-5w-checklist.md)
- [Needs Profile Card](artifact/references/needs-profile-card.md)
- [Diagnosis Card Template](artifact/references/diagnosis-card-template.md)
- [Trial Lesson 5 Segment Structure](artifact/references/trial-lesson-5-segment-structure.md)
- [Trial Observation Record](artifact/references/trial-observation-record.md)
- [Trial Conversion Follow-Up Scripts](artifact/references/followup-scripts-trial-conversion.md)
- [Formal Student Profile Template](artifact/references/formal-student-profile-template.md)
- [Platform Conventions](artifact/shared/platform-conventions.md)
- [Solo Teacher Workspace Schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Guidance]

**Output Format:** [Markdown templates, scripted teaching guidance, and structured workspace field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces teacher-facing drafts and profile records for consented student intake; it does not send messages or collect contact details.]

## Skill Version(s):

2.1.6 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

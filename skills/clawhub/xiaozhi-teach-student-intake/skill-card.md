## Description:

Guides solo teachers through guardian-consented trial lesson intake, 5W needs interviews, short baseline diagnostics, trial observations, fit assessment, and minimal student profile creation without storing direct contact identifiers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to turn trial lessons into structured diagnostic intake and create minimal student records after guardian consent. It supports needs interviews, baseline checks, trial lesson planning, observation notes, fit decisions, and handoff boundaries for later scheduling or lesson-record workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles persistent records about minor students, and the included schema does not enforce every consent requirement described in the instructions.

Mitigation: Require the storage layer or release environment to reject student records without complete consent, guardian authorization where needed, and a retention deadline.

Risk: Student intake can accidentally collect direct identifiers or contact details that are not needed for the teaching record.

Mitigation: Store only aliases, grade band, learning goals, availability, communication preference, consent, and diagnostic learning evidence; keep phone numbers, chat IDs, real names, addresses, and school details outside the skill.

Risk: A trial lesson is a limited observation and can lead to overconfident conclusions about a learner.

Mitigation: Treat trial observations as provisional evidence, avoid fixed trait labels, and update the formal student profile as later learning evidence accumulates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Student basic information form](artifact/references/student-basic-info-form.md)
- [Needs interview 5W checklist](artifact/references/needs-interview-5w-checklist.md)
- [Needs profile card](artifact/references/needs-profile-card.md)
- [Diagnosis card template](artifact/references/diagnosis-card-template.md)
- [Trial lesson 5-segment structure](artifact/references/trial-lesson-5-segment-structure.md)
- [Trial observation record](artifact/references/trial-observation-record.md)
- [Trial conversion follow-up scripts](artifact/references/followup-scripts-trial-conversion.md)
- [Formal student profile template](artifact/references/formal-student-profile-template.md)
- [Solo teacher workspace schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text templates for intake forms, diagnosis cards, observation records, student profile cards, and follow-up scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces teacher-facing drafts and records; communication scripts are intended for teacher review and manual use.]

## Skill Version(s):

2.1.10 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

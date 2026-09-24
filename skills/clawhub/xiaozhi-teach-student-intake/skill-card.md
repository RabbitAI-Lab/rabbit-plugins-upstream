## Description:

把试听从"体验课"变成一次双向诊断，并按最小化原则给新学员建档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language independent K12 tutors use this skill to run consent-gated trial lesson intake, collect only minimal learning information, and create a student profile after a diagnostic trial lesson. It supports need interviews, short pre-assessments, trial observation notes, fit judgment, and limited trial-to-enrollment follow-up drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent learning and business records about minors.

Mitigation: Confirm guardian consent before creating a card, use aliases instead of real names, keep contact details outside the workspace, and review retention fields before use.

Risk: A trial intake may surface safety or crisis signals outside normal tutoring scope.

Mitigation: Stop the intake flow and follow the crisis referral protocol, including trusted adult or emergency-resource referral based on location.

Risk: Drafted diagnosis or follow-up language could overstate a student's needs or the expected teaching outcome.

Mitigation: Require the teacher to review all parent-facing messages, keep observations factual, and avoid score-improvement promises.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Student basic info form](references/student-basic-info-form.md)
- [Needs interview 5W checklist](references/needs-interview-5w-checklist.md)
- [Diagnosis card template](references/diagnosis-card-template.md)
- [Trial lesson 5-segment structure](references/trial-lesson-5-segment-structure.md)
- [Trial observation record](references/trial-observation-record.md)
- [Formal student profile template](references/formal-student-profile-template.md)
- [Follow-up scripts for trial conversion](references/followup-scripts-trial-conversion.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese Markdown guidance with structured student intake and profile fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces consent-gated drafts and records; excludes contact details and real identifiers by design.]

## Skill Version(s):

2.3.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

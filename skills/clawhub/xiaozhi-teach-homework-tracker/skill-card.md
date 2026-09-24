## Description:

作业跟进管家 helps independent teachers register homework, track submission status, classify error causes, and turn homework evidence into next-lesson priorities while leaving grading, parent messaging, and lesson logs to the teacher or adjacent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill in Chinese K12 homework workflows to record assignments, monitor seven homework states, classify error causes, identify repeated weaknesses, and prepare next-lesson focus notes. It is designed for teacher-reviewed records and low-sensitivity student aliases rather than direct student grading or automated parent messaging.

### Deployment Geography for Use:

Mainland China unless localized for another jurisdiction

## Known Risks and Mitigations:

Risk: Homework records for minors can expose student identity or learning patterns if stored with real names or unnecessary raw work.

Mitigation: Confirm consent settings, use aliases instead of real names, and keep records scoped to completion status, error dimensions, knowledge points, and follow-up actions.

Risk: Generated validation questions or follow-up exercises may be incorrect or unsuitable for the student's grade band.

Mitigation: Require teacher review before any generated question reaches students or is reused in a resource bank.

Risk: Repeated-error thresholds could incorrectly label a student weakness if written directly into durable student records.

Mitigation: Store threshold evidence first and write primary weaknesses only after explicit teacher confirmation.

Risk: The workflow and crisis referral defaults are designed for Chinese-language, mainland-China K12 settings.

Mitigation: Localize consent rules, curriculum assumptions, and emergency referral channels before deployment in another jurisdiction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [Completion tracking views](references/completion-tracking-views.md)
- [Error reflow checklist template](references/error-reflow-checklist-template.md)
- [Persistent weakness file template](references/persistent-weakness-file-template.md)
- [Pre-diagnosis output template](references/pre-diagnosis-output-template.md)
- [Student homework profile template](references/student-homework-profile-template.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Shared vocabulary](shared/vocab.md)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown and structured text guidance with workspace field names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed outputs; generated validation questions require human checking before student use or resource-bank reuse.]

## Skill Version(s):

2.3.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

把试听从“体验课”变成一次双向诊断，并按最小化原则给新学员建档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to run diagnostic trial lessons, collect minimal student intake information, draft follow-up language, and create pseudonymous student records for tutoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores student learning records and extends into renewal, churn, scheduling-state, and retention workflows beyond a narrow intake boundary.

Mitigation: Review scope before deployment, route renewal, churn, scheduling, lesson logs, and stage reports to companion skills, and keep this skill focused on intake and pseudonymous trial records.

Risk: The skill handles records about minors and tutoring needs.

Mitigation: Confirm guardian consent before creating or sharing records, retain only the minimum fields needed for teaching, and define a deletion window for trial students who do not enroll.

Risk: Crisis-support references may include China-specific contacts.

Mitigation: Replace crisis contacts and referral instructions with locally appropriate resources before use outside that jurisdiction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Student Basic Info Form](artifact/references/student-basic-info-form.md)
- [Needs Interview 5W Checklist](artifact/references/needs-interview-5w-checklist.md)
- [Trial Lesson 5-Segment Structure](artifact/references/trial-lesson-5-segment-structure.md)
- [Trial Observation Record](artifact/references/trial-observation-record.md)
- [Formal Student Profile Template](artifact/references/formal-student-profile-template.md)
- [Follow-up Scripts for Three Stages](artifact/references/followup-scripts-three-stages.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance and structured student-record field content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to use pseudonymous student fields and avoid contact details or direct message sending.]

## Skill Version(s):

2.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

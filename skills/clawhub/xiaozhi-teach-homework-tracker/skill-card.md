## Description:

帮助独立教师登记作业、追踪提交与订正状态、归纳错因，并确定下节课的教学重点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking independent K–12 teachers use this skill to track homework completion, identify recurring learning difficulties, and prepare follow-up teaching. Teachers review student-facing content and confirm lasting changes to learner records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Homework records could expose information about minors when shared beyond the teacher's intended audience.

Mitigation: Use student aliases, confirm consent settings before sharing with other skills or parents, and honor pause, delete, and export requests.

Risk: An incorrect recurring-weakness label could persist in a student's profile.

Mitigation: Present supporting homework evidence and require teacher confirmation before updating the student profile.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [Completion tracking views](references/completion-tracking-views.md)
- [Error reflow checklist](references/error-reflow-checklist-template.md)
- [Next-lesson pre-diagnosis template](references/pre-diagnosis-output-template.md)
- [Student homework profile template](references/student-homework-profile-template.md)
- [Teacher workspace schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON records]

**Output Format:** [Chinese-language summaries and structured homework records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses student aliases; requires teacher confirmation before recording persistent weaknesses.]

## Skill Version(s):

2.6.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

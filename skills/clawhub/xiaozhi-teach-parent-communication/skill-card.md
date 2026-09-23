## Description:

家长沟通助手 helps independent Chinese K12 teachers draft concrete, low-anxiety parent communications and record channel/status summaries without sending messages or changing student files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to draft parent updates, replies about progress or grades, renewal notes, and parent-group announcements in Chinese K12 teaching contexts. It checks consent and communication frequency, keeps individual feedback private, and records only parentCommunicationLogs[] summaries after teacher review.

### Deployment Geography for Use:

China Mainland by default; localize crisis resources, curriculum assumptions, and minor-data rules before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill may save parent communication logs when recording should be paused or not authorized.

Mitigation: Before installation, require a rule that no communication log is saved when a student is paused, completed, pending deletion, lacks consent, or when the teacher, student, or guardian says not to remember the interaction.

Risk: The skill reads sensitive student records and saves communication summaries.

Mitigation: Limit use to the intended Chinese K12 teacher-workspace context, avoid storing contacts or family details, and keep persistent output limited to approved parentCommunicationLogs[] summaries.

Risk: A generated parent message could expose individual student details in a group setting.

Mitigation: Require specific-student feedback to use one-to-one channels only, and use group announcements only for general, non-identifying class information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [Communication principles examples](references/communication-principles-examples.md)
- [Typical scenario scripts](references/typical-scenario-scripts.md)
- [Weekly group announcement template](references/weekly-group-announcement-template.md)
- [Crisis exception](shared/crisis-exception.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Chinese prose drafts with structured parentCommunicationLogs[] fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts are teacher-reviewed and not sent by the skill; persistent output is limited to parent communication log summaries.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

帮独立教师把临时想起来的家长消息变成有节奏、低焦虑、具体且可操作的沟通草稿，并记录沟通渠道与发送状态。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to draft parent-facing updates about learning progress, concerns, renewal discussions, and class announcements while keeping specific student feedback private and teacher-reviewed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive student-parent communication may be drafted from incorrect or incomplete consent and status data.

Mitigation: Require teacher review before use, verify parentCommunicationAllowed and emotionSharingWithParent before drafting, and avoid drafting or logging for paused or deletion-pending students until the student record is confirmed.

Risk: Emotional details about a student could be shared without appropriate consent or context.

Mitigation: Keep emotional or classroom-state details out of parent drafts unless consent provenance is verified; describe observable learning behavior only and use crisis referral guidance for safety signals.

Risk: Communication logs may not match the workspace schema expected by the deployment.

Mitigation: Confirm that parentCommunicationLogs[] supports the exact fields written by the skill before deployment.

## Reference(s):

- [Communication principles examples](references/communication-principles-examples.md)
- [Typical scenario scripts](references/typical-scenario-scripts.md)
- [Weekly group announcement template](references/weekly-group-announcement-template.md)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [Publisher profile](https://clawhub.ai/user/qizhitang)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain-text communication drafts with structured communication-log fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft-only; does not send messages; may append parentCommunicationLogs[] entries when the teacher records communication status.]

## Skill Version(s):

2.1.12 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

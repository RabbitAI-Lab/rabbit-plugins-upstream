## Description:

帮助独立教师起草具体、低焦虑、可操作的家长沟通内容，并记录沟通渠道和发送状态；消息由教师审核后自行发送。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent K–12 teachers use this skill to draft parent updates, replies about learning progress and concerns, renewal messages, and general group notices. It checks communication consent and message frequency, then lets the teacher review and send each draft.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: A parent message could disclose a student's learning or emotional information without consent.

Mitigation: Check parent-communication consent before drafting, separately check consent for emotional details, and keep student-specific feedback out of group announcements.

Risk: Crisis guidance intended for mainland China could be unsuitable elsewhere.

Mitigation: Confirm the user's region and localize crisis contacts and referral resources before use outside mainland China.

Risk: Communication logs may not be supported by every workspace schema.

Mitigation: Verify that the platform supports the expected communication-log fields before relying on persistent records.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [Communication principles and examples](references/communication-principles-examples.md)
- [Typical scenario scripts](references/typical-scenario-scripts.md)
- [Weekly group announcement template](references/weekly-group-announcement-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Simplified Chinese message drafts and communication guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts are not sent automatically; the teacher reviews and sends them. When permitted, a communication log records the channel and draft or sent status.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

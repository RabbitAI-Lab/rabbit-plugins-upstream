## Description:

帮助独立教师起草具体、低焦虑的中文家长沟通消息，并在获得授权后记录简要沟通状态；不代替教师发送消息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师用它起草面向家长的课后反馈、问题沟通、续课说明及不涉及个别学员的群公告，并跟踪沟通状态。教师审核草稿后自行发送。

### Deployment Geography for Use:

Global (Chinese-language K–12 teaching contexts)

## Known Risks and Mitigations:

Risk: A draft or log could disclose student information without valid parent-communication consent or share emotional observations beyond the parent's authorization.

Mitigation: Keep parentCommunicationAllowed and emotionSharingWithParent consent settings current; check them before drafting or logging, and require crossSkillSharing before sharing across skills.

Risk: A group announcement could reveal an individual student's performance.

Mitigation: Use group announcements only for general class information; share student-specific feedback privately after teacher review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [Communication principles and examples](references/communication-principles-examples.md)
- [Typical scenario scripts](references/typical-scenario-scripts.md)
- [Weekly group announcement template](references/weekly-group-announcement-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language message drafts and brief structured communication logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts are not sent automatically; logs record channel and draft/sent status without contact details or verbatim parent replies.]

## Skill Version(s):

2.8.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

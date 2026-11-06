## Description:

帮助独立教师按授权和沟通场景起草具体、低焦虑且可执行的家长沟通内容，并记录沟通状态。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师可用此技能起草课后反馈、进度说明、续课沟通和通用家长群公告，并记录沟通渠道与发送状态。教师审核草稿后自行发送。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Communication summaries may persist in the teacher workspace.

Mitigation: Use student aliases, confirm relevant consent, review each draft before sending, and pause memory when persistence is not needed.

Risk: Host storage protections and separately installed companion skills were not verified.

Mitigation: Avoid including unnecessary sensitive details and confirm the workspace's storage protections.

## Reference(s):

- [Typical Scenario Scripts](references/typical-scenario-scripts.md)
- [Communication Principles Examples](references/communication-principles-examples.md)
- [Weekly Group Announcement Template](references/weekly-group-announcement-template.md)
- [Crisis Exception](shared/crisis-exception.md)
- [Crisis Referral Protocol](shared/crisis-referral-protocol.md)
- [Teacher Workspace Schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise message drafts and communication log entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts require teacher review; the teacher sends messages.]

## Skill Version(s):

2.12.6 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

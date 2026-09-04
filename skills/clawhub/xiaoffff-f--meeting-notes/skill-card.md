## Description:

把零散的会议记录、聊天记录或语音转写整理成结构化的会议纪要。当用户说"整理会议纪要"、"帮我总结这次会议"、"把这段记录变成纪要"、"meeting notes"、"meeting summary"时使用。适用于例会、项目评审、客户沟通等场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoffff-f](https://clawhub.ai/user/xiaoffff-f)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, project teams, and external collaborators use this skill to turn rough meeting notes, chat logs, or transcripts into structured meeting minutes with decisions, action items, owners, deadlines, and open issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated meeting minutes may omit source details or use a format that does not match the user's intent.

Mitigation: Review the generated minutes against the original notes or transcript before sharing or relying on them.

Risk: Action item owners or deadlines may be absent or ambiguous in the source material.

Mitigation: Leave missing meeting metadata blank and mark unclear owners as 待确认 rather than adding unsupported details.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown meeting minutes with headings, bullet lists, and an action-item table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source meaning, leaves missing meeting metadata blank, marks unclear action owners as 待确认, and omits unsupported sections instead of fabricating content.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

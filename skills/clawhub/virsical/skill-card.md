## Description: <br>
Virsical 威思客智慧空间管理平台集成技能，用于查询或预订会议、查看个人会议、查询访客记录、创建工单报修，并支持中英双语交互。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wafer](https://clawhub.ai/user/wafer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and workplace support staff use this skill to check meeting-room availability, book rooms, view their meetings, query visitor records, and create facility work orders through Virsical. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles account authorization codes and stores refreshable account tokens locally after login. <br>
Mitigation: Use the skill only in trusted private sessions, avoid sharing authorization codes in retained transcripts, and treat the local skill directory as sensitive after authentication. <br>
Risk: The skill can create live meeting bookings and facility work orders on behalf of the user. <br>
Mitigation: Require confirmation of exact booking or work-order details before submission, including time, room or project, description, and priority. <br>


## Reference(s): <br>
- [Virsical API Reference](references/api_reference.md) <br>
- [Virsical OAuth2 认证流程](references/auth_flow.md) <br>
- [Virsical 命令参考](references/commands.md) <br>
- [Virsical Error Codes](references/error_codes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown tables and lists with inline shell commands and concise status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bilingual Chinese and English user-facing responses; avoids presenting full raw API JSON.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
This skill helps an agent use the porteden CLI to manage Google and Outlook calendars, including listing calendars, querying events, searching events, creating meetings, and updating or deleting events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect and manage personal calendar events through porteden. It is intended for lightweight calendar workflows such as viewing today's agenda, finding events, and creating or changing meetings after confirming the active account and target event. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete calendar events through porteden. <br>
Mitigation: Require an explicit preview and user confirmation before any calendar-changing command is executed. <br>
Risk: Calendar data may be sent to external Google or Outlook calendar APIs despite local-only privacy wording in the artifact. <br>
Mitigation: Use only the intended calendar account, confirm the active profile before use, and avoid sending sensitive calendar content unless external API access is acceptable. <br>
Risk: The artifact contains conflicting trigger-scope and privacy guidance. <br>
Mitigation: Invoke the skill only for explicit calendar tasks and treat calendar event text as untrusted content. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include command suggestions, calendar query results, execution logs, and structured JSON responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

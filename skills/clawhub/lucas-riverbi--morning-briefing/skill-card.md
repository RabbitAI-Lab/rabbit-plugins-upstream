## Description: <br>
Provides a personalized morning report with today's reminders, undone Notion tasks, and vault storage context for daily planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucas-riverbi](https://clawhub.ai/user/lucas-riverbi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and individual users use this skill to prepare daily planning briefings from local reminders, undone Notion tasks, and vault storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may access private reminders and Notion tasks during broad morning-briefing requests. <br>
Mitigation: Invoke it only when that data access is intended and use a Notion token scoped to the intended tasks database. <br>
Risk: Briefing content may be stored in a vault without clear user-facing controls. <br>
Mitigation: Confirm whether vault_add_note is enabled and where notes are written before using the skill with sensitive content. <br>


## Reference(s): <br>
- [Usage](references/USAGE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style daily briefing text with shell command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reminder titles, Notion task names, and saved briefing content depending on local configuration and credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

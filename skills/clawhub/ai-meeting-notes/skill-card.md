## Description: <br>
Messy notes to clear action items: paste meeting notes, transcripts, or other text to get summaries, action items with owners and deadlines, saved notes, search support, and integrated to-do tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffjhunter](https://clawhub.ai/user/jeffjhunter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees, teams, and individual contributors use this skill to turn pasted meeting notes, transcripts, email threads, or chat exports into concise summaries, action items, decisions, and follow-up tasks. It is intended for local workspace note capture and to-do tracking without a meeting bot or external setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pasted notes and transcripts may be saved verbatim in local workspace files, including sensitive meeting content. <br>
Mitigation: Use the skill in a private workspace, redact sensitive transcripts before processing, and review or delete files in meeting-notes/ when retention is no longer needed. <br>
Risk: Selected action items may persist in todo.md and remain searchable in later sessions. <br>
Mitigation: Add only the tasks that should be tracked, periodically review todo.md, and remove completed or sensitive items. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jeffjhunter/skills/ai-meeting-notes) <br>
- [Publisher profile](https://clawhub.ai/user/jeffjhunter) <br>
- [Publisher homepage](https://jeffjhunter.com) <br>
- [Preferences template](artifact/assets/PREFERENCES-template.md) <br>
- [To-do template](artifact/assets/TODO-template.md) <br>
- [Output example](artifact/examples/output-example.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown notes, chat summaries, checklist-style tasks, optional JSON/table/Slack/email formats, and workspace files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save full meeting notes under meeting-notes/ and selected tasks in todo.md; preserves raw pasted notes in saved Markdown files when used as directed.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

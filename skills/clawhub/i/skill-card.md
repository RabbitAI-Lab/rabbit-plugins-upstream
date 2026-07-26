## Description: <br>
Memo helps an agent record work notes, search and summarize history, manage todos, and generate reports from a local JSON store. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qu8](https://clawhub.ai/user/qu8) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and individual users use this skill as a personal work memo assistant for capturing spoken or typed work events, tracking todos, searching past records, and exporting time-bounded work reports. Developers can also use its Python and CLI interfaces to operate the same local record store. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores work notes locally and can export reports that may contain sensitive operational details. <br>
Mitigation: Require user confirmation before saving or exporting records, and avoid recording sensitive data unless the user explicitly intends local storage. <br>
Risk: The reminder workflow includes a direct SQLite automation fallback that may modify WorkBuddy reminder state outside normal tool controls. <br>
Mitigation: Disable or remove the SQLite fallback unless explicitly trusted; prefer scoped automation tool calls and confirm before creating, updating, pausing, or deleting reminders. <br>
Risk: Record modification and deletion workflows can alter stored history and synchronize reminder changes. <br>
Mitigation: Show the matched content and event ID before destructive changes, require confirmation for deletion, and report reminder synchronization actions back to the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qu8/skills/i) <br>
- [Publisher profile](https://clawhub.ai/user/qu8) <br>
- [WorkBuddy documentation](https://www.codebuddy.cn/docs/workbuddy/Overview) <br>
- [README](artifact/README.md) <br>
- [Field recognition rules](artifact/references/field-rules.md) <br>
- [Report format](artifact/references/report-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text confirmations, Markdown reports, JSON records, and Python or CLI snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include event IDs, local file paths, reminder schedule details, and exported Markdown report paths.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata, SKILL.md frontmatter, skill.yaml, README version history) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

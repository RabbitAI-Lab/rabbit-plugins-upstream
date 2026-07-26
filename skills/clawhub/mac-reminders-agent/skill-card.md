## Description: <br>
Integrates an agent with macOS Reminders to list, add, edit, delete, complete, and parse suggested reminders across multiple lists, priorities, recurrence rules, and English, Korean, Japanese, and Chinese responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[swancho](https://clawhub.ai/user/swancho) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users on macOS use this skill to let an agent manage local Reminders, including list review, creation, updates, completion, deletion, recurring reminders, and action-item suggestions from meeting notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change local macOS Reminders, including edits, completions, and deletes. <br>
Mitigation: Grant Reminders permission only when this access is intended, and confirm the exact reminder ID before edit, complete, or delete commands. <br>
Risk: Reminder output may contain sensitive personal or work information, and scheduled examples can write that output to shared /tmp log files. <br>
Mitigation: Avoid logging reminder output to shared /tmp files; configure cron or LaunchAgent jobs only when scheduled background checks are desired and use private log locations. <br>
Risk: Meeting-note parsing may misread an action item, due date, or priority. <br>
Mitigation: Present parsed items for user approval before adding them; use the parse command as suggestions and call add only for approved reminders. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/swancho/skills/mac-reminders-agent) <br>
- [Publisher profile](https://clawhub.ai/user/swancho) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target a local macOS Reminders store and may require macOS Reminders permission, Node.js 18+, npm, and Swift from Xcode Command Line Tools.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

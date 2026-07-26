## Description: <br>
Manage Apple Reminders via the remindctl CLI on macOS, with support for listing, adding, editing, completing, deleting, filtering by date, and returning JSON or plain output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Mac users use this skill to let an agent inspect and manage Apple Reminders through remindctl on macOS, including reminders, lists, due dates, completion status, and scripting-friendly output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit, complete, rename, or delete reminders and lists, including commands that use --force. <br>
Mitigation: Confirm destructive or state-changing remindctl commands before execution, especially delete, rename, complete, and --force operations. <br>
Risk: The skill depends on a third-party Homebrew tap and requires Apple Reminders access on the Mac where commands run. <br>
Mitigation: Install only when the user trusts the remindctl tap and grant Reminders permission only on intended macOS systems. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/steipete/skills/apple-reminders) <br>
- [remindctl GitHub Project](https://github.com/steipete/remindctl) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands; remindctl can return JSON, plain TSV, quiet counts, or terminal text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [macOS-only; requires remindctl and Apple Reminders permission.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

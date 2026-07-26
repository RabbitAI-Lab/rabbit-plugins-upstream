## Description: <br>
Manage Apple Notes via the memo CLI on macOS, including creating, viewing, editing, deleting, searching, moving, and exporting notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External macOS users use this skill to have an agent manage Apple Notes through the memo CLI for note lookup, creation, edits, folder movement, export, and deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, edit, export, move, and delete Apple Notes that may contain sensitive personal or business information. <br>
Mitigation: Confirm the exact note and requested action before edit, move, export, or delete operations. <br>
Risk: The skill depends on the external memo CLI and Apple Notes Automation permissions. <br>
Mitigation: Install memo only from a trusted source and grant Notes.app Automation access only when needed. <br>


## Reference(s): <br>
- [ClawHub Apple Notes skill page](https://clawhub.ai/steipete/skills/apple-notes) <br>
- [memo CLI homepage](https://github.com/antoniorodr/memo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [macOS-only; requires the memo CLI and Apple Notes.app Automation access for note operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

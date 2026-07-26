## Description: <br>
Manage Google Tasks from the command line - view, create, update, delete tasks and task lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bro3886](https://clawhub.ai/user/bro3886) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to manage Google Tasks through the gtasks CLI, including viewing, creating, updating, completing, deleting, and exporting tasks and task lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act on an authenticated Google Tasks account, including creating, completing, deleting, and changing task lists. <br>
Mitigation: Require explicit user confirmation before delete, bulk-complete, or task-list change actions. <br>
Risk: OAuth client secrets, stored tokens, and exported task files can expose account access or personal task data if printed, shared, or written with broad permissions. <br>
Mitigation: Do not print or share GTASKS_CLIENT_SECRET, keep token and export files protected, and use restrictive file permissions for local credential files. <br>


## Reference(s): <br>
- [gtasks project homepage](https://github.com/BRO3886/gtasks) <br>
- [Quick Reference Card](references/QUICK-REFERENCE.md) <br>
- [Advanced Usage and Integration](references/ADVANCED.md) <br>
- [gtasks releases](https://github.com/BRO3886/gtasks/releases) <br>
- [dateparse examples](https://github.com/araddon/dateparse#extended-example) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands, configuration notes, and optional JSON or CSV command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may read or modify Google Tasks through an authenticated gtasks CLI session.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter metadata version is 1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

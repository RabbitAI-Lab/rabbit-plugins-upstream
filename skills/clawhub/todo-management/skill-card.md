## Description: <br>
Per-workspace SQLite todo manager (./todo.db) with groups and task statuses (pending/in_progress/done/skipped), operated via {baseDir}/scripts/todo.sh for adding, listing, editing, moving, and removing entries and managing groups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lstpsche](https://clawhub.ai/user/lstpsche) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to manage a project-local todo list through an agent-controlled SQLite CLI. It supports grouped tasks, task status changes, concise confirmations, and explicit list display when requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Todo entries are stored in a local workspace SQLite database and may persist sensitive text if users add it. <br>
Mitigation: Avoid storing secrets or sensitive personal data in todos, and choose the workspace or TODO_DB path intentionally. <br>
Risk: Clear, remove, and group deletion requests can delete or move tasks. <br>
Mitigation: Confirm ambiguous destructive requests by listing matching IDs first, and use the default group removal behavior that moves entries to Inbox unless deletion is explicitly requested. <br>
Risk: The skill depends on sqlite3 and will create or modify todo.db in the active workspace by default. <br>
Mitigation: Install sqlite3 before use and review the active working directory or TODO_DB override before running todo commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lstpsche/skills/todo-management) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Concise text confirmations, optional markdown todo lists, and bash command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses sqlite3 and stores todo data in a workspace-local todo.db by default; TODO_DB can override the database path.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

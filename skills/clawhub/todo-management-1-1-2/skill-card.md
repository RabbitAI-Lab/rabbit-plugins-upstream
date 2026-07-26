## Description: <br>
Per-workspace SQLite todo manager (./todo.db) with groups and task statuses (pending/in_progress/done/skipped), operated via {baseDir}/scripts/todo.sh for adding, listing, editing, moving, and removing entries and managing groups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucky-2968](https://clawhub.ai/user/lucky-2968) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to manage local workspace todos through a SQLite-backed CLI, including adding, listing, editing, moving, and removing entries and groups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates and mutates a local SQLite todo.db in each workspace. <br>
Mitigation: Install only when local workspace todo storage is intended, and avoid putting secrets or sensitive data in todo entries. <br>
Risk: Clear, remove, group remove, and --delete-entries commands can delete local todo data. <br>
Mitigation: Confirm destructive intent, use IDs for removals, and only pass --delete-entries when the user explicitly chooses deletion. <br>
Risk: Unused package files are present in the artifact. <br>
Mitigation: Do not run npm or pnpm install in the skill directory unless the publisher explains why those package files are needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lucky-2968/skills/todo-management-1-1-2) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Concise text confirmations and occasional Markdown tables, with bash commands executed through the bundled CLI script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires sqlite3 in PATH and stores todo data in a local todo.db file, or in TODO_DB when that environment variable is set.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

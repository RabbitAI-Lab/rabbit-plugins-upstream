## Description: <br>
Tasks Skill provides a SQLite-backed task manager for tracking tasks by status, description, and tags, with commands to add, list, filter, update, move, tag, and delete tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dvjn](https://clawhub.ai/user/dvjn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to maintain a local SQLite task list for personal tasks or project workflow tracking, including adding, listing, filtering, updating, moving, tagging, and deleting tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task titles, descriptions, and tags are stored in a local SQLite database on disk. <br>
Mitigation: Avoid storing secrets or sensitive data in tasks, and configure NO_NONSENSE_TASKS_DB to a protected path when needed. <br>
Risk: Update and delete commands modify the stored task list. <br>
Mitigation: Review task IDs and command arguments before running update, move, tag, or delete operations. <br>
Risk: The skill runs local shell scripts and requires sqlite3. <br>
Mitigation: Install sqlite3 from a trusted source and review the scripts before deployment in managed environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dvjn/skills/no-nonsense-tasks) <br>
- [Skill Usage Guide](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Development Guide](artifact/AGENT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text and Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local SQLite database at ~/.no-nonsense/tasks.db by default, configurable with NO_NONSENSE_TASKS_DB.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

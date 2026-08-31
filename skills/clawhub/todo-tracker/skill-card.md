## Description:

Persistent TODO scratch pad for tracking tasks across sessions. Use when the user asks to add, list, complete, remove, or summarize tasks in a portable workspace Markdown file. Uses stable task IDs and exact matching; heartbeat reporting is opt-in and count-only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to maintain a local Markdown TODO tracker across sessions, including adding, listing, completing, removing, and summarizing tasks. It is suited for portable workspace task tracking without a service or database.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill mutates the path selected by TODO_FILE and adjacent .bak, .lock, and .next-id files.

Mitigation: Choose TODO_FILE deliberately, quote the path, and keep the task file with its adjacent ID counter when moving or restoring the tracker.

Risk: Task removal is destructive.

Mitigation: Use the preview flow first, show the resolved stable ID and task text to the user, and remove only after explicit confirmation of the same ID.

Risk: Concurrent or interrupted writes can leave a lock or recoverable backup state.

Mitigation: Do not remove an active lock; investigate the writer and retry only after the lock is known to be stale, using the backup for recovery when needed.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown task-file updates, count-only text summaries, and inline bash command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes are local to TODO_FILE and adjacent backup, lock, and ID-counter files; heartbeat output is opt-in and count-only.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

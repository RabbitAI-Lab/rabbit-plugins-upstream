## Description:

memocap is a persistent memory skill for storing, recalling, forgetting, encapsulating, and visualizing agent memories across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to give an agent a local memory system that can proactively store preferences, tasks, decisions, emotions, time-related notes, and session context, then recall or visualize those records later.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill broadly and proactively stores persistent local memory about the user, including preferences, tasks, decisions, emotions, and context.

Mitigation: Install only when persistent memory is desired, review the local data directory before sensitive use, and confirm deletion or export behavior before storing sensitive records.

Risk: Stored memories may be recalled across sessions with limited scoping or consent controls.

Mitigation: Use explicit session boundaries, review recalled records before relying on them, and avoid using the skill for confidential sessions unless the storage location and retention expectations are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/memocap)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and local file path guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can direct an agent to read from, write to, export, delete, recover, and visualize records in a local memory directory.]

## Skill Version(s):

2.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

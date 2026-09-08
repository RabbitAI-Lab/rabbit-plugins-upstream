## Description:

智能办公本助手 lets an agent operate real Doxent notes, books, schedules, reminders, todos, and tasks through a local Doxent CLI when the user explicitly requests those workspace actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iflyink](https://clawhub.ai/user/iflyink)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their Doxent workspace so it can retrieve, organize, upload, and modify notes, books, schedules, reminders, todos, and tasks when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install, update, start, and persist a local Doxent CLI daemon and write user-level environment configuration.

Mitigation: Review the skill before installation, trust the Doxent CLI download source, and stop the daemon when the user explicitly no longer wants it running.

Risk: The skill can modify or delete real Doxent notes, folders, schedules, reminders, todos, and tasks.

Mitigation: Require explicit user confirmation for destructive or high-impact actions and verify target names, ids, and object types before writing.

Risk: The skill can upload or import files into the Doxent book workspace, including from local paths or remote URLs.

Mitigation: Confirm the source, destination, and file identity before upload or import, especially when content may be sensitive.

Risk: Workspace data may be stale if synchronization is incomplete or times out.

Mitigation: Wait for a successful sync before business data operations and stop the request instead of returning potentially stale data when sync does not complete.

## Reference(s):

- [open-model-note API](note/references/open-model-note-api.md)
- [open-model-book API](book/references/open-model-book-api.md)
- [open-model-schedule API](schedule/references/open-model-schedule-api.md)
- [Port and health rules](shared/port-and-health.md)
- [Write and sync rules](shared/write-and-sync.md)
- [Encoding rules](shared/encoding-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with structured status, result, source, and next-step sections; may include shell commands, JSON request bodies, and Doxent deep links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can trigger local API calls through the Doxent CLI and may reflect synchronized user workspace data.]

## Skill Version(s):

1.3.6 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

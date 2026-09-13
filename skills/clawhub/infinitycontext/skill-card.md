## Description:

Infinity Context helps agents keep long sessions searchable by archiving redacted conversation chunks in a local SQLite/FTS5 store, compacting working context, and retrieving exact past details on demand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pondsi](https://clawhub.ai/user/pondsi)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent users use this skill to keep long-running AI-agent sessions usable after context compaction while retaining searchable local access to earlier details. It is intended for agents that need offline recall, retention cleanup, and controlled redaction workflows for session history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local archive contains detailed session history and may remain sensitive even after best-effort redaction.

Mitigation: Treat archive files as sensitive data, keep them out of shared or synced folders, and use the documented retention cleanup or INFINITY_CONTEXT_NO_ARCHIVE=1 off switch when history should not be retained.

Risk: Maintenance behavior can permanently delete expired archive files or rewrite a file during in-place redaction.

Mitigation: Use the documented scope controls: destructive cleanup requires explicit confirmation, and in-place redaction requires an allowed directory with path resolution checks.

Risk: Extending retention beyond the bounded default increases exposure of past conversations.

Mitigation: Keep the default 30-day retention or choose a shorter configured window unless there is a clear need for longer retention.

## Reference(s):

- [ClawHub Release Page](https://clawhub.ai/pondsi/skills/infinitycontext)
- [Architecture](references/architecture.md)
- [Other Languages](references/languages.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead an agent to create, search, prune, or redact local archive files using the bundled Python scripts.]

## Skill Version(s):

1.8.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

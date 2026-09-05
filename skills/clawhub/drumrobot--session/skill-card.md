## Description:

Session manages Claude Code and Antigravity conversation histories, including lookup, listing, search, import, summarization, analysis, archiving, classification, cleanup, repair, rewind, migration, and URL generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to inspect, organize, repair, move, archive, summarize, and recover Claude Code or Antigravity session histories. It is most useful when session metadata, transcript files, or cross-agent handoffs need explicit management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad access to local Claude and Antigravity session stores.

Mitigation: Install only in environments where that access is acceptable, and inspect target project paths and session IDs before use.

Risk: Mutating topics can move, delete, truncate, or rewrite session histories.

Mitigation: Prefer documented dry-run or check-only modes, keep backups, and avoid running mutating operations on a live active session.

Risk: Import, sync, and RAG flows can send session-derived content that may contain secrets or private project context.

Mitigation: Review transcripts before export and confirm the destination memory, agent, or RAG receiver before dispatch.

Risk: Hook installation can persist session ID injection behavior in local settings.

Mitigation: Review hook registrations after installation and remove them when automatic session context injection is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/session)
- [Skill overview](artifact/SKILL.md)
- [Release changelog](artifact/CHANGELOG.md)
- [Session repair guide](artifact/repair.md)
- [Session archive guide](artifact/archive.md)
- [Session install guide](artifact/install.md)
- [Session search guide](artifact/search.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with command snippets, tables, file paths, and structured operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some topics may call local scripts or MCP tools and may modify session files, hooks, memory, or RAG destinations when the user selects mutating flows.]

## Skill Version(s):

0.9.0 (source: evidence release and CHANGELOG, released 2026-08-29; frontmatter metadata says 0.8.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

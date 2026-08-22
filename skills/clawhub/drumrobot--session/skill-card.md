## Description:

Session helps agents manage Claude Code session histories, including lookup, listing, search, summarization, analysis, archiving, classification, cleanup, migration, repair, renaming, and related memory workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect, recover, move, compress, archive, and summarize local Claude Code session records. It is also used to route selected session context into memory, RAG, or other agent workflows when the user explicitly wants that content reused.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and reuse Claude session transcripts, which may contain secrets or sensitive project context.

Mitigation: Review session content before import, sync, RAG indexing, or handoff to another agent, and avoid automatic transcript-derived indexing unless that reuse is intended.

Risk: Some workflows can rewrite, move, compress, archive, or remove session history.

Mitigation: Use dry-run, check-only, or backup paths before repair, compression, purge, move, archive, or destroy operations.

Risk: Hook installation can persist session ID injection behavior across future Claude Code sessions.

Mitigation: Review hook configuration before enabling it and prefer project-local MCP or hook settings over user-level settings when practical.

Risk: Session content can be routed to memory, RAG stores, or other agents.

Mitigation: Confirm the destination and scope before dispatching session content, especially when using import, classify with RAG, or analyze sync workflows.

## Reference(s):

- [ClawHub Session Skill](https://clawhub.ai/drumrobot/skills/session)
- [Session skill overview](artifact/SKILL.md)
- [Session repair guide](artifact/repair.md)
- [Session classify guide](artifact/classify.md)
- [Session import guide](artifact/import.md)
- [Session install guide](artifact/install.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and tabular summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May operate on local session JSONL files and may call MCP tools when those tools are available.]

## Skill Version(s):

0.8.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

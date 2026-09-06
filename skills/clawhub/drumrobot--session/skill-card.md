## Description:

Session helps agents manage Claude Code and Antigravity sessions, including lookup, listing, search, import, summarization, analysis, archiving, classification, cleanup, splitting, compression, context measurement, migration, moving, purging, renaming, repair, rewind, and URL generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to inspect, organize, recover, and move local Claude Code and Antigravity session history. It is also used to measure context usage, prepare session summaries, and route session data to configured analysis or memory workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access local Claude Code and Antigravity session stores that may contain private project data, secrets, or personal transcript content.

Mitigation: Review transcript destinations before use, avoid forwarding sensitive sessions to other agents or RAG stores, and limit use to workspaces where that access is acceptable.

Risk: Some topics can rewrite, move, archive, truncate, or permanently delete session history.

Mitigation: Prefer dry-run or preview modes when available, verify the target session ID and destination, and keep backups before destructive operations.

Risk: Hook-based features can persistently inject session context or context-usage data into future prompts.

Mitigation: Enable hooks only after reviewing the configured files and remove or disable them when persistent prompt injection is no longer needed.

Risk: MCP-backed compression, analysis, summarization, or memory workflows may send transcript content to configured tools or stores.

Mitigation: Pin and review MCP dependencies where possible, confirm configured endpoints and collections, and avoid syncing confidential transcript content without approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/session)
- [Session Skill Source](SKILL.md)
- [Changelog](CHANGELOG.md)
- [Context Measurement Guide](context.md)
- [Repair Guide](repair.md)
- [Rewind Guide](rewind.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with shell commands, configuration snippets, and file-operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run operations that read, rewrite, move, archive, or delete local session history depending on the selected topic.]

## Skill Version(s):

0.11.1 (source: server release metadata and changelog, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

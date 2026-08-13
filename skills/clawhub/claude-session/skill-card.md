## Description:

Claude Session helps Claude Code users find, inspect, summarize, archive, repair, move, compress, sanitize, and route local Claude session transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and Claude Code users use this skill to manage local Claude session history, recover or reorganize transcripts, and route selected session content into summaries or follow-on agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private Claude session transcripts under ~/.claude/projects.

Mitigation: Install and invoke it only in environments where transcript access is acceptable, and review selected sessions for sensitive content before summarizing, importing, analyzing, or sharing them.

Risk: Several topics can move, rewrite, archive, purge, split, compress, repair, or destroy session files.

Mitigation: Use dry-run or explicit confirmation where available, keep backups for important sessions, and verify the target session ID and project path before running mutating operations.

Risk: Import, analyze sync, classification with RAG, and summarization workflows can send transcript content or derived summaries to other agents, memories, or tools.

Mitigation: Confirm the destination and retention behavior before use, and redact secrets or sensitive personal information before external or persistent sharing.

Risk: The install and compression flows can modify hook or MCP configuration that persists across future Claude Code sessions.

Mitigation: Review settings changes before enabling them globally and remove persistent hooks or MCP entries when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/claude-session)
- [Skill overview](artifact/SKILL.md)
- [Install session ID hook](artifact/install.md)
- [Session import](artifact/import.md)
- [Session compression](artifact/compress.md)
- [Session repair](artifact/repair.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and occasional JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May move, rewrite, archive, purge, summarize, or share selected Claude session transcript content depending on the invoked topic.]

## Skill Version(s):

0.7.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

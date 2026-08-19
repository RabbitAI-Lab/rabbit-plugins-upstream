## Description:

Claude Session helps agents inspect, search, summarize, archive, repair, migrate, and otherwise manage local Claude Code session files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to manage Claude Code session transcripts, including finding session IDs, listing and searching sessions, summarizing prior work, repairing damaged JSONL chains, moving sessions between projects, and archiving or deleting sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify private local session files through repair, move, archive, clean, purge, and destroy workflows.

Mitigation: Review the exact target session and prefer dry runs or backups before allowing destructive or in-place operations.

Risk: Session-derived content can be routed into other agents, memory, or RAG stores.

Mitigation: Review archive, import, analyze, RAG, Serena memory, and agent-transfer behavior before use, especially when sessions may contain sensitive data.

Risk: The security verdict is suspicious because the skill has real session-management capabilities with access to local private transcripts.

Mitigation: Install only when the operator explicitly wants agent-managed session maintenance and accepts the local file access and routing behavior described by the security evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/claude-session)
- [Skill overview](artifact/SKILL.md)
- [Archive guide](artifact/archive.md)
- [Repair guide](artifact/repair.md)
- [Session import guide](artifact/import.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some workflows can lead the agent to read, move, modify, repair, archive, or delete local session JSONL files.]

## Skill Version(s):

0.8.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

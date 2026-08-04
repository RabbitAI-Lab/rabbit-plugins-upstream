## Description: <br>
Claude Session helps agents manage Claude Code session records, including lookup, listing, search, import, summarization, analysis, archive, classification, sanitization, splitting, compression, deletion, memory trimming, migration, movement, purge, rename, repair, and URL generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to inspect, organize, repair, move, archive, and summarize Claude Code session history. It is useful for session recovery, project migration, cleanup, knowledge extraction, and controlled sharing of session-derived content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, summarize, persist, or forward Claude session history, which may contain secrets or sensitive conversation content. <br>
Mitigation: Review target sessions before import, RAG storage, analyze --sync, summarization, or sharing, and avoid using these paths on sessions containing secrets unless downstream exposure is acceptable. <br>
Risk: Several operations can move, rewrite, archive, compress, repair, or delete session JSONL files. <br>
Mitigation: Prefer documented dry-run or check-only modes, confirm exact session IDs and destination paths, and keep or verify backups before applying destructive or irreversible changes. <br>
Risk: Hook installation and session ID injection can add session metadata to agent context. <br>
Mitigation: Enable hooks only when session tracking is desired and review hook behavior before using workflows that depend on injected session identifiers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/claude-session) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>
- [LICENSE](artifact/LICENSE) <br>
- [repair.md](artifact/repair.md) <br>
- [import.md](artifact/import.md) <br>
- [purge.md](artifact/purge.md) <br>
- [destroy.md](artifact/destroy.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, file paths, session identifiers, and optional script-driven file changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or invoke local scripts that read, move, rewrite, archive, delete, summarize, or forward Claude Code session JSONL files.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release metadata and CHANGELOG, released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

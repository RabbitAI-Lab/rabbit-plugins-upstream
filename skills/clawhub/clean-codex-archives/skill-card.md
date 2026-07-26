## Description: <br>
Safely inspects and removes locally archived Codex conversation data on Windows, macOS, and Linux, including archived rollout JSONL files, archived session rows and related logs in Codex SQLite databases, and stale session_index.jsonl entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lunarcache](https://clawhub.ai/user/lunarcache) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Codex users use this skill to inventory and, after explicit authorization, remove archived local Codex sessions, related SQLite metadata, logs, goals, and stale session index entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The cleanup deletes archived conversations and related local metadata when applied. <br>
Mitigation: Run the dry run first, review the reported counts, and use --apply only after explicit authorization. <br>
Risk: SQLite cleanup can fail or block when Codex databases are locked. <br>
Mitigation: Close Codex or the process holding the database before retrying, and use --vacuum only when compaction is explicitly desired. <br>
Risk: Malformed session_index.jsonl data could make index cleanup unsafe. <br>
Mitigation: The script refuses to rewrite malformed, blank, or missing-ID index entries instead of silently dropping them. <br>


## Reference(s): <br>
- [Clean Codex Archives on ClawHub](https://clawhub.ai/lunarcache/skills/clean-codex-archives) <br>
- [Publisher profile: lunarcache](https://clawhub.ai/user/lunarcache) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Cleanup script](artifact/scripts/clean_codex_archives.py) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, text] <br>
**Output Format:** [Markdown with inline shell commands and plain-text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled script defaults to dry-run output and requires --apply before deletion.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

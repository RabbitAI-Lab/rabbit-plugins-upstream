## Description: <br>
Claude Session helps agents manage Claude Code sessions, including session lookup, listing, search, summarization, analysis, archiving, classification, cleanup, migration, repair, renaming, splitting, compression, hook setup, and session URL generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to inspect, organize, summarize, repair, move, archive, and clean Claude Code session transcripts while keeping session IDs, project mappings, and related metadata manageable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session transcripts, IDs, and file paths may be forwarded to memory, RAG receivers, or other agents. <br>
Mitigation: Review and redact sensitive transcript content before import, archive RAG dispatch, or --sync memory writes; require explicit approval for any external handoff. <br>
Risk: Workflows can mutate, move, archive, or permanently delete Claude session files. <br>
Mitigation: Use dry-run or check-only modes where available, verify the exact target session, avoid operating on the active session, and confirm backups before destructive operations. <br>
Risk: The install workflow can register a persistent hook that injects session metadata into future prompts. <br>
Mitigation: Install the hook only when automatic session ID context is desired, review the generated settings entry, and remove the hook when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/claude-session) <br>
- [Session topic index](artifact/SKILL.md) <br>
- [Archive workflow](artifact/archive.md) <br>
- [Import workflow](artifact/import.md) <br>
- [Install hook workflow](artifact/install.md) <br>
- [Repair workflow](artifact/repair.md) <br>
- [Purge workflow](artifact/purge.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON snippets, and session-management instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute file operations against Claude session JSONL files, hooks, and memory or RAG handoffs when the user requests those workflows.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata and artifact CHANGELOG, released 2026-07-23; artifact frontmatter metadata.version is 0.1.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Session Memory helps agents save, recall, review, import, export, and manage persistent local memories across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[swaylq](https://clawhub.ai/user/swaylq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs lightweight local continuity: recording decisions or insights, loading recent and high-importance context at startup, searching prior notes, and maintaining memory backups. <br>

### Deployment Geography for Use: <br>
Runs in the user's local agent environment wherever bash and node are available. <br>

## Known Risks and Mitigations: <br>
Risk: Memories, exports, and backups are stored as local plaintext files and may contain sensitive context. <br>
Mitigation: Do not store API keys, passwords, tokens, or sensitive raw data; use vault references and handle exports as sensitive files. <br>
Risk: The security review reports script argument handling bugs that crafted inputs could abuse. <br>
Mitigation: Avoid allowing untrusted prompts, imported backups, or external content to choose script arguments until those issues are fixed. <br>
Risk: The published security verdict is suspicious, so deployment needs review before use. <br>
Mitigation: Review the scripts and storage behavior in the target environment before enabling the skill for routine agent memory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/swaylq/skills/session-memory) <br>
- [Publisher profile](https://clawhub.ai/user/swaylq) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text command output with optional JSON for recall, context, daily views, topics, consolidation, and stats.] <br>
**Output Parameters:** [Memory topic, content, tags, importance level, search query, date range, limit, topic filter, import path, export path, and AGENT_MEMORY_DIR.] <br>
**Other Properties Related to Output:** [Reads and writes JSONL memory entries in a local memory directory and supports import, export, archive, edit, delete, and summary workflows.] <br>

## Skill Version(s): <br>
2.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

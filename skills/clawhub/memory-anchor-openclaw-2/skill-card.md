## Description: <br>
Long-term memory for OpenClaw agents with SQLite hybrid recall, raw and curated anchors, session briefings, and optional embeddings for remembering and searching durable facts, preferences, and past conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g00siferdev-py](https://clawhub.ai/user/g00siferdev-py) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw agents use this skill to maintain durable memory across sessions, recall user preferences and past facts before answering, and store new long-lived facts from normal conversation. It is intended for agent-managed memory workflows where users want persistent recall without manually running memory commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain and index facts derived from normal conversation across sessions. <br>
Mitigation: Use it only where users explicitly want durable memory, define a clear retention policy, and provide a way to inspect, edit, or delete stored memories. <br>
Risk: Optional cloud embeddings can expose memory content to an external provider if enabled. <br>
Mitigation: Prefer the local database and local embedding provider by default; require explicit opt-in and secret handling review before configuring cloud embeddings. <br>
Risk: Broad agent-managed memory may influence future answers if stale or incorrect facts are stored. <br>
Mitigation: Have agents recall before relying on memories, avoid inventing memories, and periodically review or reindex stored anchors. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g00siferdev-py/skills/memory-anchor-openclaw-2) <br>
- [Server-resolved GitHub source](https://github.com/g00siferdev-py/Memory-Anchor-OpenClaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-capable CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing memory workflow guidance; CLI examples may read and write a local SQLite memory database and optionally use local or cloud embedding providers.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

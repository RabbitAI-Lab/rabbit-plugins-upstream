## Description: <br>
Persistent memory for AI agents to store facts, learn from actions, recall information, and track entities across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dennis-da-menace](https://clawhub.ai/user/dennis-da-menace) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to give AI agents local, cross-session memory for durable facts, lessons learned, and entity context. It is suited for workflows where agents need to recall prior preferences, project details, or operational lessons without relying on remote services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local persistent memory can retain sensitive, regulated, confidential, or stale information across agent sessions. <br>
Mitigation: Do not store secrets or regulated data unless an explicit policy allows it; use separate database paths for different users or projects and periodically inspect, export, or delete stored memory. <br>
Risk: Recalled facts or lessons may be outdated or inappropriate for the current task if memory is not maintained. <br>
Mitigation: Review recalled memories before acting on them, and use expiration, superseding, deletion, and stale-memory cleanup features to keep stored context current. <br>


## Reference(s): <br>
- [Agent Memory ClawHub listing](https://clawhub.ai/dennis-da-menace/skills/agent-memory) <br>
- [README](README.md) <br>
- [Skill usage guide](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with Python and shell command examples; runtime methods return Python objects, dictionaries, CLI text, and JSON export data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores facts, lessons, and entities in a local SQLite database, defaulting to ~/.agent-memory/memory.db unless a custom path is configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact src/__init__.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

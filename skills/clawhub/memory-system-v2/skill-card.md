## Description: <br>
Memory System V2 provides a fast, file-based memory system for AI agents with JSON indexing, auto-consolidation, and sub-20ms search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kellyclaudeai](https://clawhub.ai/user/kellyclaudeai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to give agents persistent local memory for learnings, decisions, insights, events, and interactions across sessions. It supports capturing notes, searching prior context, reviewing recent memories, viewing stats, and consolidating weekly summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive or confidential information may be retained in plaintext under $HOME/clawd/memory. <br>
Mitigation: Do not store secrets, credentials, regulated personal data, or confidential material; periodically review and delete old memories. <br>
Risk: Recalled memories may be stale, incomplete, or no longer authoritative. <br>
Mitigation: Treat recalled memories as context rather than current truth, and verify important details before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kellyclaudeai/skills/memory-system-v2) <br>
- [Memory System V2 design document](docs/memory-system-v2-design.md) <br>
- [Memory System V2 test results](docs/memory-system-v2-test-results.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with bash command examples and local JSON-backed memory files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash and jq; stores plaintext memory logs, indexes, and weekly summaries under $HOME/clawd/memory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

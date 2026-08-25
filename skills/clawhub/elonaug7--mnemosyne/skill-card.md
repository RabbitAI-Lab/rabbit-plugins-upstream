## Description:

Cognitive memory engine for AI agents that provides long-term local memory using compound-cue scoring, Markdown storage, and no embedding model, vector database, or LLM API dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elonaug7](https://clawhub.ai/user/elonaug7)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add persistent, local memory for cross-session recall of user facts, preferences, decisions, tasks, and conversation history. It is intended for OpenClaw or Hermes environments where memory should remain inspectable and stored locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory can store conversation history, profile facts, and user preferences across sessions.

Mitigation: Install only when an agent-wide memory layer is intended, and confirm where memory files are stored before use.

Risk: The skill changes agent behavior by requiring memory recall before replies.

Mitigation: Review the memory protocol and installer behavior before deployment, then verify that users can inspect, disable, delete, or back up stored memory.

Risk: The release security verdict is suspicious because user control guidance is incomplete.

Mitigation: Document operational controls for memory retention, review, deletion, and backup before using the skill with sensitive conversations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/elonaug7/skills/mnemosyne)
- [Architecture](references/architecture.md)
- [Benchmark Methodology](references/benchmark.md)
- [Hermes Adapter](references/hermes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing memory protocol guidance and local command usage; memory data is stored outside the skill output.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

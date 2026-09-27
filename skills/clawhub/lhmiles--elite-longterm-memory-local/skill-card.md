## Description:

Local vector memory system with LanceDB and pure JavaScript embeddings for storing, searching, and recalling agent memories without native modules or required external APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lhmiles](https://clawhub.ai/user/lhmiles)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to add local long-term memory to OpenClaw workflows, including storing user preferences, decisions, facts, and searching those memories for later context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored memories can be automatically injected into future prompts, which may carry stale, sensitive, or untrusted text into later agent work.

Mitigation: Disable autoRecall unless the stored memories are trusted, and review or delete memory entries before sensitive tasks.

Risk: Dormant Kimi and ONNX embedding adapters can make network calls despite the normal local-only posture.

Mitigation: Use the default pure JavaScript embedding path and avoid enabling the Kimi or ONNX adapters unless their network behavior has been reviewed and approved.

Risk: Initialization commands create or overwrite local memory files in the current workspace.

Mitigation: Back up existing SESSION-STATE.md, MEMORY.md, and memory/ data before running init commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lhmiles/skills/elite-longterm-memory-local)
- [Ollama](https://ollama.com)
- [LanceDB](https://lancedb.github.io)
- [nomic-embed-text Model](https://ollama.com/library/nomic-embed-text)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, CLI text output, OpenClaw tool responses, and JSON-compatible tool details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can create local memory files and a LanceDB-backed vector store in the current workspace.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

A memory capsule system for OpenCode agents that stores, retrieves, exports, and resurfaces conversation-derived memories with human-like recall behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenCode users use this skill to give an agent local long-term memory for preferences, tasks, decisions, context, time capsules, workflow memories, and recall-driven conversation support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically record, search, export, and reuse selected conversation content, preferences, decisions, tasks, emotions, and workflows.

Mitigation: Review before installing, avoid storing secrets or confidential data, and consider manual-only use instead of adding the global instructions file.

Risk: Local memory data, backups, temporary exports, and generated Desktop HTML files may retain sensitive conversation-derived information.

Mitigation: Regularly inspect and delete ~/.local/share/opencode/忆时, backups, /tmp exports, and generated Desktop HTML files when retention is not intended.

Risk: Automatic resurfacing of memories may introduce stale, private, or unwanted context into future agent responses.

Mitigation: Review recalled memories before acting on them and delete or correct records that should not influence future sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/memocap)
- [ChromaDB API reference](references/chroma-api.md)
- [bge-base-zh-v1.5 model download](https://hf-mirror.com/Xenova/bge-base-zh-v1.5/resolve/main/onnx/model.onnx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, CLI text output, JSON or timeline exports, and generated local HTML visualizations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local ChromaDB data, JSONL backups, exported memory files, and generated HTML reports.]

## Skill Version(s):

2.2.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

忆时 is an OpenCode memory-capsule skill that stores, retrieves, summarizes, exports, visualizes, and resurfaces personal conversation memory using local ChromaDB-backed storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenCode users and developers use this skill to add a persistent personal memory layer that can recall prior context, store preferences and decisions, manage time capsules, import or export memory files, and generate memory visualization or profile pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically store, recall, summarize, profile, and reuse prior conversation content.

Mitigation: Install it only for users who explicitly want persistent personal memory, avoid storing secrets or sensitive personal data, and prefer explicit storage and export commands.

Risk: Memory exports, backups, and generated profile or visualization pages may expose private context.

Mitigation: Review the data directory, backup files, exported Markdown or JSON, and generated HTML before sharing, publishing, or opening them outside a trusted local environment.

Risk: Automatic loading, archiving, and resurfacing can introduce stale or unexpected personal context into future sessions.

Mitigation: Disable or avoid auto-load and automatic archiving where possible, scope the data directory deliberately, and periodically inspect or prune stored memories.

Risk: Model setup may involve downloading model files from external mirrors.

Mitigation: Use trusted download sources, verify model file provenance where possible, and avoid running unreviewed downloaded artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/memocap)
- [ChromaDB API reference](references/chroma-api.md)
- [bge-base-zh-v1.5 ONNX model mirror](https://hf-mirror.com/Xenova/bge-base-zh-v1.5/resolve/main/onnx/model.onnx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, HTML files, JSON files]

**Output Format:** [Markdown guidance with shell commands, plus generated JSON, Markdown, and self-contained HTML artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local persistent memory data and can export or visualize stored conversation content.]

## Skill Version(s):

2.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

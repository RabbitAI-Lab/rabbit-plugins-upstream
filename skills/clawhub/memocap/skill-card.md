## Description:

memocap provides an OpenCode memory capsule system for storing, retrieving, archiving, exporting, and visualizing local conversation memories with semantic and keyword search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenCode users use memocap to add an always-on local memory layer that can recall prior context, store preferences and decisions, manage time capsules, and generate exports or visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local memory may store sensitive conversation content.

Mitigation: Avoid storing secrets or regulated personal data, review memory contents before sharing exports, and delete local memory data when it is no longer needed.

Risk: Auto-loaded memories may resurface stale, private, or irrelevant context in later conversations.

Mitigation: Review recalled memories before acting on them and disable auto-open, profile, or capsule behavior where possible.

Risk: Exports and visualization HTML files can expose stored memories outside the chat.

Mitigation: Generate files only in controlled locations, inspect them before opening or sharing, and remove backups or exports when they are no longer needed.

Risk: Stored workflows may be applied silently if treated as current task context.

Mitigation: Confirm stored workflows and proposed commands against the current request before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/memocap)
- [Chroma API reference](references/chroma-api.md)
- [bge-base-zh-v1.5 model download](https://hf-mirror.com/Xenova/bge-base-zh-v1.5/resolve/main/onnx/model.onnx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown responses with inline shell commands and optional local JSON, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write a local ChromaDB memory directory and generate backup, export, profile, or visualization files.]

## Skill Version(s):

2.3.3 (source: target metadata, release evidence, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

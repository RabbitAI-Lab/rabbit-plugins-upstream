## Description:

记忆胶囊系统 that gives an OpenCode agent persistent, human-like memory retrieval with automatic recall, association, storage, time capsules, import/export, and visualization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to add a persistent memory layer to an OpenCode agent, including recall of prior context, user preferences, decisions, emotional anchors, and scheduled time-capsule reminders. It also supports importing, exporting, visualizing, and profiling stored memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create a persistent automatic memory layer that records, retrieves, and resurfaces conversation data across sessions.

Mitigation: Enable it only when persistent memory is desired, review or disable auto-load and proactive storage behavior, and avoid using it for private, work, health, financial, or credential-related conversations unless the storage location and retention policy are acceptable.

Risk: Memory databases, JSONL backups, JSON or Markdown exports, /tmp files, and generated HTML pages may contain sensitive user data.

Mitigation: Treat all generated memory files as sensitive, keep them in access-controlled local paths, delete temporary exports when finished, and review outputs before sharing or opening them in other tools.

Risk: Visualization and profile workflows can generate browser-viewable HTML and may auto-open those files.

Mitigation: Use no-open options where available, inspect generated files before viewing or distributing them, and avoid generating profile pages from sensitive memories unless the user explicitly wants that output.

Risk: Model setup may download embedding model files from external mirror URLs.

Mitigation: Review the download source before installation, prefer vetted local model files in controlled environments, and restrict network downloads where policy requires.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/memocap)
- [ChromaDB API reference](references/chroma-api.md)
- [Xenova bge-base-zh-v1.5 ONNX model file](https://hf-mirror.com/Xenova/bge-base-zh-v1.5/resolve/main/onnx/model.onnx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown and terminal-oriented text with shell commands, configuration snippets, JSON exports, and generated HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include persistent local memory records, JSONL backups, JSON or Markdown exports, timeline files, and browser-viewable HTML visualizations.]

## Skill Version(s):

1.3.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

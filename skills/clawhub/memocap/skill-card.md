## Description:

忆时 is an OpenCode memory-capsule skill that adds local memory retrieval, automatic recall, active association, archiving, export, and visualization workflows for an agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this OpenCode skill to give an agent a local memory layer for storing, retrieving, summarizing, exporting, and visualizing conversation history, preferences, decisions, tasks, and workflow memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Always-on recall and storage can change normal agent behavior by surfacing or reusing conversation history without strong consent boundaries.

Mitigation: Enable the memory layer only after deciding that automatic recall and storage are acceptable, and prefer explicit confirmation before storing or reusing sensitive context.

Risk: Stored memories, backups, exports, and profile generation can expose secrets or sensitive personal data.

Mitigation: Avoid storing secrets or sensitive personal data, review local data and backup paths, and protect or remove exported files when they are no longer needed.

Risk: Deletion, recovery, export, and automatic archival operations can alter or reveal the local memory store.

Mitigation: Require explicit user confirmation before deletion, export, recovery, or automatic archival actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/memocap)
- [ChromaDB API reference](references/chroma-api.md)
- [bge-base-zh-v1.5 model file](https://hf-mirror.com/Xenova/bge-base-zh-v1.5/resolve/main/onnx/model.onnx)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML files, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with shell commands; memory exports may be Markdown, timeline Markdown, JSON, or standalone HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on local ChromaDB memory data and may include recalled memories, summaries, backups, exports, recovery guidance, and visualizations.]

## Skill Version(s):

2.3.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

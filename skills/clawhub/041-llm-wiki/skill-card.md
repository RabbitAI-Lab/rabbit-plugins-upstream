## Description:

Use when an AI Agent needs to operate an llm-wiki knowledge base by ingesting source files into Markdown wiki pages, answering from wiki pages and links, running maintenance tasks, preserving provenance and temporal metadata, or using Zotero as a literature-discovery layer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nemo4110](https://clawhub.ai/user/nemo4110)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to create and maintain a durable Markdown knowledge base from source materials, then query, link, lint, merge, index, and update that wiki through agent-guided workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Embedding providers such as OpenAI or MCP can receive wiki text and user queries when embedding features are enabled.

Mitigation: Keep embeddings disabled unless the provider and data-sharing posture are acceptable, and configure providers explicitly before indexing or semantic query.

Risk: Zotero full-text access and write-back workflows can expose local library content or alter local research metadata.

Mitigation: Treat Zotero read and write actions as explicit user-approved steps, prefer dry-run previews, and review outputs before applying changes.

Risk: The skill executes local Python and shell helper commands over user-provided files, PDFs, links, and wiki content.

Mitigation: Install and run it in an isolated environment, keep dependencies patched or locked, and review command output before accepting file changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nemo4110/skills/041-llm-wiki)
- [README](README.md)
- [File Handling](docs/FILE_HANDLING.md)
- [Zotero MCP Integration](docs/ZOTERO_MCP_INTEGRATION.md)
- [Karpathy llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [OpenAI Zotero skill](https://github.com/openai/plugins/tree/main/plugins/zotero/skills/zotero)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, file paths, configuration examples, and generated or updated wiki files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update Markdown wiki pages, logs, indexes, and configuration-backed retrieval artifacts when the user authorizes write operations.]

## Skill Version(s):

1.5.2 (source: SKILL.md frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

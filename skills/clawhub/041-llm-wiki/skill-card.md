## Description:

Helps agents operate an llm-wiki Markdown knowledge base by ingesting source files, answering from linked wiki pages, running maintenance commands, preserving provenance and temporal metadata, and coordinating Zotero-backed literature workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nemo4110](https://clawhub.ai/user/nemo4110)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and knowledge workers use this skill to have an agent build, query, and maintain a durable Markdown wiki from local source files and Zotero literature while preserving source provenance and temporal context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supply-chain exposure from GitHub-based installation and pipe-to-shell bootstrap commands.

Mitigation: Review the release before installing, prefer a pinned release or commit, install in an isolated environment, and avoid pipe-to-shell bootstrap commands when possible.

Risk: Credential and document-scope exposure when Zotero integration or remote embeddings are configured.

Mitigation: Configure Zotero and embedding providers only after reviewing what local documents, queries, API keys, and Zotero data the workflow can access or modify.

Risk: Generated wiki content can preserve incorrect or incomplete interpretations if source ingestion is not reviewed.

Mitigation: Use the skill's coverage, depth, lint, dry-run, and provenance checks before treating new or updated wiki pages as reliable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nemo4110/skills/041-llm-wiki)
- [Karpathy llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Zotero MCP integration](docs/ZOTERO_MCP_INTEGRATION.md)
- [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp)
- [Packaging and distribution decisions](docs/PACKAGING_DISTRIBUTION.md)
- [uv documentation](https://docs.astral.sh/uv/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to create or update wiki Markdown pages, logs, metadata, manifests, and optional Zotero workflow reports.]

## Skill Version(s):

1.5.3 (source: ClawHub release metadata; artifact frontmatter says 1.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

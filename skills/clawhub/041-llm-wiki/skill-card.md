## Description: <br>
llm-wiki helps an agent maintain a Markdown knowledge base by ingesting source files, answering wiki-backed questions, preserving provenance, and running status, lint, link, merge, query, and index workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nemo4110](https://clawhub.ai/user/nemo4110) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn local sources, notes, PDFs, and optional Zotero literature records into a durable Markdown wiki that supports later synthesis, search, linking, and maintenance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote embedding providers can receive page text and queries when embedding is enabled. <br>
Mitigation: Keep embeddings disabled for sensitive content unless the user intentionally accepts the configured provider and endpoint. <br>
Risk: MCP, SSE, and Zotero write-back integrations can affect external tools or literature libraries. <br>
Mitigation: Treat those integrations as trusted opt-in paths, verify capability gates, and review dry runs before applying merge or sync actions. <br>
Risk: The skill expects permission to read sources and write wiki, log, and cache files in the target repository. <br>
Mitigation: Install it only in repositories where those file operations are allowed, and keep generated summaries out of protected source directories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nemo4110/skills/041-llm-wiki) <br>
- [Karpathy llm-wiki note](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) <br>
- [OpenAI Plugins Zotero skill](https://github.com/openai/plugins/tree/main/plugins/zotero/skills/zotero) <br>
- [Zotero Literature Workflow Notes](docs/ZOTERO_MCP_INTEGRATION.md) <br>
- [Source File Handling](docs/FILE_HANDLING.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples and generated or updated Markdown wiki files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write wiki pages, logs, caches, and reviewed relation updates in the local workspace when the user authorizes wiki operations.] <br>

## Skill Version(s): <br>
1.5.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

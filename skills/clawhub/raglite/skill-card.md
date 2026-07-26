## Description: <br>
Local-first RAG cache: distill docs into structured Markdown, then index/query with Chroma (vector) + ripgrep (keyword). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virajsanghvi1](https://clawhub.ai/user/virajsanghvi1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use RAGLite to build a local, auditable retrieval cache for repeated lookups over private or local documents. It supports distilling documents to Markdown, indexing them with Chroma and ripgrep, and querying the resulting collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer retrieves the raglite-chromadb package from PyPI or a configured package index. <br>
Mitigation: Install only when the package source is trusted and review the configured package index before running the installer. <br>
Risk: Distilled Markdown, Chroma collections, and output directories may contain sensitive source document content. <br>
Mitigation: Index only intentional folders, avoid secrets or regulated records unless storage and access controls are understood, and delete generated artifacts when no longer needed. <br>
Risk: Source documents may contain prompt injection attempts or misleading instructions. <br>
Mitigation: Treat retrieved content as untrusted data and review important answers against the original sources before relying on them. <br>


## Reference(s): <br>
- [RAGLite ClawHub page](https://clawhub.ai/virajsanghvi1/skills/raglite) <br>
- [RAGLite repository listed in skill documentation](https://github.com/VirajSanghvi1/raglite) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown files, local Chroma collection data, and text query results produced through shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, pip, and rg; installs into a skill-local virtual environment and defaults to OpenClaw unless --engine is supplied.] <br>

## Skill Version(s): <br>
1.0.8 (source: SKILL.md frontmatter, manifest.json, openclaw.plugin.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

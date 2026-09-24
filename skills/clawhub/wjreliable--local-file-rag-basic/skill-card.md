## Description:

High-performance local File RAG suite (Basic Edition).

This skill is ready for commercial/non-commercial use.

## Publisher:

[wjreliable](https://clawhub.ai/user/wjreliable)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to search local workspaces for relevant code, documents, metadata, and focused snippets without reading every file directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can scan and index arbitrary user-supplied directories.

Mitigation: Run it only in constrained workspaces and avoid broad rootDir values such as home or system directories.

Risk: The local index may contain extracted file content.

Mitigation: Treat the .storage/code-rag.db file under the selected scan root as sensitive and remove it when the index is no longer needed.

Risk: The skill can silently install npm dependencies at runtime.

Mitigation: Install and audit dependencies before use instead of relying on automatic runtime installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wjreliable/skills/local-file-rag-basic)
- [README](artifact/README.md)
- [CHANGELOG](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Plain text with Markdown-like file sections, metadata blocks, line-numbered skeletons, and focused snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns up to five matched files, or one file when targetFile is provided; indexes supported files under 20MB.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

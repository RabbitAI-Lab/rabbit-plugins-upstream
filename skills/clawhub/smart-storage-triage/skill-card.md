## Description:

Universal smart search and storage triage for codebases, local files, documents, and archives. Uses SQLite FTS5 (BM25) and fast gzip tree snapshots. Requires user confirmation before broad directory indexing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synthet1x](https://clawhub.ai/user/synthet1x)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to create local searchable indexes for selected codebases, document folders, and storage trees, then retrieve concise file paths or snippets without broad shell walks. It is intended for confirmed local directories where the user wants faster content and archive search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing a broad local directory can collect more file content or path metadata than intended.

Mitigation: Confirm the exact target path and expected scope before indexing, avoid broad personal or shared drives unless needed, and use broad-scope indexing only after explicit approval.

Risk: Generated local index files can retain searchable snippets, paths, and file metadata after the original task is complete.

Mitigation: Periodically remove generated storage_rag.db and tree.json.gz files when they are no longer needed.

Risk: Sensitive non-secret business or personal documents may still be indexed if they are inside an approved target directory.

Mitigation: Choose the narrowest practical directory, review the target before indexing, and rely on the documented secret and credential exclusions as safeguards rather than as a substitute for scope control.

## Reference(s):

- [Artifact README](artifact/README.md)
- [Artifact Skill Definition](artifact/SKILL.md)
- [ClawHub Skill Page](https://clawhub.ai/synthet1x/skills/smart-storage-triage)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and plain-text search results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local SQLite FTS5 and gzip tree snapshot files for directories the user confirms.]

## Skill Version(s):

1.2.3 (source: server release metadata and artifact title)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Universal smart search and storage triage for codebases, local files, documents, and archives. Uses SQLite FTS5 (BM25) and fast gzip tree snapshots. Requires user confirmation before broad directory indexing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synthet1x](https://clawhub.ai/user/synthet1x)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to index selected local folders, codebases, documents, and archives, then retrieve targeted snippets or paths without broad shell walks. It supports local storage triage by separating active full-text search from lightweight archive tree search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing a broad or unintended folder can expose more local file paths and snippets than the user intended.

Mitigation: Confirm the exact target directory and expected scope before indexing, and avoid broad drives unless the user explicitly authorizes that scope.

Risk: Generated SQLite index and tree snapshot files can contain searchable excerpts and file paths from local data.

Mitigation: Treat generated index files as sensitive local artifacts, store them only where appropriate, and remove or protect them when no longer needed.

Risk: Search results may be incomplete when files are intentionally excluded by secret filters, archive triage, or active-age settings.

Mitigation: Tell users when scope controls may affect results and adjust flags such as full indexing or active-day windows only with clear user intent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/synthet1x/skills/smart-storage-triage)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and local search or indexing results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include file paths, line numbers, page or sheet numbers, snippets, and directory snapshot matches.]

## Skill Version(s):

1.3.0 (source: server release metadata and SKILL.md heading)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Smart Files provides content-aware workspace file management, including content search with opt-in snippets, duplicate detection, read-only organization and cleanup analysis, file metadata inspection, dry-run rename, and watch-mode journaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jlacroix82](https://clawhub.ai/user/jlacroix82)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Smart Files to inspect workspace contents, search file text, find duplicates, understand file metadata, and preview organization or cleanup actions before enabling any forced mutation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recursive file reading and optional snippets can expose sensitive workspace content in terminal output or agent context.

Mitigation: Keep snippets disabled by default, scan only intended workspaces, and avoid running searches over directories that contain secrets unless raw matches may be shown.

Risk: Watch mode records file paths, hashes, sizes, timestamps, and change events to a persistent journal.

Mitigation: Use one-shot commands when no disk writes are acceptable, restrict watched paths, and clear memory/smart-files-journal.json when the journal is no longer needed.

Risk: --force and workspace environment overrides can expand scans beyond the current workspace and may affect sensitive external paths.

Mitigation: Avoid --force and SMART_FILES_WORKSPACE overrides on sensitive directories unless external scanning is intentional and reviewed.

Risk: Mutation and watch behavior may not fully match the documentation according to the security guidance.

Mitigation: Verify behavior in a disposable workspace before relying on rename, organize, or watch mode for operational file changes.

## Reference(s):

- [ClawHub smart-files release page](https://clawhub.ai/jlacroix82/skills/smart-files)
- [README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search snippets are hidden unless --snippets is used; watch mode persists file metadata journal entries.]

## Skill Version(s):

2.2.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

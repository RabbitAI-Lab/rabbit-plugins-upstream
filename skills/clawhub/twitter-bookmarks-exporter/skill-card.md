## Description:

Exports all X/Twitter bookmarks into individual Markdown files with metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to convert manually captured X/Twitter bookmark API responses into local Markdown files for note-taking systems such as Obsidian or Notion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The user-supplied bookmarks.json and generated Markdown files can contain private bookmark data.

Mitigation: Treat bookmarks.json and output/bookmarks/ as private local data and review where those files are stored, shared, or synced.

Risk: Very large bookmark collections can create many local files.

Mitigation: Confirm the output location before running and review available disk space for large exports.

Risk: The export depends on manually captured X/Twitter bookmark responses.

Mitigation: Verify bookmarks.json contains the raw bookmark API responses before running the exporter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/twitter-bookmarks-exporter)
- [X/Twitter bookmarks page](https://x.com/i/bookmarks)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown files with YAML frontmatter plus a text completion summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes one local Markdown file per bookmark under output/bookmarks/.]

## Skill Version(s):

1.0.0 (source: server release metadata, released 2026-08-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

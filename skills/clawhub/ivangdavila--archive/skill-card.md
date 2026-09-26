## Description:

Capture and preserve content as intelligent snapshots with semantic search, automatic extraction, and proactive resurfacing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to save user-selected articles, files, notes, videos, and other content as local markdown snapshots, then search and resurface those saved items by topic, project, source, author, or time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store full extracted text, source URLs, local file paths, search history, tags, project names, and resurfacing preferences in a persistent local archive.

Mitigation: Archive only material the user is comfortable retaining locally, and avoid saving sensitive content unless that persistent local record is acceptable.

Risk: Proactive resurfacing may expose saved content at an unexpected time if preferences are too broad.

Mitigation: Honor user opt-out or search-only preferences and keep resurfacing limited to genuinely relevant items.

## Reference(s):

- [Capture Patterns](artifact/capture.md)
- [Archive Memory Template](artifact/memory-template.md)
- [Resurfacing Rules](artifact/resurface.md)
- [Search Patterns](artifact/search.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and local file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local archive files under ~/archive when the user asks to archive content.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

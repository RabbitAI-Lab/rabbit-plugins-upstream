## Description:

Scan a directory of Markdown files, extract titles/headings/frontmatter, build a searchable index JSON, and output a concise summary report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, documentation maintainers, and knowledge-base operators use this skill to inventory Markdown folders, generate searchable JSON metadata, and produce a concise catalog of document titles, headings, line counts, and frontmatter presence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated index can expose private file paths, document titles, line counts, and related metadata if shared or uploaded.

Mitigation: Review index.json and catalog.md before sharing them, and run the indexing commands only on folders intended for cataloging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/markdown-indexer)
- [Publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [Shell commands, Code, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands that produce JSON and optional Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces index.json and, optionally, catalog.md from local UTF-8 Markdown files; requires jq.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

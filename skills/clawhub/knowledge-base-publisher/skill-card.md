## Description:

Organize, format, and publish knowledge-base articles and documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, documentation maintainers, and support teams use this skill to convert raw notes, transcripts, and scattered Markdown or text files into structured, publication-ready knowledge-base entries with metadata, cross-references, and version tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated knowledge-base content may include inaccurate summaries, tags, links, or metadata if source material is incomplete or ambiguous.

Mitigation: Review generated articles, index.json, CHANGELOG.md, and metadata before publishing.

Risk: Using a production output directory directly could commingle draft files with approved documentation.

Mitigation: Write to a dedicated staging directory first, then publish only reviewed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/knowledge-base-publisher)
- [Publisher profile](https://clawhub.ai/user/terrycarter1985)
- [Getting Started with Knowledge Base Publisher](examples/getting-started.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, configuration, guidance]

**Output Format:** [Structured Markdown files with JSON catalogs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces organized article files, an index.json catalog, per-article meta.json files, a taxonomy file when used, and a CHANGELOG.md for version history.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

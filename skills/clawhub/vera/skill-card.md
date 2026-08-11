## Description:

Search PDFs and local document libraries with vera-cli to retrieve citation-ready context for AI agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dkylewillis](https://clawhub.ai/user/dkylewillis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search local PDF or document archives, inspect VERA archive metadata, retrieve figure and region context, and produce source-cited answers from local documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversion, indexing, overwrite, update, and export commands write local files.

Mitigation: Require explicit user authorization before running write operations and limit them to intended folders and documents.

Risk: Retrieved result rank or score may not prove that a passage supports the answer.

Mitigation: Read returned text, headings, and page metadata before citing evidence, and rerun targeted searches when support is incomplete.

Risk: Figure retrieval returns captions and metadata, not visual image inspection.

Mitigation: State when answers are based on figure metadata only and use a separate vision-capable tool before making visual claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dkylewillis/skills/vera)
- [VERA CLI reference for agents](references/cli-reference.md)
- [VERA retrieval workflows](references/retrieval-workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and JSON interpretation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should include document-backed citations with source filename, page or page range, and heading when available.]

## Skill Version(s):

0.1.1 (source: release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

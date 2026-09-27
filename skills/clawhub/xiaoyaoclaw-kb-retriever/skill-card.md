## Description:

Retrieves and answers questions from a specified local knowledge base of text, PDF, and spreadsheet files using hierarchical indexes and source-aware search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

People and teams with a local knowledge base use this skill to find and answer questions about their documents with source references. On request, they can also build indexes or extract PDF content for searching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A search helper may follow symlinks and read files outside the selected knowledge-base directory.

Mitigation: Use a trusted knowledge-base folder and remove symlinked files before searching.

Risk: Optional maintenance writes files and optional package installation changes the Python environment.

Mitigation: Review the proposed changes and obtain user confirmation before writing files or installing packages.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-kb-retriever)
- [PDF reading guide](references/pdf_reading.md)
- [Excel reading guide](references/excel_reading.md)
- [Excel analysis guide](references/excel_analysis.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown answers with source references and optional maintenance instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional confirmed maintenance produces knowledge-base indexes, extracted PDF text, or page images.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata and artifact manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

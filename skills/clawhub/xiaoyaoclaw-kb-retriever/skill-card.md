## Description:

Retrieves and answers questions from a local knowledge base of text, PDF, and Excel files using hierarchical indexes and focused searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

People using OpenClaw to search a specified local knowledge-base directory and get answers with file references; they can also request and confirm index generation or PDF conversion when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read operations may follow symlinked files outside the selected knowledge-base directory.

Mitigation: Use trusted knowledge-base directories and inspect symlinked files in imported or shared archives before retrieval.

Risk: Optional index generation and PDF conversion write files that may contain sensitive source content.

Mitigation: Confirm each write and its destination; store derived files only in approved locations and handle them as sensitive data.

Risk: Optional PDF or Excel support can require installing additional packages.

Mitigation: Review and approve the packages and environment changes before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-kb-retriever)
- [PDF reading guide](references/pdf_reading.md)
- [Excel reading guide](references/excel_reading.md)
- [Excel analysis guide](references/excel_analysis.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Markdown answers with file references; optional local index, extracted text, or page images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieval is read-only; optional file writes require an explicit request and confirmation.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

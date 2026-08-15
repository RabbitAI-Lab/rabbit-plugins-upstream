## Description:

Converts Markdown files or pasted Markdown text into academically formatted Word (.docx) documents with support for headings, body text, images, tables, code blocks, lists, and LaTeX math.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trisia](https://clawhub.ai/user/trisia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, students, and technical writers use this skill to convert Markdown content into formatted DOCX documents for academic papers, technical reports, theses, and similar structured documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted Markdown can trigger automatic outbound image downloads.

Mitigation: Review Markdown image URLs before conversion or disable remote image fetching when processing untrusted content.

Risk: The setup workflow creates a persistent cache virtual environment and installs Python packages.

Mitigation: Approve dependency installation before first use and run the skill in an environment where the persistent cache location is acceptable.

Risk: The converter reads Markdown inputs and writes DOCX files to the selected output location.

Mitigation: Use intended input files and explicit output paths when converting sensitive or untrusted documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/trisia/skills/mddoc)
- [Sample Markdown evaluation](artifact/evals/test-sample.md)
- [LaTeX coverage evaluation](artifact/evals/test-latex-coverage.md)

## Skill Output:

**Output Type(s):** [files, shell commands, configuration, guidance]

**Output Format:** [DOCX files with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or reuse a persistent Python virtual environment and may fetch image URLs embedded in Markdown.]

## Skill Version(s):

0.1.8 (source: server release evidence; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

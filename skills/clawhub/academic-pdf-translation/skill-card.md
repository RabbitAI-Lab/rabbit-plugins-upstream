## Description:

Translates academic PDF papers into readable, searchable target-language PDFs while preserving document structure, layout, and research meaning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ezra-y](https://clawhub.ai/user/ezra-y)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, and developers use this skill to translate one or more research-paper PDFs into readable, searchable PDFs with selectable review depth and final output paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow copies source PDFs into a local Workspace and keeps hidden processing files until the user deletes them.

Mitigation: Use only documents you have permission to process, choose an appropriate local workspace for sensitive files, and delete local input, process, and output files when no longer needed.

Risk: The skill runs PDF and image parsing libraries on user-provided documents, including potentially untrusted PDFs.

Mitigation: Use an isolated environment for untrusted PDFs and keep dependencies within the release-specified version ranges.

Risk: The generated translation may be unsuitable for publication, assessment, legal, medical, or other high-stakes reliance without review.

Mitigation: Review the final translation before relying on it, and treat it as a reading and review aid rather than an official or legally authoritative translation.

## Reference(s):

- [README_EN.md](README_EN.md)
- [Quality Contract](references/quality-contract.md)
- [Workspace and Output Specification](references/workspace.md)
- [Translation Scope](references/translation-scope.md)
- [Validation Scope](references/validation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON batch data, and generated searchable PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local Workspace input, output, and hidden processing directories; final translations are written as PDF files.]

## Skill Version(s):

1.2.1 (source: pyproject.toml, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

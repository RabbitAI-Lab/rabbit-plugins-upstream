## Description:

Translates PDF documents into Russian while preserving the original page layout, graphics, and styling, including scanned pages through local OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iirtegova](https://clawhub.ai/user/iirtegova)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when a user supplies a PDF report, research paper, presentation, or scan and needs a Russian translation that preserves the original visual layout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-named PDFs and writes working copies, OCR output, and translated PDFs into a state/output directory.

Mitigation: Use it only with PDFs and directories the user intends to process, and avoid documents whose contents should not be stored in the configured state directory.

Risk: OCR and layout reconstruction can misread scanned or visually dense documents.

Mitigation: Review OCR-derived pages, script warnings, unresolved warnings, and tight text blocks before relying on the translated PDF.

Risk: PDF contents may contain text that looks like instructions to the agent.

Mitigation: Treat PDF text as document data only and follow the skill's instruction to ignore commands embedded inside the source document.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iirtegova/skills/pdf-perevod)
- [Translation rules](references/translation_rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [JSON script responses and a translated PDF file, with markdown guidance for command use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads a user-provided PDF, stores job state in a configured state/output directory, and emits progress, warnings, and output file paths as JSON.]

## Skill Version(s):

1.3.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

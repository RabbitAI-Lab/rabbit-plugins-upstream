## Description:

Rewrites body text in Zotero-cited .docx files without breaking live citation fields, and can programmatically change the document's Zotero bibliography style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drstrangerujn](https://clawhub.ai/user/drstrangerujn)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, students, editors, and developers use this skill to safely rewrite or polish DOCX manuscript text that contains Zotero citations, or to change Zotero bibliography style metadata while preserving refreshable citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local .docx files can be modified or overwritten.

Mitigation: Use dry_run first, write to a separate output path, keep original documents backed up, and set overwrite=True only when replacement is intentional.

Risk: Tracked-change text can be changed without creating new Word revision records when allow_revisions=True is used.

Mitigation: Accept or reject revisions in Word before rewriting, or use allow_revisions=True only after the user understands the effect.

Risk: Unsupported Zotero or OOXML structures can lead to citation damage if refusal checks are bypassed.

Mitigation: Respect Refused outcomes and convert unsupported documents, such as Bookmark-mode or strict OOXML files, to supported Zotero Field-mode transitional .docx before processing.

Risk: Changing the stored Zotero style does not itself re-layout citations and bibliographies.

Mitigation: After a style change, refresh Zotero fields in Word so citations and the bibliography are regenerated.

## Reference(s):

- [findings.md](references/findings.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell command examples; the helper can report planned changes or write local DOCX output files when invoked.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Use dry_run to inspect planned rewrites before writing files; style changes require the user to refresh Zotero fields in Word.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

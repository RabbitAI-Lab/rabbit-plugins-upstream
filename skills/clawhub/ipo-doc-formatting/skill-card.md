## Description:

Applies IPO prospectus and exchange feedback-reply formatting conventions to Word documents, including document-type detection, template-based style mapping, title numbering, three-line tables, and validation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kianchales](https://clawhub.ai/user/kianchales)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and document-preparation agents use this skill to format Chinese A-share IPO prospectus sections, formal reports, due-diligence memoranda, and exchange feedback replies without changing the document text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic triggers may apply formatting to important Word documents more broadly than intended.

Mitigation: Review the target document and selected style family before running, and prefer saving formatted output to a new file.

Risk: In-place edits or template customization can affect existing or future formatted documents.

Mitigation: Make backups before local edits and copy templates before customizing them.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/Kianchales/ipo-doc-formatting)
- [ClawHub skill page](https://clawhub.ai/kianchales/skills/ipo-doc-formatting)
- [Style Map](artifact/references/style-map.md)
- [IPO Document Numbering and Table Rules](artifact/references/rules.md)
- [Usage Examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [DOCX files, Markdown fallback text, validation summaries, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on formatting and validation; source text should remain unchanged.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

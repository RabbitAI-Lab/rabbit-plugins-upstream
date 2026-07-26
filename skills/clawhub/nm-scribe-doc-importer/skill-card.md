## Description: <br>
Converts external documents (PDF, DOCX, PPTX, XLSX, HTML) into editable markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation authors use this skill to turn user-provided PDFs, DOCX files, slide decks, spreadsheets, or HTML documents into editable markdown for project documentation, rewriting, remediation, or integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A user-provided document or URL may contain untrusted content that should not be treated as agent instructions. <br>
Mitigation: Confirm the source document or URL before conversion, sanitize imported content, strip instruction-like tags, and wrap external content in boundary markers. <br>
Risk: Writing converted markdown to an unintended path could overwrite or place generated content in an important project directory. <br>
Mitigation: Confirm the output path before writing, especially when converting files in important project directories. <br>
Risk: Conversion can produce garbled sections, broken tables, or other artifacts that may misrepresent the source document. <br>
Mitigation: Normalize headings and tables, preserve substantive content, and mark unclear sections with review comments for human follow-up. <br>


## Reference(s): <br>
- [ClawHub listing: Nm Scribe Doc Importer](https://clawhub.ai/athola/skills/nm-scribe-doc-importer) <br>
- [Publisher profile: athola](https://clawhub.ai/user/athola) <br>
- [Metadata homepage: claude-night-market scribe plugin](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown draft plus concise conversion guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes converted markdown to a user-confirmed target path and marks unclear conversion artifacts for review.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description:

Converts external documents (PDF, DOCX, PPTX, XLSX, HTML) into editable markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and documentation authors use this skill to convert local or remote PDF, DOCX, PPTX, XLSX, and HTML documents into editable markdown for project documentation, rewriting, remediation, or integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad document import or conversion requests and write a converted markdown file.

Mitigation: Use it only when document-to-markdown conversion is intended, confirm source accessibility, and review the target output path before allowing the agent to write.

Risk: Converted external content can contain misleading instructions, large sections, or conversion artifacts.

Mitigation: Apply content sanitization, truncate oversized sections as directed by the artifact workflow, preserve substantive content, and mark unclear sections for review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-doc-importer)
- [Publisher profile](https://clawhub.ai/user/athola)
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, guidance]

**Output Format:** [Markdown draft files with concise guidance and optional review markers for unclear conversion artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a converted markdown draft to a user-approved target path; image extraction may require separate handling.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

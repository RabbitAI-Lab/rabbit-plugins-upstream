## Description:

Rebuilds Omni-parsed content or agent-authored Markdown as structured Word, HTML, PDF, and PowerPoint deliverables with page anchors, tables of contents, source references, and scenario-based formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document professionals use this skill to turn Omni Reader parsed material or agent-authored Markdown into structured Word, HTML, print-ready PDF, or presentation files, including source-page markers and provenance notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The discard-text option may leave confidential text in shared presentation notes.

Mitigation: Inspect generated presentation notes and remove sensitive text before sharing.

Risk: Remote image links may make offline documents incomplete.

Mitigation: Remove remote image links when preparing offline documents.

Risk: Sensitive files require an appropriately approved Omni parsing service.

Mitigation: Use an approved Omni parsing service for sensitive files.

Risk: Unreviewed dependencies may introduce software risk.

Mitigation: Install reviewed dependency versions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huhoo/skills/cue-omni2docx)
- [Publisher profile](https://clawhub.ai/user/huhoo)

## Skill Output:

**Output Type(s):** [Word documents, HTML documents, PDFs, PowerPoint presentations]

**Output Format:** [.docx, .html, .pdf, and .pptx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Omni-parsed workflows require a connected omni-reader MCP; PDF and PPTX outputs have additional local dependencies. Presentation prose may appear in speaker notes.]

## Skill Version(s):

0.6.13 (source: server-resolved release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

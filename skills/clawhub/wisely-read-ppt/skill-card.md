## Description: <br>
Converts PPTX and PDF files into page-by-page Word analysis documents with full-page screenshots, editable text organization, and inline image descriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sedey999](https://clawhub.ai/user/sedey999) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and business users use this skill to turn complex presentation or PDF content into structured, reviewable Word documents. It is intended for slide decks, reports, financial materials, and other documents where text extraction must be paired with visual page review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local document-conversion commands and install Python dependencies. <br>
Mitigation: Use an isolated environment, preinstall dependencies yourself, and run with --no-install where practical. <br>
Risk: LibreOffice, poppler, and related tooling may require local installation or persistent environment changes. <br>
Mitigation: Review installation steps before use and prefer already-managed system packages or sandboxed tooling. <br>
Risk: Extracted screenshots, images, text JSON, and draft documents may retain sensitive PPT/PDF content in working folders. <br>
Mitigation: Delete ppt-parse-working and extracted assets when audit artifacts are no longer needed. <br>


## Reference(s): <br>
- [macOS LibreOffice installation guide](reference/macos-install.md) <br>
- [Subagent workflow guide](reference/subagent-workflow.md) <br>
- [LibreOffice downloads](https://www.libreoffice.org/download/) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [DOCX files with embedded screenshots, extracted asset files, JSON metadata, and Markdown-style task reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local PPTX or PDF inputs and an image-capable model for visual review; working folders may retain extracted document content.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

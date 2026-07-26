## Description: <br>
Converts PPTX and PDF files into page-by-page structured DOCX parsing documents with full-page screenshots, editable text organization, and inline image descriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sedey999](https://clawhub.ai/user/sedey999) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
Developers, analysts, and document-review agents use this skill to transform complex PPTX or PDF presentations into reviewable Word documents with extracted text, screenshots, and structured descriptions of embedded visuals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The runtime dependency installer can silently modify the Python environment. <br>
Mitigation: Run the skill in an isolated virtual environment or container, preinstall dependencies, and use the --no-install option. <br>
Risk: Input decks and PDFs may be retained as screenshots, extracted images, text JSON, and working DOCX files in the workspace. <br>
Mitigation: Avoid highly sensitive documents unless retention is acceptable, and manually remove ppt-parse-working, retained assets, and intermediate outputs when processing is complete. <br>
Risk: The generated parsing document can contain missed text, incorrect ordering, or incomplete image transcription if visual review is skipped. <br>
Mitigation: Complete the documented full-page visual review and main-agent final review before delivering the final DOCX. <br>


## Reference(s): <br>
- [Wisely Read PPT ClawHub Skill Page](https://clawhub.ai/sedey999/skills/wisely-read-ppt) <br>
- [README.md](artifact/README.md) <br>
- [subagent-workflow.md](artifact/reference/subagent-workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Shell commands, Guidance] <br>
**Output Format:** [DOCX document with page screenshots, structured text, inline image markers, and retained PNG/JSON asset files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a vision-capable model for page review; PPTX rendering requires LibreOffice, and PDF rendering requires poppler or PyMuPDF.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

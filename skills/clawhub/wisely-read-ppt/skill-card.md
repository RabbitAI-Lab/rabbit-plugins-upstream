## Description: <br>
Parses PPTX and PDF files into page-by-page structured Word documents with full-page screenshots, editable text, and inline image descriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sedey999](https://clawhub.ai/user/sedey999) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
Developers, analysts, and external users use this skill to convert complex slide decks or PDFs into reviewable DOCX analysis drafts. It is intended for workflows that need page-by-page visual checking, text reordering, image annotation, and final human or agent review before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run shell commands, create working and output directories, spawn subagents for larger jobs, and install LibreOffice, poppler, or Python packages during normal use. <br>
Mitigation: Run it in a virtual environment or container, prefer the script's no-install option where possible, and approve any operating system package installation explicitly. <br>
Risk: PPT and PDF parsing can produce incomplete or misleading output if visual verification or final review is skipped. <br>
Mitigation: Require page-by-page visual checking and a final review pass before using or delivering the generated DOCX file. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sedey999/skills/wisely-read-ppt) <br>
- [README](artifact/README.md) <br>
- [Subagent workflow reference](artifact/reference/subagent-workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [DOCX files with extracted assets and Markdown-style page annotations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates working and final output directories; requires an image-capable model for visual verification.] <br>

## Skill Version(s): <br>
1.3.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description:

Parses PowerPoint presentations and PDF files into structured, page-by-page Word documents containing screenshots, editable text, and descriptions of embedded images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can convert PPTX presentations or PDFs into editable, page-by-page Word documents for reviewing and working with slide content, including text and visual references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic dependency setup may change or bypass protections in the Python environment.

Mitigation: Review dependency installation steps before running the skill, and use an isolated Python environment where practical.

Risk: Installation guidance includes elevated or system-wide changes, and the security scan reports incomplete evidence.

Mitigation: Review installation commands and referenced files before execution; avoid elevated or system-wide changes unless they are necessary and understood.

## Reference(s):

- [Wisely Read PPT on ClawHub](https://clawhub.ai/sedey999/skills/wisely-read-ppt)
- [macOS LibreOffice installation guide](reference/macos-install.md)
- [PPT/PDF subagent workflow guide](reference/subagent-workflow.md)

## Skill Output:

**Output Type(s):** [Files, Text, Images]

**Output Format:** [DOCX (.docx) page-by-page documents with editable text and embedded page screenshots; a paired image-free DOCX is also produced.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each page contains organized text and image descriptions; embedded visuals can be retained in the full version or removed in the paired image-free version.]

## Skill Version(s):

1.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

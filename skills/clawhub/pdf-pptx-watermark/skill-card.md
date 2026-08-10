## Description: <br>
PPTX-to-PDF watermark tool with real-time mobile parameter tuning for converting PPT/PPTX or existing PDF files into custom watermarked PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avocadoleaf-highfive](https://clawhub.ai/user/avocadoleaf-highfive) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, employees, and document owners use this skill to convert presentation files to PDFs and apply diagonal, grid, or centered watermarks before sharing internal materials, client deliverables, or controlled documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document conversion and PDF parsing can expose the local environment to malformed or untrusted files. <br>
Mitigation: Process only files the user intentionally selects, keep LibreOffice and Python dependencies updated, and sandbox untrusted presentations or PDFs. <br>
Risk: The packaged files do not clearly document the advertised phone and QR tuning workflow. <br>
Mitigation: Treat mobile tuning as optional and validate generated JSON configuration before relying on it for production documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/avocadoleaf-highfive/skills/pdf-pptx-watermark) <br>
- [Project homepage](https://github.com/AvocadoLeaf-Highfive/pdf-pptx-watermark) <br>
- [Mobile parameter tuning](https://github.com/AvocadoLeaf-Highfive/pdf-pptx-watermark#mobile-parameter-tuning) <br>
- [Watermark effects](https://github.com/AvocadoLeaf-Highfive/pdf-pptx-watermark#watermark-effects) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Watermarked PDF files, JSON configuration, and Markdown instructions with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python 3, PyPDF2, reportlab, and LibreOffice for PPT/PPTX conversion.] <br>

## Skill Version(s): <br>
1.5.2 (source: server release metadata; artifact frontmatter reports 1.5.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

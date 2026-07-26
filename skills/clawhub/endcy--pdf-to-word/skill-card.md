## Description: <br>
Converts local PDF documents to Word DOCX files while attempting to preserve paragraphs, tables, images, and layout. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endcy](https://clawhub.ai/user/endcy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, employees, and external users can use this skill to convert PDFs they are authorized to access into editable Word DOCX files. It is intended for local document conversion workflows where preserving visible layout is useful. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-specified local PDFs and writes DOCX files, which may involve sensitive documents. <br>
Mitigation: Use it only with files the user is authorized to process, and confirm local conversion aligns with the organization's document handling policy. <br>
Risk: The skill depends on Python PDF conversion libraries installed in the local runtime. <br>
Mitigation: Install dependencies from trusted package sources, keep the OpenClaw and Python runtime current, and avoid untrusted dependency mirrors. <br>
Risk: Converted output may not perfectly preserve source layout, especially for scanned or image-based PDFs. <br>
Mitigation: Review the generated DOCX before relying on it for business, legal, or compliance-sensitive work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/endcy/skills/pdf-to-word) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [VERIFICATION_REPORT.md](artifact/VERIFICATION_REPORT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Shell commands] <br>
**Output Format:** [DOCX file plus command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local PDF input path and optionally accepts an output DOCX path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

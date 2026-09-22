## Description:

Pdf Toolkit lets agents inspect, extract, transform, create, merge, split, rotate, OCR, and convert PDF, DOCX, and text content through a local command-line utility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youpele52](https://clawhub.ai/user/youpele52)

### License/Terms of Use:


## Use Case:

Developers, operators, and external users can use this skill to automate common document workflows such as PDF inspection, text and table extraction, image extraction, page operations, DOCX reading and writing, OCR, text-to-speech audio generation, and document conversion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read from and write to caller-supplied host paths.

Mitigation: Run it only on files and output locations you intend to expose, and review requested paths before execution.

Risk: The text-to-speech command sends input text to an external service.

Mitigation: Do not use TTS with confidential, regulated, or private content unless that off-host processing is acceptable.

Risk: Runtime dependencies are installed and executed through uv and optional local binaries.

Mitigation: Use a locked or reviewed dependency environment and run the doctor command to confirm required local tools before relying on optional OCR, TTS, or conversion features.

## Reference(s):

- [pypdf documentation](https://pypdf.readthedocs.io)
- [ClawHub skill page](https://clawhub.ai/youpele52/skills/pdf-toolkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Plain text status and extracted content, with generated files written to caller-supplied paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some commands create PDF, DOCX, image, audio, or converted document files; errors are prefixed with "Error:".]

## Skill Version(s):

0.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

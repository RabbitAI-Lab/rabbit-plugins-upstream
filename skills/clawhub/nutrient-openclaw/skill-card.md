## Description: <br>
OpenClaw-native document processing skill for converting, OCRing, extracting, redacting, watermarking, signing, and checking Nutrient DWS API credits from OpenClaw chats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to process PDFs and other documents through Nutrient DWS from OpenClaw conversations, including conversion, OCR, extraction, redaction, watermarking, digital signatures, and credit checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected documents or extracted document content are sent to Nutrient DWS for processing. <br>
Mitigation: Install only when third-party document processing is acceptable, review Nutrient security and privacy documentation, and start with non-sensitive sample files. <br>
Risk: Redaction, signing, watermarking, OCR, or extraction results may be incomplete or unsuitable for a production decision without review. <br>
Mitigation: Review generated outputs before relying on them, especially for sensitive documents or compliance workflows. <br>
Risk: A broad API key can increase impact if exposed or misused. <br>
Mitigation: Use a dedicated or least-privilege API key where possible and rotate it according to organizational policy. <br>


## Reference(s): <br>
- [Nutrient API](https://www.nutrient.io/api/) <br>
- [Nutrient Processor API Security](https://www.nutrient.io/api/documentation/security) <br>
- [Nutrient OpenClaw Repository](https://github.com/PSPDFKit-labs/nutrient-openclaw) <br>
- [ClawHub Skill Page](https://clawhub.ai/jdrhyne/skills/nutrient-openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, YAML configuration, and document-processing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses configured Nutrient DWS credentials and sends selected files or extracted document content to Nutrient DWS for processing.] <br>

## Skill Version(s): <br>
1.2.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

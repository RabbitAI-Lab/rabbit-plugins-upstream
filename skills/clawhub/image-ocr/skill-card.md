## Description: <br>
Extract text from images using Tesseract OCR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to extract text from screenshots, scanned documents, and other image files with local Tesseract OCR. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the skill requires adding the Tesseract system package. <br>
Mitigation: Install only in environments where adding that package is acceptable and reviewed. <br>
Risk: OCR reads image contents to extract text. <br>
Mitigation: Use the skill only on images the agent is authorized to process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/image-ocr) <br>
- [Publisher profile](https://clawhub.ai/user/xejrax) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text OCR output and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the local tesseract binary; CLI usage supports selecting an OCR language with --lang.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Converts phone screenshots into structured Word and Markdown knowledge documents using OCR and AI-assisted categorization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haoyiyong985](https://clawhub.ai/user/haoyiyong985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure screenshot processing, extract text from images, classify captured content, and produce organized knowledge-base documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Screenshots and extracted text may be sent to cloud OCR, LLM, or note-sync services when those integrations are configured. <br>
Mitigation: Use local Tesseract-only mode for sensitive screenshots and configure cloud services only when off-device processing is acceptable. <br>
Risk: API keys may be stored in local configuration files. <br>
Mitigation: Avoid committing or sharing generated credential files, and review configuration files before processing images. <br>
Risk: Processed images are moved into an archive as part of normal operation. <br>
Mitigation: Back up source images before running batch processing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/haoyiyong985/skills/image-knowledge-converter) <br>
- [Usage Guide](artifact/references/usage-guide.md) <br>
- [Multi-Engine OCR Guide](artifact/docs/multi-engine-ocr.md) <br>
- [Tencent Cloud OCR](https://cloud.tencent.com/product/ocr) <br>
- [Baidu OCR](https://ai.baidu.com/tech/ocr) <br>
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Files] <br>
**Output Format:** [Markdown guidance with shell commands and generated Word/Markdown document files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated outputs may include .md, .docx, logs, reports, configuration files, and archived processed images.] <br>

## Skill Version(s): <br>
1.2.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

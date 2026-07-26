## Description: <br>
夸克扫描王一站式图片/文档处理中心，帮助 agents 对用户指定的图片或 URL 执行 OCR、图片翻译、图像增强、图片转 Word/Excel/PDF，以及证件照生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yescan-ai](https://clawhub.ai/user/yescan-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill when they need Quark Scan-powered OCR, image cleanup, image translation, document conversion, or ID photo generation from a user-supplied image file or URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-selected images or URLs are uploaded to Quark Scan as a third-party processor for OCR, enhancement, conversion, or ID photo generation. <br>
Mitigation: Use only with authorization for the submitted content, and avoid sensitive IDs, invoices, business documents, or regulated data unless third-party processing is acceptable. <br>
Risk: The skill requires installing or upgrading the yescan CLI package and configuring SCAN_WEBSERVICE_KEY. <br>
Mitigation: Review the yescan package source and trust posture before installing in shared environments, and keep the API key out of screenshots, logs, and public outputs. <br>


## Reference(s): <br>
- [Quark Scan Open Platform](https://scan.quark.cn/business) <br>
- [ClawHub skill page](https://clawhub.ai/yescan-ai/skills/alibaba-quark-scanking-all) <br>
- [Privacy, Data Flow, and Key Security](references/privacy.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Implementation Details](references/implementation.md) <br>
- [Security Policy](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON response interpretation, OCR text, and local output file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local image or document files for translation, enhancement, conversion, and AIGC scenes.] <br>

## Skill Version(s): <br>
1.1.3 (source: ClawHub server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

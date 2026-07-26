## Description: <br>
高精度文字识别。输入包含文本的图像，自动检测并识别内容。适用于各类文档、广告牌、屏幕截图等场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to extract text from images such as documents, signs, screenshots, and other image-based content through the XiaoBenYang OCR provider. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images are processed by the XiaoBenYang OCR provider, which can expose sensitive visual content to a remote service. <br>
Mitigation: Use only with data approved for that provider, and avoid submitting private IDs, financial records, medical documents, internal screenshots, or other sensitive images unless explicitly approved. <br>
Risk: The required API key is saved in a local .env file. <br>
Mitigation: Protect the local environment file, avoid sharing it, and rotate the key if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/xby-skill/skills/xby-ocr-pro) <br>
- [XiaoBenYang provider site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text summary derived from OCR JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an image URL or Base64 image input and a XiaoBenYang API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

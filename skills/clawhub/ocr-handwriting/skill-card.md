## Description: <br>
输入包含手写文本的图像，自动检测文本行并识别内容。适用于手写笔记、签名、手写表单等。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to route handwriting OCR requests for image URLs or base64-encoded image data and summarize the returned recognition results. It is intended for handwriting scenarios such as notes, signatures, and handwritten forms when the user has a XiaoBenYang API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Handwriting images can contain signatures, identity information, financial forms, or other confidential data that is sent to an external OCR API. <br>
Mitigation: Use the skill only for images you are comfortable submitting to the external OCR service, and avoid sensitive signatures, identity documents, financial forms, and confidential handwriting unless that transfer is acceptable. <br>
Risk: The skill stores the XiaoBenYang API key in a local .env file. <br>
Mitigation: Use a service-specific API key, keep .env out of source control, and rotate the key if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/ocr-handwriting) <br>
- [Publisher profile](https://clawhub.ai/user/xby-skill) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown or text summary of JSON OCR API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key and either an image URL or base64-encoded image data.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

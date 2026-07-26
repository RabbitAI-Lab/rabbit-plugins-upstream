## Description: <br>
兼顾速度与精度的文字识别。输入包含文本的图像，自动检测并识别内容。适用于各类文档、广告牌、屏幕截图等场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to extract text from images, including documents, signs, screenshots, and other image-based text sources. The skill accepts either an image URL or a base64-encoded image and returns OCR results from the remote Xiaobenyang API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images, image URLs, or base64 image data are sent to Xiaobenyang's remote OCR API. <br>
Mitigation: Avoid submitting IDs, invoices, screenshots with secrets, or other sensitive documents unless the provider and data handling behavior have been reviewed. <br>
Risk: The XBY_APIKEY is stored in a plaintext .env file in the working directory. <br>
Mitigation: Use a scoped API key where possible, restrict access to the working directory, and rotate the key if the workspace may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/ocr) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/xby-skill) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, API calls, guidance] <br>
**Output Format:** [JSON results summarized as text or markdown for the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY and sends image URLs or base64 image data to the Xiaobenyang remote OCR API.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
识别驾驶证主页（证号、姓名、性别、国籍、住址、出生日期、准驾车型、初次领证日期、有效期限）和副页（档案编号）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit a Chinese driver's license image URL or base64-encoded image and receive OCR-extracted license fields, including identity details, permitted vehicle class, validity, and archive number. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends driver's license images and extracted identity fields to an external OCR service. <br>
Mitigation: Use only when the user trusts the XiaoBenYang service with this sensitive ID data and has permission to process the image. <br>
Risk: The API key is persisted in a plaintext .env file. <br>
Mitigation: Store only appropriate scoped credentials, restrict workspace access, and rotate the key if the workspace or .env file may have been exposed. <br>
Risk: Raw OCR results are shown back to the user and may contain sensitive personal information or OCR errors. <br>
Mitigation: Review the returned fields before reuse, avoid unnecessary redistribution, and verify important identity data against the original document. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/ocr-driver-license) <br>
- [Publisher profile](https://clawhub.ai/user/xby-skill) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [Markdown or text summary of raw OCR JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided API key and either an image URL or base64-encoded image input.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

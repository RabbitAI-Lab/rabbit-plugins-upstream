## Description: <br>
识别身份证正面（姓名、性别、民族、出生日期、住址、身份证号）和背面（签发机关、有效期限），自动判断正反面并校验身份证号有效性。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to extract structured fields from Chinese ID-card images, either from an image URL or from base64 image data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles government-ID images and extracted identity fields. <br>
Mitigation: Use it only when the user has consent and trusts the XiaoBenYang OCR service with the submitted documents and returned identity data. <br>
Risk: The skill can store the API key in a plaintext .env file. <br>
Mitigation: Prefer providing the API key through a secure environment variable or secret manager instead of persisting it in plaintext. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/ocr-id-card) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown summary of JSON OCR results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key and an ID-card image URL or base64 image input.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

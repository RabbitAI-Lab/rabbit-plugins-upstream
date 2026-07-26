## Description: <br>
识别营业执照的统一社会信用代码、名称、法定代表人、注册资本、成立日期、经营范围、登记机关和住所地址。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers can use this skill to extract structured business-license fields from an image URL or base64-encoded image. The skill is useful for document intake workflows that need OCR output for Chinese business licenses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Xiaobenyang API key and saves it as a persistent plaintext secret in a .env file. <br>
Mitigation: Use a disposable or tightly scoped API key, restrict local file access, and rotate the key if the workspace or .env file is exposed. <br>
Risk: Business-license images and base64 document contents are sent to an external OCR API. <br>
Mitigation: Use the skill only when sharing those documents with the external provider is acceptable under the user's privacy, compliance, and data-handling requirements. <br>
Risk: Server evidence marks the release as suspicious because of incomplete disclosure and scope mismatches. <br>
Mitigation: Review the skill behavior and publisher trust before deployment, especially in workflows that process sensitive company documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/ocr-biz-license) <br>
- [Xiaobenyang API provider](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration guidance] <br>
**Output Format:** [Markdown summary of OCR results, derived from JSON returned by the external API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a business-license image URL or base64 image input and a Xiaobenyang API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

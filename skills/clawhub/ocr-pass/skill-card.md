## Description: <br>
识别港澳通行证、台湾通行证的通行证号码、姓名、性别、出生日期、有效期、签发地点等信息，支持MRZ机读码解析。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to extract key fields from authorized Hong Kong, Macau, and Taiwan travel-permit images. It supports image URL and base64 image inputs and returns OCR results for agent presentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Passport or travel-permit images and extracted personal information may be sent to an external OCR provider. <br>
Mitigation: Use the skill only for authorized documents, confirm the provider's data handling terms before use, and avoid real identity documents in tests unless necessary. <br>
Risk: API credentials may be stored in a plaintext .env file. <br>
Mitigation: Use scoped and revocable API keys, restrict local file access, and remove stored keys when the workflow is complete. <br>
Risk: Broad dependency lower bounds may allow unreviewed dependency versions in sensitive workflows. <br>
Mitigation: Review and pin dependency versions before using the skill in production or regulated identity-document processing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/ocr-pass) <br>
- [Publisher profile](https://clawhub.ai/user/xby-skill) <br>
- [XiaoBenYang service site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [Markdown summary derived from OCR JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes success status, status message, and raw OCR result fields for the agent to summarize.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

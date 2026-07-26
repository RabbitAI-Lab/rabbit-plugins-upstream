## Description: <br>
识别护照号码、中文姓名、英文姓名、性别、国籍、出生日期、签发日期、有效期至、签发地点等信息，支持MRZ机读码解析。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to submit passport image URLs or base64 image data to Xiaobenyang's OCR API and return extracted passport fields, including MRZ data, to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Passport images and image URLs are sent to Xiaobenyang's OCR API for processing. <br>
Mitigation: Use the skill only with the passport holder's permission and only when sending this sensitive data to the third-party API is acceptable. <br>
Risk: The API key may be stored in a plaintext .env file. <br>
Mitigation: Use a dedicated API key with limited exposure and keep the .env file out of commits, shared folders, and broad-access directories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/ocr-passport) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown summary of raw JSON OCR results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a dict with success, raw, and message fields after calling the OCR API.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

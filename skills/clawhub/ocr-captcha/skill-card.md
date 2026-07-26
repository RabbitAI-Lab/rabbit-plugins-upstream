## Description: <br>
输入常见验证码图片，返回验证码文本内容。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to submit captcha images by URL or Base64 to the XiaoBenYang OCR API and receive the extracted captcha text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends captcha images and the API key to the third-party XiaoBenYang service. <br>
Mitigation: Install only when that service is trusted, avoid sensitive or account-bound captchas, and disclose the third-party upload path to users. <br>
Risk: The skill persists the API key in a local .env file. <br>
Mitigation: Treat the saved key as a local secret, restrict file access, rotate exposed keys, and prefer a proper secret store for managed deployments. <br>
Risk: Server security evidence flags copied Gaokao/MCP scaffolding that makes the skill scope unclear. <br>
Mitigation: Review the artifact before deployment and prefer a cleaned version whose files and documentation match the captcha OCR scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/ocr-captcha) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON] <br>
**Output Format:** [JSON API result summarized as user-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided API key and a captcha image URL or Base64 image input.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

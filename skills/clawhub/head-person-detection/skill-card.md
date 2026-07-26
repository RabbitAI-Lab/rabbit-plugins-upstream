## Description: <br>
输入一张图像，对其中的人头人体进行检测，输出图片中所有目标的检测框、置信度和标签。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to detect heads and human bodies in supplied images through the XiaoBenYang API. It returns bounding boxes, confidence scores, and labels that an agent can present for review or use in downstream workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image URLs or base64 image contents are sent to an external XiaoBenYang service. <br>
Mitigation: Use this skill only with images appropriate for that provider and confirm the provider's privacy terms before processing sensitive photos. <br>
Risk: The required XiaoBenYang API key may be stored locally in a plaintext .env file. <br>
Mitigation: Protect the .env file, avoid sharing workspaces that contain it, and rotate or revoke the key if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/head-person-detection) <br>
- [XiaoBenYang API key page](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON] <br>
**Output Format:** [Structured JSON detection results summarized in text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns detection boxes, confidence scores, and labels; requires an API key and an image URL or base64-encoded image input.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

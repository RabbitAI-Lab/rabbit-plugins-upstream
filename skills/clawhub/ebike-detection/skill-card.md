## Description: <br>
输入一张图像，对其中的电动自行车进行检测，输出图片中所有目标的检测框、置信度和标签。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit an image URL or base64-encoded image and receive e-bike detection boxes, confidence scores, and labels from the XiaoBenYang service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and stores it locally in a .env file. <br>
Mitigation: Treat the API key as sensitive, avoid committing or sharing the .env file, and remove the key when the skill is no longer used. <br>
Risk: Image URLs or base64 image content are sent to the external XiaoBenYang API for detection. <br>
Mitigation: Use only images that are approved for external processing and avoid submitting sensitive or regulated image content. <br>
Risk: The artifact contains stale Gaokao naming references that do not match the e-bike detection purpose. <br>
Mitigation: Review packaging and documentation changes carefully before upgrading or redistributing the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/ebike-detection) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API host](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns raw API response fields for detections, including bounding boxes, confidence scores, and labels when supplied by the upstream service.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

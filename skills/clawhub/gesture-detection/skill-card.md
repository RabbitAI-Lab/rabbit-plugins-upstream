## Description: <br>
输入一张图像，对其中的手势进行检测，输出图片中所有目标的检测框、置信度和标签。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit an image URL or base64-encoded image data to a gesture-detection API and receive detected gesture boxes, confidence scores, and labels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends gesture images or image URLs to XiaoBenYang's remote API. <br>
Mitigation: Use it only with images approved for that external service and avoid sensitive image data unless the service terms and privacy posture are acceptable. <br>
Risk: The skill stores the XiaoBenYang API key in a local plaintext .env file. <br>
Mitigation: Prefer a scoped or disposable API key and use a managed secret store where the deployment environment supports one. <br>
Risk: The package contains stale Gaokao-related code and instructions. <br>
Mitigation: Review or remove stale references before using the package in a sensitive environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/gesture-detection) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON results summarized in Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns raw API data with success status and message fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

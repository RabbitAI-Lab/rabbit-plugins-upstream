## Description: <br>
输入一张图像，对其中的手机进行检测，输出图片中所有目标的检测框、置信度和标签。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to submit an image URL or base64-encoded image to a remote phone-detection API and return detected phone bounding boxes, confidence scores, and labels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted images or image URLs are sent to XiaoBenYang's external API service. <br>
Mitigation: Avoid submitting sensitive images unless external processing is acceptable for the use case. <br>
Risk: The XBY API key is stored in a local plaintext .env file. <br>
Mitigation: Use a limited, rotatable API key and delete or rotate it when the skill is no longer used. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/cellphone-detection) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API Calls] <br>
**Output Format:** [JSON from the remote API, summarized for the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an image URL or base64-encoded image and an XBY API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

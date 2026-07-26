## Description: <br>
输入一张图像，对其中的香烟目标进行检测，输出图片中所有目标的检测框、置信度和标签。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to send an image URL or base64-encoded image to a remote API for cigarette-object detection and receive detected boxes, confidence scores, and labels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images or image URLs are sent to XiaoBenYang's remote API. <br>
Mitigation: Avoid sensitive images and review privacy expectations before using the skill. <br>
Risk: The skill stores the API key in a local plaintext .env file. <br>
Mitigation: Limit key scope where possible and document how to remove or rotate the saved key after use. <br>
Risk: The artifact includes unrelated Gaokao references that may confuse review or operation. <br>
Mitigation: Review the skill before deployment and prefer a cleaned version that removes unrelated references. <br>
Risk: Dependencies are declared without exact pins. <br>
Mitigation: Pin and review dependency versions before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/smoking-detection) <br>
- [XiaoBenYang API provider](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON results summarized in Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns remote API data including detection boxes, confidence scores, labels, success status, and status message.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

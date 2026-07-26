## Description: <br>
检测各类通用场景中出现的火焰，最佳使用场景：安防摄像头、交通摄像头视角。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to detect fire in general image inputs, especially security-camera and traffic-camera scenes, by submitting either an image URL or Base64-encoded image data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image URLs or full Base64 image contents are sent to XiaoBenYang's external API. <br>
Mitigation: Use the skill only when sharing the image data with that external service is acceptable; avoid private camera footage or other sensitive images. <br>
Risk: The API key may be saved in plaintext in a .env file. <br>
Mitigation: Use a disposable or restricted API key and avoid providing important reusable credentials through chat. <br>
Risk: Copied Gaokao configuration text may confuse review or maintenance of the fire-detection skill. <br>
Mitigation: Review the configuration and public instructions before deployment so operators understand the actual fire-detection behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/fire-detection) <br>
- [XiaoBenYang API provider site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an API key and sends image URLs or Base64 image contents to an external API.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

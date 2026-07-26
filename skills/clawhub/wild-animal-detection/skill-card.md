## Description: <br>
输入一张图像，输出图像中所有识别到的野生动物的检测框、置信度及标签。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to send an image URL or Base64-encoded image to a XiaoBenYang API and receive detected wild-animal labels, confidence scores, and bounding boxes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and saves it in a local .env file. <br>
Mitigation: Use a dedicated API key with least necessary access, protect the .env file as a local secret, and remove or rotate the key after testing or decommissioning. <br>
Risk: Image URLs or Base64 image contents are sent to a third-party service. <br>
Mitigation: Avoid submitting sensitive, private, biometric, or location-revealing images unless the provider's data handling is acceptable for the intended use. <br>
Risk: Security evidence notes unrelated Gaokao and school-search leftovers that make the skill scope unclear. <br>
Mitigation: Review the artifact before deployment and confirm only the wild-animal detection functions are exposed in the target agent environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/wild-animal-detection) <br>
- [Publisher profile](https://clawhub.ai/user/cainingnk) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>
- [XiaoBenYang API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns raw detection data containing labels, confidence scores, and bounding boxes when the upstream API succeeds.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

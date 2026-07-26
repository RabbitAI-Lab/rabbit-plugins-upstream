## Description: <br>
对包含主体物体的图像进行标签识别，输出主体物体的类别标签，目前已经覆盖了5万多类的物体类别。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit an image URL or base64-encoded image and receive a category label for the main object in the image. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and stores it in a local plaintext .env file. <br>
Mitigation: Install only where plaintext local key storage is acceptable, restrict filesystem access to the .env file, and rotate the key if it may have been exposed. <br>
Risk: The skill sends image URLs or full base64 image data to an external image-recognition provider. <br>
Mitigation: Avoid submitting sensitive personal or confidential images unless the provider is trusted and its data handling terms have been reviewed. <br>
Risk: The security summary notes unrelated leftover Gaokao references in the artifact. <br>
Mitigation: Review the skill text and scripts before deployment to confirm the release behavior matches the intended image-recognition use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/general-recognition) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON] <br>
**Output Format:** [JSON API response summarized as user-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key and either an image URL or base64-encoded image data.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

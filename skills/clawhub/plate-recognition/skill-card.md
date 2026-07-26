## Description: <br>
识别车牌号、车牌颜色、单/双层车牌、位置框。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit vehicle images or image URLs to XiaoBenYang's API and receive license plate text, color, layer type, and bounding-box details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: License plate images or image links are sent to XiaoBenYang's third-party API. <br>
Mitigation: Use only images you are permitted to process and review the provider's privacy and retention terms before installation. <br>
Risk: The XiaoBenYang API key may be stored in a local plaintext .env file. <br>
Mitigation: Protect the local environment file, rotate exposed keys, and avoid shared machines or repositories for stored secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/plate-recognition) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Guidance] <br>
**Output Format:** [JSON API response summarized as user-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns the upstream raw payload with success and message fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

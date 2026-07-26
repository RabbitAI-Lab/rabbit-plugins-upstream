## Description: <br>
识别机动车行驶证的号牌号码、车辆类型、所有人、住址、品牌型号、发动机号码、车辆识别代号等信息，支持自动方向检测和主副页过滤。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit vehicle-license images by URL or Base64 and receive OCR results for license plate, vehicle type, owner, address, model, engine number, VIN, and related fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Vehicle-license images and extracted personal or vehicle identifiers are sent to the Xiaobenyang OCR API. <br>
Mitigation: Submit only documents the user is authorized to share with that provider, and avoid processing sensitive licenses without consent. <br>
Risk: The API key is saved locally in a plaintext .env file. <br>
Mitigation: Use a limited-scope API key, restrict local file access, and rotate the key if the workspace or .env file may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/ocr-vehicle-license) <br>
- [Xiaobenyang API site](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown summary with JSON-derived OCR fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY and either an image URL or a Base64-encoded image.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

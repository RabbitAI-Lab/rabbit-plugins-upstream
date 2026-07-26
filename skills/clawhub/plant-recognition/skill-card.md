## Description: <br>
识别植物名称（或所属科, 属, 种或亚种）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to identify plant names or taxonomy from an image URL or base64-encoded image data through the Xiaobenyang API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a Xiaobenyang API key locally in a .env file and uses it when calling the provider. <br>
Mitigation: Use a revocable API key, protect the local .env file, and rotate or remove the key when it is no longer needed. <br>
Risk: Plant images or image URLs are sent to Xiaobenyang for analysis. <br>
Mitigation: Avoid sensitive photos, private or internal image URLs, and any image content that should not be shared with the provider. <br>


## Reference(s): <br>
- [Xiaobenyang API provider](https://xiaobenyang.com) <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/plant-recognition) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Markdown, JSON] <br>
**Output Format:** [Markdown summary of raw JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Xiaobenyang API key and either an image URL or base64-encoded image data.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

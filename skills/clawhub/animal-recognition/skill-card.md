## Description: <br>
对含有动物的图像进行标签识别，无需任何额外输入，输出动物的类别标签。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to identify animal category labels from an image supplied as a URL or base64-encoded image data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the API key in plaintext in a local .env file as XBY_APIKEY. <br>
Mitigation: Use a scoped, revocable API key and remove or rotate it when the skill is no longer in use. <br>
Risk: The skill sends supplied image data to an external XiaoBenYang service. <br>
Mitigation: Use only non-sensitive images that the user is willing to send to xiaobenyang.com. <br>
Risk: The security verdict requires review before installation because disclosure and scoping are inconsistent. <br>
Mitigation: Review the skill and its remote API workflow before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/animal-recognition) <br>
- [xby-skill publisher profile](https://clawhub.ai/user/xby-skill) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, JSON, Guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an image URL or base64-encoded image data and a configured XBY_APIKEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Detects people, pets, cars, fire, and cardboard boxes in an input image, returning labels, confidence scores, and bounding boxes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to route an image URL or base64-encoded image to object detection and receive detected object labels, confidence scores, and bounding boxes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be stored in plaintext configuration. <br>
Mitigation: Use a managed secret store or environment-level secret injection instead of committing or sharing .env files. <br>
Risk: Submitted images are sent to xiaobenyang.com for processing. <br>
Mitigation: Install only if the publisher and service are trusted, and avoid submitting sensitive or regulated photos. <br>
Risk: Mismatched Gaokao configuration artifacts may cause confusion during review or operation. <br>
Mitigation: Inspect the configuration and remove unrelated Gaokao leftovers before relying on the skill in a production workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/daily-object-detection) <br>
- [Publisher profile](https://clawhub.ai/user/xby-skill) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns detected object labels, confidence scores, and bounding boxes from either image URL or base64 image input.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

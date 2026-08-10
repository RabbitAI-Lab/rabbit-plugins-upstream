## Description: <br>
Detects image quality issues in camera footage, including black or white screens, color cast, stripes, noise, and blurriness for surveillance and camera self-check workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze camera images, video frames, or supplied media URLs for common image quality defects and to retrieve structured cloud analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes camera images, videos, or supplied URLs through the Life Emergence cloud service. <br>
Mitigation: Use it only with media approved under organizational privacy requirements, especially for surveillance footage or sensitive environments. <br>
Risk: The skill automatically creates or reuses a local identity, logs in remotely, and stores returned access tokens in the workspace data directory. <br>
Mitigation: Review identity and token handling before deployment, restrict workspace access, and clear stored credentials when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Markdown and JSON analysis reports, with optional shell command examples and saved text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include structured analysis results, historical report lists, recommendations, and report links.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

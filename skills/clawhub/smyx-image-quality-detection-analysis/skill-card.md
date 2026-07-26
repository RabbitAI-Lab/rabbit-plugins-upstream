## Description: <br>
Detects camera image or video quality problems such as black screens, white screens, color casts, stripes, snow noise, and blur for surveillance self-check and maintenance workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and camera operations teams use this skill to analyze uploaded camera images, videos, or image URLs for common visual quality defects and to review structured reports and report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Camera images, videos, or URLs may be sent to configured lifeemergence.com services for analysis. <br>
Mitigation: Confirm that users understand remote processing before analysis and avoid submitting confidential footage unless the configured service is approved for that data. <br>
Risk: Report history is tied to an automatically managed identity, with user records and tokens stored locally. <br>
Mitigation: Review identity creation, token storage, and report-history behavior before deployment; prefer a version that documents retention and asks for confirmation before history lookup or account creation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands] <br>
**Output Format:** [Markdown and JSON analysis reports with optional report links and saved text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can query cloud report history and can save analysis output to a user-specified file.] <br>

## Skill Version(s): <br>
1.0.6 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

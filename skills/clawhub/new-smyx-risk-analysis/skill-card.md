## Description: <br>
Analyzes video or image inputs for fall, abnormal-behavior, and visual health-risk signals, then returns structured risk findings, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit surveillance, care, or safety-monitoring media for cloud-assisted risk analysis and to retrieve identity-linked historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive video, image, and health-risk data may be sent to publisher cloud services. <br>
Mitigation: Use only approved media, confirm recipient and retention expectations before use, and avoid private surveillance footage unless all required permissions are in place. <br>
Risk: Identity-linked report history may be created or reused with limited user control. <br>
Mitigation: Run the skill only where identity-linked history is expected, and review access to generated reports before sharing output. <br>
Risk: Local user and token records may persist in the workspace. <br>
Mitigation: Restrict workspace access and inspect or clear persisted local data according to the deployment's retention policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-risk-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Risk categories and alert levels](references/risk_categories.md) <br>
- [API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis content and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save returned analysis text to a caller-specified output file.] <br>

## Skill Version(s): <br>
999.999.1000 (source: ClawHub release evidence; artifact frontmatter version 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

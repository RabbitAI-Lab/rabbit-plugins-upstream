## Description: <br>
Identifies plant diseases from image or video input and returns structured diagnostic reports with disease type, likely cause, severity context, prevention suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agricultural or horticultural teams use this skill to submit plant images or videos for cloud-based disease recognition and to retrieve structured analysis reports or report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends plant images, videos, URLs, and associated account identifiers to a cloud service for analysis and report-history retrieval. <br>
Mitigation: Review cloud data handling expectations before installation and use only with media and identifiers that are appropriate to send to the service. <br>
Risk: The skill may create or reuse a local identity and store service tokens in a local SQLite database with limited user control. <br>
Mitigation: Run in an approved environment, review local credential storage before deployment, and clear local state when identity reuse is not desired. <br>
Risk: The server evidence classifies the release as suspicious despite no listed individual risk findings. <br>
Mitigation: Perform a security review before installing and restrict execution until the cloud API behavior and local token handling are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-disease-recognition-analysis) <br>
- [API reference](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, files] <br>
**Output Format:** [Markdown or JSON text, with optional file output when an output path is provided.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report links and history-list records; image and video inputs are sent to a cloud service for analysis.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

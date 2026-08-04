## Description: <br>
Combines continuous livestock barn video with environmental sensor data to identify group stress responses associated with abnormal in-barn conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operations teams, animal welfare reviewers, and developers use this skill to analyze livestock barn media together with temperature, humidity, ammonia, carbon dioxide, or related sensor data. It returns behavior-environment correlation findings, stress level indicators, report links, and historical cloud report listings for pre-inspection and anomaly review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends supplied barn media, URLs, and related metadata to Lifeemergence/Open API services for analysis. <br>
Mitigation: Use it only with media and sensor data approved for that service boundary, and review retention, access, and data-sharing expectations before processing sensitive farm footage. <br>
Risk: The skill may create or reuse a local internal identity and store account tokens in a workspace SQLite database. <br>
Mitigation: Run it in a controlled workspace, restrict local database access, and rotate or remove stored credentials according to the deployment's credential handling policy. <br>
Risk: Historical report queries return cloud report history associated with the resolved internal identity. <br>
Mitigation: Confirm the active identity context before listing reports and avoid sharing returned report links outside authorized farm or account users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Environmental anomaly API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or structured JSON text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include behavior observations, environment correlation results, stress-level labels, exported report image URLs, and cloud history listings.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

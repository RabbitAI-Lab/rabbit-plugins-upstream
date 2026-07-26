## Description: <br>
Utilizes vision and radar technology for contactless detection of falls, triggering alarms within seconds for home safety monitoring of elderly people living alone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregiving, elder-care, and home-monitoring users can submit images, videos, or URLs for fall-detection analysis and cloud report lookup. Results should be treated as safety alerts that require human confirmation and appropriate emergency follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elder-care photos, videos, and report history may be sent to the configured lifeemergence.com backend. <br>
Mitigation: Use only with appropriate consent and authority, review privacy expectations before installation, and avoid submitting unrelated personal media. <br>
Risk: Silent identity creation, identity linking, and token storage can reduce user visibility into account control. <br>
Mitigation: Confirm the account and token handling model before deployment, isolate runtime credentials, and remove stored tokens when decommissioning the skill. <br>
Risk: Cloud history retrieval may expose prior fall-detection reports or report links. <br>
Mitigation: Restrict use to authorized users and review report links before sharing outputs outside the care or monitoring workflow. <br>
Risk: Fall-detection results may be incorrect or incomplete. <br>
Mitigation: Treat outputs as safety alerts, not final determinations; manually confirm alarms and escalate through appropriate emergency or caregiver channels. <br>


## Reference(s): <br>
- [API 接口文档](artifact/references/api_doc.md) <br>
- [API接口文档](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-fall-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured command output, with optional JSON detail and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include fall-detection findings, recommendations, historical report tables, and links to cloud-hosted reports.] <br>

## Skill Version(s): <br>
1.0.8 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

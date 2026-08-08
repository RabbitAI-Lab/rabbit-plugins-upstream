## Description: <br>
Detects strangers near minors from monitoring images, videos, local files, or URLs and returns safety alerts, structured analysis, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze monitoring media for possible strangers near minors, assess risk, and retrieve prior warning reports from the cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images or videos involving minors may be uploaded to the lifeemergence.com backend for analysis. <br>
Mitigation: Use only with appropriate consent and confirm backend retention, deletion, and access-control policies before deployment. <br>
Risk: Reports are associated with a silently managed local identity and persisted account tokens. <br>
Mitigation: Review identity creation and token storage, and provide account revocation, token rotation, and deletion procedures for operators. <br>
Risk: Cloud history retrieval may expose prior analysis reports and report links. <br>
Mitigation: Limit report-list and export access to authorized users and audit access before use in homes, schools, or childcare settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-approach-warning-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [smyx_analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Markdown or JSON analysis output with optional saved result file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured findings, risk level, recommendations, report links, and cloud history tables.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

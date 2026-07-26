## Description: <br>
Detects people in target areas from monitoring videos or video URLs and returns structured human-detection reports for access monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and site security teams use this skill to analyze fixed-camera monitoring footage for personnel presence, counts, intrusion indicators, and prior report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monitoring footage or video URLs may be sent to a configured remote service. <br>
Mitigation: Use only footage approved for this service and avoid workplace, restricted-area, or personally identifiable media unless retention and processing controls have been reviewed. <br>
Risk: The skill can silently create or reuse a local identity and persist account tokens in a workspace SQLite database. <br>
Mitigation: Run it in an environment where token storage is acceptable, access to the workspace database is controlled, and persisted identities can be reviewed or cleared. <br>
Risk: Historical cloud report lookup may expose prior analysis records associated with the resolved identity. <br>
Mitigation: Limit use to authorized operators and verify that cloud report access aligns with organizational privacy and access-control requirements. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-detection-analysis) <br>
- [API 接口文档](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON text reports, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return structured detection results, report links, and historical report tables; video inputs are documented as mp4, avi, or mov up to 10MB.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

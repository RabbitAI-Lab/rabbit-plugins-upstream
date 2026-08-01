## Description: <br>
Automatically detects personnel in target areas from video or image inputs using computer vision, supports real-time stream analysis, and returns structured human-detection reports for monitored areas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security, facilities, and operations teams use this skill to analyze surveillance video, video URLs, or uploaded media for people presence, counts, frequency, and intrusion indicators in parks, offices, and restricted areas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends video inputs and report-history requests to external lifeemergence.com APIs. <br>
Mitigation: Review data sensitivity, retention expectations, and network policy before using it with private camera streams or sensitive facilities footage. <br>
Risk: The skill can silently create or reuse a local identity and store tokens in a workspace SQLite database. <br>
Mitigation: Install only where local identity creation and token persistence are acceptable, and protect or rotate the workspace data store according to local policy. <br>
Risk: The skill can retrieve cloud report history associated with the resolved local identity. <br>
Mitigation: Confirm that cloud history access aligns with the user's privacy and access-control requirements before enabling historical report queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown report with optional JSON detail and report export links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write the report to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

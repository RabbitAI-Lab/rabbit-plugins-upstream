## Description: <br>
Analyzes in-cabin driver-face video to detect eye open/closed state, blink rate, prolonged eye closure, PERCLOS, and fatigue-driving warning signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and fleet-safety teams use this skill to analyze DMS driver-face videos or video URLs, generate structured fatigue indicators and warning recommendations, and query cloud-hosted historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver-monitoring videos or video URLs may be sent to cloud services for analysis. <br>
Mitigation: Use only when operators are comfortable sending this footage to the listed cloud services and have explicit driver consent. <br>
Risk: Cloud report-history queries can expose sensitive driver or fleet monitoring records. <br>
Mitigation: Confirm retention, access-control, and deletion policies with the publisher before fleet or workplace deployment. <br>
Risk: The skill may create or reuse a local identity and store service tokens locally. <br>
Mitigation: Install only in controlled workspaces where local credential storage is acceptable and can be reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-driver-blink-fatigue-detection-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Driver fatigue API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown text with structured JSON result content and optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include fatigue indicators, warning recommendations, report-history listings, and report export links.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

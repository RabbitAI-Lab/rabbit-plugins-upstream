## Description: <br>
Early monitoring of plant wilting based on hyperspectral imaging and computer vision, capturing early wilting signs before visible symptoms and providing early warning for precision irrigation and disease control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to analyze plant image or video inputs, distinguish environmental wilting from pathological wilt, quantify wilting severity, and return early-warning reports with recommendations. It can also retrieve cloud-hosted historical plant wilting monitoring reports associated with the internally resolved identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant image or video inputs may be sent to lifeemergence.com services for analysis. <br>
Mitigation: Use only with plant media approved for external service processing, and avoid sensitive local files or shared workspaces unless that data flow is acceptable. <br>
Risk: The skill silently creates or reuses an internal identity and ties cloud report history to that identity. <br>
Mitigation: Review the identity behavior before installation and run it only where automatic identity association and cloud history retrieval are acceptable. <br>
Risk: Token-like credentials and user records may be stored locally in a workspace SQLite database. <br>
Mitigation: Avoid environments where local token storage is unacceptable, and isolate or clean the workspace data directory when testing or uninstalling the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis text, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include plant wilting analysis, severity and cause indicators, recommendations, report links, and cloud report-history listings.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

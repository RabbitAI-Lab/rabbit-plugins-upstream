## Description: <br>
Analyzes pet race start and finish videos to identify false starts, lane crossings, finish order, lane assignment, and supporting evidence for referee review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Event organizers, referees, trainers, and developers use this skill to review pet racing video for objective foul-detection results. It supports adjudication workflows by returning structured findings, evidence snippets, and historical report listings without providing race advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Race videos may be uploaded to a configured cloud analysis service. <br>
Mitigation: Use the skill only when that service and its data handling are acceptable for the video content being analyzed. <br>
Risk: The skill can silently create or reuse a local identity and store identity tokens for report association. <br>
Mitigation: Run it in a workspace where local identity-token storage is acceptable, and avoid placing unrelated secrets in the workspace data directory. <br>
Risk: Historical report retrieval may return identity-linked cloud reports. <br>
Mitigation: Review generated report listings before sharing them and limit use to environments where identity-linked report access is expected. <br>


## Reference(s): <br>
- [Skill API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown reports and tables, with JSON available for detailed analysis output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links, detected foul status, lane and finish-order details, and history listings from the configured cloud service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Analyzes child activity-zone images, videos, or URLs to detect contact with dangerous objects or electrical sockets and return structured warning results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to route child-monitoring media through a cloud analysis service that detects dangerous object contact, socket interaction, and related warning levels. It is intended as an auxiliary alerting workflow for homes, kindergartens, and early-education settings, not as a replacement for adult supervision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Child-monitoring images, videos, or URLs may be processed by the publisher's cloud service. <br>
Mitigation: Use only with appropriate guardian consent, confirm the publisher's retention and deletion practices, and avoid submitting media that is not necessary for the safety task. <br>
Risk: Cloud history queries and generated report links may expose sensitive information about children and monitored locations. <br>
Mitigation: Limit access to report links, review who can retrieve historical reports, and remove stale reports according to the user's privacy requirements. <br>
Risk: The skill silently creates or reuses an identity and stores service tokens locally. <br>
Mitigation: Review token storage, rotation, and revocation expectations before installation, especially on shared systems. <br>
Risk: Detection results may be incomplete or incorrect and cannot guarantee child safety. <br>
Mitigation: Treat alerts as auxiliary signals, maintain adult supervision, and test the skill with representative camera angles and lighting before relying on it operationally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-dangerous-object-detection-analysis) <br>
- [Skill API interface document](references/api_doc.md) <br>
- [Shared API error-code reference](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown tables and structured JSON analysis results with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include alert levels, detected object classes, confidence values, timestamps, snapshot URLs, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

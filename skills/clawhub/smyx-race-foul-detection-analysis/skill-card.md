## Description: <br>
Analyzes pet race start and finish videos or URLs to identify start timing, finish order, lane assignment, false starts, and lane-crossing fouls, returning objective referee-assist results rather than race advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, event staff, and developers use this skill to submit pet race videos or video URLs for foul detection and structured referee-assist reporting. It can also retrieve cloud-stored historical race foul reports for the resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Race videos, video URLs, and analysis requests are sent to lifeemergence.com services. <br>
Mitigation: Use the skill only for footage whose upload to that service is acceptable; avoid sensitive, proprietary, or private race footage unless the data flow has been approved. <br>
Risk: The skill can create or reuse a local identity and store auth tokens in a workspace SQLite database. <br>
Mitigation: Review local workspace data before sharing or archiving the workspace, and rotate or remove stored credentials when the skill is no longer needed. <br>
Risk: Historical report queries can retrieve cloud-stored report history associated with the resolved identity. <br>
Mitigation: Run history queries only when the user expects cloud report retrieval and the account association is appropriate. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Pet Race Foul Detection API Documentation](artifact/references/api_doc.md) <br>
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-formatted text with optional report links and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analysis uses local video files or public video URLs and history queries return API-backed report lists.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; SKILL.md frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

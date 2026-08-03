## Description: <br>
Analyzes child or student study-session media to identify learning behavior patterns, poor study habits, and risk signals, then returns structured reports with family education improvement suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, parents, educators, and developers use this skill to submit study-session videos or images for learning behavior analysis, receive structured reports, and retrieve historical learning behavior reports associated with the user account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process videos or images of minors through external cloud services. <br>
Mitigation: Review consent, privacy, retention, and compliance requirements before installation or use. <br>
Risk: The skill can create or reuse a cloud-linked identity and persist local account tokens in the workspace data directory. <br>
Mitigation: Install only where this account persistence is acceptable, limit workspace access, and remove or rotate stored tokens when no longer needed. <br>
Risk: Historical report queries are identity-linked and retrieved from cloud services. <br>
Mitigation: Confirm that users understand the history-report data flow and that report access aligns with organizational privacy requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown reports, JSON analysis responses, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include historical report tables and cloud-hosted report export links.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence; artifact frontmatter lists 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

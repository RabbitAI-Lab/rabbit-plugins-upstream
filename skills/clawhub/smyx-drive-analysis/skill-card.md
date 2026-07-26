## Description: <br>
Analyzes driver video or image inputs to identify unsafe driving behaviors and produce structured safety reports with recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit driving footage or media URLs for safety-behavior analysis, including fatigue, distraction, seatbelt use, posture, and other risky driving patterns. The skill returns structured findings, safety suggestions, report links, and cloud report-history results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver media or media URLs are sent to configured LifeEmergence cloud APIs for analysis. <br>
Mitigation: Use only footage that is authorized for cloud processing, avoid sensitive in-cabin or regulated data unless retention and deletion terms are acceptable, and confirm the configured endpoint before use. <br>
Risk: The skill can silently create or reuse a cloud identity and automatically query account-linked report history. <br>
Mitigation: Run it only in workspaces where the account association is expected, and review report-history access expectations before enabling automatic history queries. <br>
Risk: Identity and token material may be stored in a local workspace database. <br>
Mitigation: Protect the workspace data directory, rotate credentials if the workspace is shared or exported, and remove local stored identity data when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>
- [Analysis API Error Codes](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-formatted structured analysis results, report-history tables, report links, and command-line guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include cloud-generated report identifiers and export links. Local file analysis is limited to supported video formats and the configured file-size limit.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

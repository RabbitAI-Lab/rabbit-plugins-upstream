## Description: <br>
Detects workplace phone usage in images or video streams using cloud computer-vision analysis, then returns structured monitoring results, usage counts, duration statistics, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprise operators and workplace-management teams use this skill to analyze office surveillance images, videos, or media URLs for phone-use behavior and to retrieve historical monitoring reports. The output is intended as an internal management aid and should be reviewed alongside privacy, labor, and workplace-notice requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs workplace surveillance analysis and may process employee images or videos. <br>
Mitigation: Confirm employee notice or consent, lawful workplace-monitoring basis, retention rules, and human review before operational use. <br>
Risk: Media and report queries are sent to a cloud service with historical report access. <br>
Mitigation: Use only approved media, verify backend access controls and retention settings, and avoid submitting sensitive footage outside the intended workspace. <br>
Risk: The skill may reuse or create an identity and store authentication tokens in local workspace data. <br>
Mitigation: Run in an isolated workspace, review the workspace data file and SQLite database before use, and remove stored credentials when access should end. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Workplace phone usage monitoring API documentation](references/api_doc.md) <br>
- [Shared API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with optional saved output file and report-link text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires image/video input or a media URL; can also query historical cloud reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata; artifact frontmatter states 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

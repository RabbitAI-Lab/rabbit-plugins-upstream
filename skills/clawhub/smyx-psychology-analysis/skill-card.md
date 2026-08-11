## Description: <br>
Analyzes human mental health and psychological behavior, supports identifying common psychological problem tendencies through video analysis, and provides structured mental health analysis reports and improvement suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit mental-health-related video files or video URLs for cloud analysis, receive structured reports, and query prior reports. It is intended as a wellness reference and does not replace professional mental-health diagnosis or treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive mental-health videos or video URLs are sent to a configured cloud service. <br>
Mitigation: Use the skill only with informed consent, avoid uploading other people's media, and use a separate workspace or account for testing. <br>
Risk: Reports are associated with an automatically selected identity and prior reports can be queried from the cloud service. <br>
Mitigation: Review the active workspace and account context before use, and avoid mixing test reports with production or personal reports. <br>
Risk: Service tokens may persist in the local workspace database. <br>
Mitigation: Limit workspace access, remove or rotate credentials after evaluation, and avoid sharing workspaces that have run the skill. <br>
Risk: Mental-health analysis output may be mistaken for clinical diagnosis or treatment advice. <br>
Mitigation: Present results as a wellness reference only and direct users with mental-health concerns to qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown text with optional structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save report output to a user-specified local file when requested.] <br>

## Skill Version(s): <br>
1.0.15 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

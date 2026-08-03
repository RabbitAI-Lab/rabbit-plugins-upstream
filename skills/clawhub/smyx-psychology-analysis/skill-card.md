## Description: <br>
Analyzes human mental health and psychological behavior, supports identifying common psychological problem tendencies through video analysis, and provides structured mental health analysis reports and improvement suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit video files or video URLs for mental health and psychological behavior analysis, then receive structured reports, risk signals, improvement suggestions, and links to generated reports. It can also retrieve cloud-stored historical mental-health analysis reports associated with the resolved internal identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive mental-health videos, URLs, and analysis results are uploaded to external cloud services. <br>
Mitigation: Use only with media the user is authorized to process, and confirm that cloud processing and retention are acceptable for the use case. <br>
Risk: The skill silently derives or creates an internal identity and can retrieve cloud-stored historical mental-health reports. <br>
Mitigation: Review identity handling, report access controls, and user consent expectations before deployment. <br>
Risk: Local configuration may store authentication tokens or service endpoints used for analysis and history queries. <br>
Mitigation: Protect configuration files, rotate credentials when needed, and avoid exposing tokens in logs or user-facing output. <br>
Risk: Mental-health analysis may be incorrect, incomplete, or inappropriate as a basis for clinical decisions. <br>
Mitigation: Present results as informational screening support only and direct users with health concerns to qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON analysis reports with report links and optional Markdown tables for history results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are mental-health reference material and should not be treated as clinical diagnosis or treatment advice.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release metadata; artifact SKILL.md frontmatter lists 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

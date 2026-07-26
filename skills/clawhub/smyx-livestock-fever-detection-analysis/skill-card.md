## Description: <br>
Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery and returns fever or hypothermia early warnings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and developers use this skill to submit livestock or poultry thermal and visible-light images or videos for body-temperature anomaly screening, including fever, hypothermia, and historical report lookup. It supports early health screening workflows but does not provide disease diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Livestock images, videos, and report queries are sent to the Life Emergence cloud service. <br>
Mitigation: Review data handling, retention, and account ownership requirements before installation, and submit only media approved for cloud processing. <br>
Risk: The skill can create or reuse a local identity and persist authentication tokens in the workspace database. <br>
Mitigation: Restrict access to the workspace data directory, review local storage before sharing the workspace, and rotate or revoke tokens when needed. <br>
Risk: Outputs are screening results rather than veterinary diagnosis or treatment advice. <br>
Mitigation: Use results as early-warning support and require veterinary or laboratory confirmation before disease response decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis) <br>
- [Life Emergence skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown or JSON text with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured analysis results, historical report records, and report export links returned by the cloud service.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter says 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

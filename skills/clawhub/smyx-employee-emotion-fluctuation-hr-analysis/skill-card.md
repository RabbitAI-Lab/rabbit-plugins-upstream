## Description: <br>
Analyzes authorized workplace camera video or URLs to produce HR-facing employee emotion fluctuation reports, baseline comparisons, care alerts, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Authorized HR senior-management users use this skill to analyze consented workplace camera footage, compare anonymous employee-level behavior and expression signals against historical baselines, and retrieve structured care reports for voluntary support conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive employee camera footage and HR emotion reports may be processed through cloud services. <br>
Mitigation: Complete legal, HR, security, and employee-representative review before installation, and require explicit employee notice, consent, and opt-out handling. <br>
Risk: Automatic triggers and report retrieval can expose sensitive employee-related reports if access controls are weak. <br>
Mitigation: Restrict invocation and historical report access to approved HR roles, require backend access controls, and maintain audit logs. <br>
Risk: Uploaded videos, remote URLs, operator identity values, and report metadata may be sent to or associated with the vendor backend. <br>
Mitigation: Review backend data flows, set retention limits, and confirm who can retrieve or export reports before deployment. <br>


## Reference(s): <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with JSON report data, report links, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report output to a file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact SKILL.md frontmatter declares 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

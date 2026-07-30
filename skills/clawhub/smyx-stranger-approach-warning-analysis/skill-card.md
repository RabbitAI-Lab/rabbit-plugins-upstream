## Description: <br>
Detects strangers near minors in images or video, returns structured safety analysis, and can query cloud-hosted historical alert reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and safety operations teams use this skill to analyze monitoring images or videos for stranger proximity risks around minors, produce structured reports, and retrieve historical alert reports from the configured cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive images or video of minors and bystanders may be sent to configured LifeEmergence cloud services for analysis. <br>
Mitigation: Deploy only with consent, legal basis, approved retention expectations, and clear controls for who can access submitted media and generated reports. <br>
Risk: The skill silently creates or reuses an account identity and stores or reuses tokens locally. <br>
Mitigation: Run it in an isolated workspace, review local credential storage before deployment, and rotate or remove tokens when access is no longer needed. <br>
Risk: Historical report lookup can expose cloud-stored safety reports linked to the resolved account identity. <br>
Mitigation: Limit use of report lookup to authorized operators and confirm retention, access, and audit expectations before enabling it. <br>
Risk: The analysis is a safety aid and may be incomplete or incorrect. <br>
Mitigation: Treat alerts as decision support and keep human review and professional safety procedures in place for urgent situations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-approach-warning-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports, Markdown tables for historical reports, and optional saved result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local file or URL inputs; documented media limit is 10 MB.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

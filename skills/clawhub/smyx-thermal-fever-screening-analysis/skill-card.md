## Description: <br>
Analyzes multi-person thermal-imaging photos or video to compare each visible person's skin-surface temperature against the group average and report relative temperature anomalies with a recommendation to recheck using a calibrated thermometer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to submit thermal-imaging footage from gatherings, generate structured relative-temperature screening reports, and retrieve prior cloud reports. It is a screening aid only and should not be used as a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Thermal or household video may contain sensitive health-adjacent personal data and may be uploaded to the publisher's cloud service. <br>
Mitigation: Use only with informed participant consent, appropriate authorization, and an acceptable cloud-data handling arrangement. <br>
Risk: The skill can create or reuse hidden user identities, store tokens locally, and query cloud report history with limited user control. <br>
Mitigation: Review account-handling, token storage, report-history access, retention, and deletion behavior before routine deployment. <br>
Risk: Relative temperature anomalies can be affected by camera quality, calibration, occlusion, recent exercise, hot drinks, sunlight, or nearby heating/cooling sources. <br>
Mitigation: Treat results as screening guidance only and confirm any concern with a calibrated medical thermometer and qualified medical advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis) <br>
- [Skill API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON reports with status text, anomaly details, recommendations, report links, and optional history tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload media to a cloud API and retrieve cloud-hosted report history.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact SKILL.md frontmatter states 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

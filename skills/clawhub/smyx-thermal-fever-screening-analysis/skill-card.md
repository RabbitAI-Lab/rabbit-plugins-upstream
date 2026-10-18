## Description:

Analyzes multi-person thermal-imaging videos to flag relative forehead-temperature anomalies and recommend a thermometer recheck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Families and operators of small shared spaces can screen groups in thermal-camera footage for relative skin-temperature outliers, review cloud-based reports, and arrange a thermometer recheck. The alerts are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Thermal footage or video URLs and identity-linked health reports are sent to a provider cloud service.

Mitigation: Obtain informed consent before monitoring; review the provider's access, retention, and deletion controls before uploading or querying reports.

Risk: The skill silently creates or reuses identity records and stores tokens for report history.

Mitigation: Limit use to trusted environments and review how to remove local workspace data and cloud reports after use.

Risk: Relative skin-temperature readings can be misleading and do not establish a medical diagnosis.

Mitigation: Confirm alerts with a calibrated thermometer and seek professional medical assessment where appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis)
- [Thermal screening API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text analysis and Markdown report-history table with report links; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relative-temperature alerts and recommended follow-up, not a medical diagnosis.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; bundled SKILL.md states 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes livestock behavior in barn videos alongside environmental sensor data to identify group stress responses associated with abnormal conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock facility operators and animal-environment professionals use this skill to assess barn video with environmental sensor readings, identify behavior associated with abnormal conditions, and review historical reports. Its results are intended as an alerting reference; it does not provide equipment-control instructions or environmental adjustment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious for reported account and credential handling, remote data transmission, and behavior that may exceed or not follow its livestock-analysis purpose.

Mitigation: Before use, review whether remote video uploads, account registration, identity and token handling, report queries, and export-only behavior fit your needs.

Risk: The scan was partial and does not establish the behavior of an unresolved reference.

Mitigation: Review the unresolved reference and confirm what data is sent before using the skill with barn video or sensor data.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [API reference](references/api_doc.md)
- [Analysis API details and error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured livestock behavior and environment analysis report, with findings, stress level, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory results; no equipment-control instructions or environmental adjustment advice]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

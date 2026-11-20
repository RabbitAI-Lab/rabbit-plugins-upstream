## Description:

Analyzes sleep-monitoring videos to identify sleep stages, movement, nighttime awakenings, and possible sleep apnea, and can retrieve prior reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People using sleep-monitoring videos can request a structured review of sleep stages, movement, awakenings, and possible apnea, or retrieve earlier reports. Results are for reference and do not replace professional sleep monitoring or medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious for privacy, credential-handling, and purpose-alignment concerns; its analysis is partial because a referenced local path was missing.

Mitigation: Avoid installation until the developer explains remote processing and account creation, documents the data and credentials sent or stored, and addresses the reported URL and environment-only behavior; reassess when the scan evidence is complete.

## Reference(s):

- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Text]

**Output Format:** [Structured sleep analysis in JSON or text; historical report lists in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts MP4, AVI, or MOV videos up to 10 MB; 30 minutes or longer is recommended. Results are informational and not a medical diagnosis.]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

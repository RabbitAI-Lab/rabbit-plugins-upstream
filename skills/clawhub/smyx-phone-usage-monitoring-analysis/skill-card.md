## Description:

Uses computer vision to analyze workplace images and video for phone use, track event frequency and duration, and produce monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Organizations use the skill to review workplace images or video for phone-use events, summarize their frequency and duration, and generate monitoring reports. The reports are intended to support internal management decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee footage is uploaded to the LifeEmergence cloud service for analysis.

Mitigation: Verify the processing destination and terms, disclose monitoring, and obtain required approvals before uploading footage.

Risk: Remote account creation and stored tokens raise account separation and secret-handling concerns.

Mitigation: Use separate user identities, restrict token access, and address the reported secret-handling issues before use.

Risk: The --export-env-only and --api-url options are reported to be ignored, so they may not prevent analysis or control the processing destination.

Mitigation: Confirm actual upload behavior and destination; do not rely on these options until their behavior is corrected.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON or Markdown monitoring reports, with warnings, suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize detected phone-use behavior, event frequency and duration, and monitoring results.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

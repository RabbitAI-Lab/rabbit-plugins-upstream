## Description:

Analyzes short facial videos for heart-rate-variability trends and provides metrics, reports, and access to report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Adults and health-monitoring application developers use short facial videos to review HRV trends, including SDNN and RMSSD, for personal wellness and fatigue awareness. Results are not a substitute for clinical assessment or diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial videos or video URLs may be sent to external services for biometric and health-adjacent analysis.

Mitigation: Obtain informed consent before use and review the service's data handling before sharing videos.

Risk: Report history is associated with an automatically created or reused identity and stored in the cloud.

Mitigation: Confirm that cloud history and identity linkage are acceptable before running analyses or retrieving past reports.

Risk: The skill creates local workspace data and persists service tokens for future history retrieval.

Mitigation: Restrict access to the workspace and stored credentials; remove them when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-facial-hrv-trend-monitoring-analysis)
- [HRV API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Report links]

**Output Format:** [Text or Markdown reports and tables; optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes HRV metrics and links to cloud-hosted reports or report history.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

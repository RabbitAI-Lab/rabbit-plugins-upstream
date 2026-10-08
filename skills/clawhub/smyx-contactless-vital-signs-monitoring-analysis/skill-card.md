## Description:

Analyzes camera video to estimate heart rate, respiration rate, blood oxygen saturation, and heart rate variability without a wearable device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Users and health-monitoring teams can analyze authorized face videos for estimated vital signs and view structured reports or past reports. Results are for health reference, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face footage and inferred health metrics are sent to LifeEmergence cloud services.

Mitigation: Analyze only videos you are authorized to use and review the service's data-handling practices before uploading sensitive footage.

Risk: The skill may silently create or reuse a persistent local identity and token-backed report history.

Mitigation: Review local credential and report retention before use; avoid using it where persistent identity is unacceptable.

Risk: Estimated vital signs may be mistaken for clinical measurements.

Mitigation: Use results only as health reference; seek professional measurement and medical advice for abnormal readings.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report or JSON analysis; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and optionally save results to a file]

## Skill Version(s):

1.0.18 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

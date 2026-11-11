## Description:

Analyzes frontal-face images and videos to estimate emotional expressions, intensity, and anomalies, returning structured reports for human-computer interaction and monitoring workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use the skill to analyze frontal-face images or video for emotion estimates, intensity, anomaly flags, and structured reports in human-computer interaction and monitoring workflows. Its results are informational and do not replace professional psychological assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared account handling can mix users’ sensitive reports.

Mitigation: Postpone shared-user deployments until sender isolation is fixed, and provide account deletion controls.

Risk: The no-analysis option may still allow facial media uploads.

Mitigation: Give users a clear upload and enrollment notice, and postpone use with private facial media until the export-only flag is fixed.

Risk: Sensitive media and credentials may be exposed; provider retention and server-side isolation are unverified.

Mitigation: Protect stored tokens, restrict credential-bearing requests to approved HTTPS origins, disable wire logging, and confirm provider retention and isolation before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured emotion analysis results and reports, including intensity estimates, anomaly flags, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts image or video input; results are estimates of visible emotional expression.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes overnight video from a fixed home camera to track lights-off time and early-morning movement against a personal baseline and produce rhythm-anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families and community care workers use it to review sleep-rhythm changes for people living alone and decide when to check in. It reports visual observations and deviations, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home videos and derived activity patterns may be processed or retained by an external service.

Mitigation: Obtain informed consent and confirm cloud-processing, footage-retention, deletion, and token-storage practices; use privacy-preserving or masked footage where feasible.

Risk: Execution controls, export destination selection, and secret-as-identity handling need fixes, and the external service's monitoring and alert behavior was not verified.

Mitigation: Wait for the stated fixes before using sensitive recordings or production credentials, and verify where exports are written and how credentials are handled.

## Reference(s):

- [API interface and analysis fields](references/api_doc.md)
- [Skill usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report with metrics, baseline deviations, anomaly labels, reminders, and report links; JSON or Markdown output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include lights-off time, early-morning activity counts and duration, historical baseline, anomaly type, and alert level.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

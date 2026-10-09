## Description:

Analyzes nighttime home-camera footage against a personal sleep-rhythm baseline to flag unusual lights-off times and early-morning movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families and community care workers use the skill to review nighttime activity and receive sleep-rhythm anomaly alerts for a person living alone; it does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bedroom or living-room night video is sent to a configured cloud service.

Mitigation: Obtain the monitored person's consent and confirm where footage is sent before use.

Risk: Automatic identity creation and local token persistence limit user control over monitoring data.

Mitigation: Clarify where reports and tokens are stored, and use history features only with authorization, retention, and deletion controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis)
- [Analysis API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports and historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include anomaly alerts, care suggestions, and report links.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

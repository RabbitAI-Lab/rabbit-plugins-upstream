## Description:

Analyzes home-camera footage for prolonged bed rest and reduced eating relative to a person's baseline, then reports behavioral changes for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, and community clinicians can review changes in bed rest and eating patterns for older adults or people living alone. Reports are behavioral observations, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bedroom and dining footage and mental-health observations are highly sensitive and may be sent to cloud services.

Mitigation: Obtain the monitored person's explicit informed consent; confirm cloud retention and deletion practices before use.

Risk: Automatic account selection and locally stored tokens may associate reports with the wrong person or expose account-linked history.

Mitigation: Verify the selected identity before retrieving history and establish how stored tokens and reports can be deleted.

Risk: Changes in activity or eating can be mistaken for a depression diagnosis.

Mitigation: Treat reports as observational signals and seek qualified clinical evaluation rather than using them to diagnose or prescribe treatment.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON, with Markdown tables for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavioral statistics, change alerts, suggested follow-up, and report links; not a diagnosis.]

## Skill Version(s):

1.0.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

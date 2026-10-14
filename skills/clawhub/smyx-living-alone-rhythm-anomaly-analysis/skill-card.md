## Description:

Analyzes nighttime home-camera video against a person's recent sleep-rhythm baseline to flag unusual lights-off times and early-morning movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families, caregivers, and community workers use nighttime video analysis and historical reports to identify changes in the routines of people living alone and decide when to check in. Alerts are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nighttime home-camera media and behavioral reports are sent to a cloud service.

Mitigation: Obtain informed consent from the monitored person or lawful guardian; confirm retention, deletion, and access controls before use.

Risk: The skill automatically creates a local identity, stores tokens, and can access historical cloud reports.

Mitigation: Limit access to reports and verify how the local identity and tokens can be removed.

Risk: Changes in nighttime activity may be mistaken for a medical condition.

Mitigation: Treat alerts as prompts for a human check-in, not as diagnoses.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table, with report links; optionally saved as text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observed rhythm metrics, anomaly notices, and cloud report links when available.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

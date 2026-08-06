## Description:

Analyzes overnight fixed-camera video for a person living alone to identify lights-off timing and early-morning movement, compare them with a 7-14 day personal baseline, and produce rhythm-anomaly reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, community care workers, and developers use this skill to analyze night video from a fixed home camera and surface non-diagnostic sleep-rhythm anomaly reminders for follow-up. It is intended to report visual rhythm metrics and deviations, not to diagnose medical or mental-health conditions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overnight in-home video and derived rhythm reports are highly sensitive personal data.

Mitigation: Use only with explicit consent from the monitored person or authorized guardian, minimize captured detail where possible, and confirm storage, retention, deletion, and report-sharing practices before deployment.

Risk: The skill silently manages user identity, stores access tokens locally, and can query account-linked monitoring history.

Mitigation: Review account and token handling before installation, restrict access to trusted operators, and verify that users have clear controls for history access and deletion.

Risk: Remote video URLs can expose private media or introduce untrusted inputs.

Mitigation: Use trusted video sources only, avoid public or unknown URLs, and validate that uploads are authorized for this care workflow.

Risk: Sleep-rhythm anomalies can be misread as medical conclusions.

Mitigation: Present outputs as visual rhythm metrics and follow-up prompts only; route concerning or repeated anomalies to caregivers or qualified professionals for assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Structured analysis text, Markdown tables for history lists, and JSON-compatible API results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include current rhythm metrics, baseline metrics, deviation scores, anomaly type, alert level, caregiver-facing reminder text, and report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

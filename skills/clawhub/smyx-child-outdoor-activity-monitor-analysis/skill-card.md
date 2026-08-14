## Description:

Analyzes fixed door or balcony camera media to estimate a child's indoor/outdoor transition events, daily outdoor duration, alert status, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, schools, kindergartens, and child-health application developers can use this skill to analyze door or balcony camera footage for child outdoor-time tracking and friendly insufficient-activity reminders. It provides visual activity statistics and should not be used for medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child or household camera footage may be sent to configured LifeEmergence cloud services.

Mitigation: Use only with explicit guardian consent, avoid bystander or highly private footage, and keep captured media under approved retention and access controls.

Risk: Cloud report history is tied to an automatically managed identity, and reusable service tokens may be stored locally.

Mitigation: Run the skill in a managed environment, review local credential and identity storage before installation, and remove stored tokens when access is no longer needed.

Risk: Outdoor duration is inferred from door or balcony transition events and may not reflect actual exercise or health status.

Mitigation: Treat the report as a caregiver-facing activity signal, validate ambiguous results manually, and avoid using it as medical advice or diagnosis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis)
- [Child outdoor activity API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured JSON or Markdown-style report text with optional saved output file and report export link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can query cloud report history; results depend on configured cloud APIs, supported media size and format, and clear indoor/outdoor camera coverage.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

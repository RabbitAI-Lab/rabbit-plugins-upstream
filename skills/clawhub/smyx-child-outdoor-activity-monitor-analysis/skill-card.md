## Description:

Tracks a child's indoor and outdoor crossings in fixed-camera footage, estimates daily time outside, and reports whether it meets a configured goal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use it to review estimated outdoor time from fixed-camera footage and receive activity reminders. Developers can integrate its analysis and report lookup into family or child-health workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video uploads may still occur when the no-analysis option is used.

Mitigation: Review before using children's footage, test with non-sensitive samples, and require clear control over uploads; do not rely on --api-url to redirect processing.

Risk: Account creation and credential storage happen automatically.

Mitigation: Require explicit control over remote enrollment, protected credential storage, and clear data retention and deletion terms.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured activity reports and Markdown report listings with reminders and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include crossing events, session durations, daily totals, goal status, and historical reports]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

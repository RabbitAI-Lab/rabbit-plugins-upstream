## Description:

Analyzes pet water fountain video to estimate drinking frequency, session duration, and daily intake, and flags changes against historical patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use this skill to review drinking behavior from fountain-area videos and compare estimated intake with historical reports. Its alerts are for monitoring, not diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area images or videos are sent to lifeemergence.com services.

Mitigation: Obtain consent and review the service's handling of uploaded media before use.

Risk: The skill silently creates or reuses a cloud identity and associates historical reports with it.

Mitigation: Review account and data-retention behavior before installation; avoid shared workspaces until identity isolation is addressed.

Risk: Tokens are stored in shared local state and caller-controlled hidden identity parameters may affect report access.

Mitigation: Use a scoped credential mechanism and remove caller-controlled identity parameters before use in shared environments.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or historical report list, with optional JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes estimated drinking metrics, change alerts, and report links when available]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

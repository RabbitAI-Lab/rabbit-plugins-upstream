## Description:

Analyzes plant images and optional growth and environmental data to provide a 0–100 vitality score and, when historical observations are available, a trend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners and plant-monitoring operators use this skill to assess plant vitality from images and view current or historical reports. Repeated observations can help them track whether vitality is rising, stable, or declining.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images or videos are sent to configured LifeEmergence cloud services.

Mitigation: Use only media you are comfortable sending to the cloud and review data-sharing requirements before installation.

Risk: A reused workspace identity and locally stored tokens may expose one user's historical reports to another user in a shared workspace.

Mitigation: Avoid shared workspaces until identity binding and report isolation are fixed; use a dedicated workspace in the meantime.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)
- [Plant vitality API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis or Markdown report and historical report table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a 0–100 vitality score, grade, available trend, and report links; a single image cannot establish a trend.]

## Skill Version(s):

1.0.14 (source: ClawHub server-resolved release; bundled SKILL.md states 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

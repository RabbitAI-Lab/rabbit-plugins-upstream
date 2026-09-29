## Description:

Analyzes plant images or videos to report a 0–100 vitality score and, when sufficient observations are available, a trend in plant health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners and plant-monitoring teams use this skill to assess plant vitality from images or video, review changes over time, and retrieve prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images or videos, report history, and an internal account identifier may be sent to the Life Emergence cloud service.

Mitigation: Use only when this data transfer is acceptable and review the service's handling of uploaded data and reports.

Risk: Automatically managed identity, locally stored tokens, and account-linked history may expose reports in shared environments.

Mitigation: Review account authentication and the local token database location before enabling history lookup or shared use.

## Reference(s):

- [Plant Vitality Index API reference](references/api_doc.md)
- [Skill usage demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured report or Markdown history table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a report to a file; a single image may not support a trend.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

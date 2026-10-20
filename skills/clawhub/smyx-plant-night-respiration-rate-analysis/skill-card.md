## Description:

Analyzes nighttime plant-canopy thermal imagery, with optional CO₂ data, to estimate relative respiration intensity and provide a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and plant-factory operators use nighttime thermal imagery to assess relative plant respiration and review reports or historical results. The estimates are for research or cultivation guidance, not a substitute for agricultural instrument measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files and URLs are processed by a remote service.

Mitigation: Use only non-sensitive plant imagery and confirm the publisher's cloud service and retention practices are acceptable before installing.

Risk: A default identity may be silently created or reused, and authentication tokens are stored in a local workspace database.

Mitigation: Review identity and local token storage behavior before use; restrict access to the workspace and avoid shared or sensitive environments.

Risk: Historical reports are retrieved from the cloud.

Mitigation: Query history only when cloud report access and retention are acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table; optional saved report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include relative intensity, assessments, recommendations, and report links.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

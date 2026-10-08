## Description:

Estimates relative nighttime plant respiration from canopy thermal imagery, with optional environmental CO₂ data, and provides activity assessments and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse and plant-factory operators use this skill to assess relative nighttime respiration from canopy thermal images or video, review activity alerts and environmental recommendations, and retrieve past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or submitted URLs are sent to an external analysis service.

Mitigation: Submit only appropriate plant imagery and non-sensitive URLs after reviewing the service's data-handling practices.

Risk: The skill silently creates or reuses a local service identity and stores authentication tokens in the workspace data directory.

Mitigation: Use a workspace whose users and retention practices you trust, and review stored credentials before sharing or reusing it.

## Reference(s):

- [Skill listing on ClawHub](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)
- [Plant respiration API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown analysis reports and report links; JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relative respiration index (0–100%), activity assessment, alerts and recommendations; historical reports as a Markdown table.]

## Skill Version(s):

1.0.10 (source: server-resolved release; artifact frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

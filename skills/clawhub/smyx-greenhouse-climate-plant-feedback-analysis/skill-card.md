## Description:

Using fixed cameras in a smart greenhouse to analyze plant morphology in real time, combine those observations with environmental sensor data, and output climate-control actions such as irrigation, shading, ventilation, wet-curtain operation, and heating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse operators, agritech developers, and automation engineers use this skill to analyze greenhouse plant images or videos with optional sensor context and produce structured plant-state feedback, climate-control action guidance, priorities, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends greenhouse images, videos, and account-linked report requests to configured smyx/lifeemergence backend services.

Mitigation: Review the configured endpoints before use and avoid sensitive facility footage unless the backend and data handling are approved.

Risk: The packaged defaults select development private-network HTTP endpoints, which may be unsuitable or unreachable in a production deployment.

Mitigation: Replace default development endpoints with approved production endpoints before installing or running the skill.

Risk: Automatic identity setup and local token persistence may associate report history with locally stored identity or token data.

Mitigation: Verify local identity and token storage behavior, restrict access to the runtime environment, and clear stored credentials when rotating users or deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Greenhouse API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON]

**Output Format:** [Markdown and structured JSON analysis reports with control-action recommendations and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include priority labels for recommended actions and links to cloud-hosted historical reports.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

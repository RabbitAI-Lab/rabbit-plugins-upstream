## Description:

Analyzes greenhouse plant images or videos with optional environmental sensor context to produce structured plant-stress findings, climate-control action recommendations, report links, and historical report listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, greenhouse operators, and automation teams use this skill to analyze crop canopy media and optional sensor context, then obtain prioritized irrigation, shading, ventilation, wet-curtain, or heating recommendations. It can also retrieve prior greenhouse-control analysis reports from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Greenhouse images, videos, and history lookup requests may be sent to lifeemergence/open.lifeemergence services.

Mitigation: Review the service endpoints and data-sharing expectations before installation, and avoid submitting confidential greenhouse media unless the deployment has approved those external services.

Risk: The skill may create or reuse a local user identity, register or log in with the external service, and persist authentication tokens in workspace data.

Mitigation: Install in a controlled workspace, inspect and rotate stored credentials as needed, and limit access to the workspace data database.

Risk: Generated climate-control recommendations could be wrong or incomplete for local equipment and crop conditions.

Mitigation: Treat outputs as decision support and require local controller safeguards or operator review before actuating irrigation, shading, ventilation, wet-curtain, or heating systems.

## Reference(s):

- [Greenhouse climate plant feedback API documentation](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, API calls, guidance]

**Output Format:** [Markdown or JSON-like structured text containing analysis results, recommendations, report links, and history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prioritized climate-control commands and cloud report export URLs; does not provide PID values or exact actuator opening percentages.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

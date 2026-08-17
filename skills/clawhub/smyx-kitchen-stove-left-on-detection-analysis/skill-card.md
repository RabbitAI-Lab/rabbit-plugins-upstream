## Description:

Analyzes fixed kitchen stove-area camera video to identify unattended stove-on conditions and return structured alerts, reports, and history-query results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, senior-care operators, and smart-home integrators use this skill to analyze kitchen stove-area video or video URLs for unattended flame or heat conditions and to review cloud-stored kitchen safety reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kitchen video or video URLs may be sent to the configured cloud service.

Mitigation: Use only with consent from monitored people and only with video sources appropriate for remote processing.

Risk: The skill can query report history remotely.

Mitigation: Limit installation and use to workspaces where remote history lookup is expected and authorized.

Risk: The skill may create or reuse an identity and store account tokens.

Mitigation: Protect the workspace data directory and review identity and token handling before deployment.

Risk: The skill describes possible smart gas-valve automation for unattended stove alerts.

Mitigation: Do not connect real gas-valve automation unless a separate explicit safety interlock and opt-in flow are in place.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-kitchen-stove-left-on-detection-analysis)
- [API 接口文档](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown text and JSON-style structured report content, with optional saved text output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud history tables; analysis depends on configured remote APIs.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

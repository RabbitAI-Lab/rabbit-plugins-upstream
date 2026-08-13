## Description:

Build, modify, or troubleshoot Sentio projects across processors, Sentio SQL in Data Studio, alerting, and dashboards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[philz3906](https://clawhub.ai/user/philz3906)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Sentio projects, query Sentio data, configure alerts and endpoints, and create or update dashboards with the Sentio CLI and API schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad changes to Sentio projects, including delete, pause, stop, import, and public-sharing operations.

Mitigation: Require explicit user confirmation and verify the target project before destructive, state-changing, import, or public-sharing actions.

Risk: The skill may involve Sentio API keys or bearer tokens for CLI authentication.

Mitigation: Use least-privilege credentials and avoid placing long-lived secrets in chat messages, shell history, or command arguments.

Risk: The security verdict is suspicious because the skill has broad authority and limited safety guidance.

Mitigation: Review the skill before installing it for production or sensitive Sentio projects, and scan generated commands before execution.

## Reference(s):

- [Sentio OpenAPI Swagger](references/openapi.swagger.json)
- [ClawHub skill page](https://clawhub.ai/philz3906/skills/sentio-platform)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that query or modify Sentio projects and dashboards.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

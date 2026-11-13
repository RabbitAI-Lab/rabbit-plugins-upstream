## Description:

Build, modify, or troubleshoot Sentio projects across processors, Sentio SQL in Data Studio, alerting, and dashboards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sentioxyz](https://clawhub.ai/user/sentioxyz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Sentio projects, processors, SQL/data queries, alerts, endpoints, dashboards, price data, and transaction simulations through the Sentio CLI and related API schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live Sentio administration tasks that affect projects, processors, alerts, endpoints, dashboards, SQL sharing, simulations, and account links.

Mitigation: Require explicit user confirmation before deletes, processor activation, pause or stop actions, public SQL sharing, and account-link changes; preview the target project and command before execution.

Risk: The skill may involve Sentio API keys or bearer tokens.

Mitigation: Use narrowly scoped credentials, avoid pasting secrets into chat or command lines, prefer safer login or secret handling mechanisms when available, and rotate credentials after use.

Risk: Using an unpinned Sentio CLI can change behavior across runs.

Mitigation: Pin the Sentio CLI version for repeatable production workflows and review command output before applying changes.

## Reference(s):

- [Sentio Platform Skill Page](https://clawhub.ai/sentioxyz/skills/sentio-platform)
- [Sentio OpenAPI Swagger Reference](references/openapi.swagger.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that operate on live Sentio projects and require user-provided credentials.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

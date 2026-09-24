## Description:

PlanetScale CLI command reference and workflows for authentication, organization and billing operations, databases, branches, deploy requests, SQL, metrics, insights, backups, webhooks, audit logs, service tokens, D1 imports, and related automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan, compose, run, and interpret PlanetScale pscale CLI commands and bundled shell workflows. It supports operational tasks such as branch management, schema deployment, service-token setup, billing inspection, webhooks, diagnostics, metrics, and backup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide sensitive PlanetScale administrative changes, including billing, organization membership, credentials, webhooks, database changes, and schema deployment.

Mitigation: Use scoped credentials and review the exact organization, database, branch, and command targets before any write operation.

Risk: Some workflows can create or expose secrets, including service tokens, webhook signing secrets, authorization headers, and database credentials.

Mitigation: Keep generated secrets out of chat, logs, tickets, and repositories; capture them only through approved secret-management paths.

Risk: Operational commands may affect availability, billing state, access, or production schema behavior.

Mitigation: Prefer read-only inspection first, require explicit approval for destructive or availability-impacting actions, and verify results after execution.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI Documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI Repository](https://github.com/planetscale/cli)
- [PlanetScale Discussion Repository](https://github.com/planetscale/discussion)
- [PlanetScale Webhook API Reference](https://planetscale.com/docs/api/reference/create_webhook)
- [PlanetScale Webhook Events Reference](https://planetscale.com/docs/api/webhook-events)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, command references, workflow steps, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce pscale CLI command sequences, JSON-oriented inspection guidance, and shell script usage recommendations.]

## Skill Version(s):

1.0.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

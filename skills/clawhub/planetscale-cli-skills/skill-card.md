## Description:

Provides PlanetScale CLI command references, safety guidance, and automation workflows for managing PlanetScale databases, branches, deploy requests, SQL, metrics, billing, webhooks, tokens, and organization operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database operators, and platform engineers use this skill to plan and execute PlanetScale pscale CLI workflows while reviewing high-impact database, billing, credential, and organization changes before approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers high-impact database and billing workflows, including deletion, deploys, SQL writes, payment-method changes, and audit-log exports.

Mitigation: Review the exact pscale command, target organization, database, branch, and expected effect before approval; use the skill's confirmation and read-back guidance for destructive or sensitive actions.

Risk: Webhook secrets, service tokens, passwords, and authorization headers can be exposed through command arguments or captured output.

Mitigation: Keep credentials in environment variables or an approved secret manager, avoid logging secret-bearing output, and redact webhook secret fields before sharing or persisting command results.

Risk: Automation can act on misleading successful exit codes or incomplete command output.

Mitigation: Validate expected JSON/resource shapes in addition to exit status, and branch on preserved API error codes when available.

## Reference(s):

- [PlanetScale CLI Skills overview](artifact/SKILL.md)
- [Release and version notes](artifact/VERSION)
- [PlanetScale CLI reference](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale create webhook API reference](https://planetscale.com/docs/api/reference/create_webhook)
- [PlanetScale webhook events reference](https://planetscale.com/docs/api/webhook-events)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and script references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local pscale CLI installation and, for structured automation workflows, jq.]

## Skill Version(s):

1.0.25 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

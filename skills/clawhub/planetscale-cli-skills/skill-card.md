## Description:

PlanetScale CLI (pscale) command reference and workflows for database administration, schema changes, diagnostics, metrics, billing, webhooks, imports, and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan and run PlanetScale CLI workflows, interpret pscale output, and apply guarded automation for schema, branch, organization, billing, metrics, webhook, import, backup, and credential tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide sensitive PlanetScale administrative changes across organizations, databases, branches, billing, webhooks, credentials, imports, backups, and deploy requests.

Mitigation: Review the exact organization, database, branch, resource ID, and command flags before approving any write or destructive operation.

Risk: pscale tokens, connection URLs, webhook secrets, invoices, and audit exports can expose secrets or sensitive business data.

Mitigation: Keep credentials in the PlanetScale CLI, environment variables, or a secret manager; redact secret-bearing output before sharing it in chat or logs.

Risk: Automation that trusts only a zero exit code can misread help output or failed resource targeting as a successful operation.

Mitigation: Validate expected JSON shape, resource identity, and API error codes before continuing automated workflows.

## Reference(s):

- [PlanetScale CLI reference](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub repository](https://github.com/planetscale/cli)
- [PlanetScale webhook create API reference](https://planetscale.com/docs/api/reference/create_webhook)
- [PlanetScale webhook events reference](https://planetscale.com/docs/api/webhook-events)
- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration notes, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pscale CLI invocations, jq examples, approval gates for write operations, and redaction guidance for sensitive outputs.]

## Skill Version(s):

1.0.23 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

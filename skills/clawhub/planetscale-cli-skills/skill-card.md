## Description:

Provides PlanetScale CLI (pscale) command references, workflows, and automation guidance for database, branch, deployment, operational, billing, organization, and security-related tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan and execute PlanetScale pscale CLI workflows, including schema migration, branch management, diagnostics, billing review, organization administration, and controlled automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact database, billing, credential, webhook, organization, SQL write, or deletion operations through the PlanetScale CLI.

Mitigation: Require explicit user approval before running commands that modify resources, affect billing or credentials, expose webhook secrets, change organization settings, perform SQL writes, or delete data.

Risk: PlanetScale service tokens, webhook secrets, billing records, audit exports, and database outputs may contain sensitive information.

Mitigation: Keep secrets and exported audit, billing, and database data out of chat transcripts and logs; redact sensitive fields before sharing command output.

## Reference(s):

- [PlanetScale CLI Skills on ClawHub](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI Reference](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI Repository](https://github.com/planetscale/cli)
- [PlanetScale Webhook API Reference](https://planetscale.com/docs/api/reference/create_webhook)
- [PlanetScale Webhook Events](https://planetscale.com/docs/api/webhook-events)
- [Branch Command Reference](artifact/pscale-branch/references/commands.md)
- [Deploy Request Command Reference](artifact/pscale-deploy-request/references/commands.md)
- [Database Command Reference](artifact/pscale-database/references/commands.md)
- [SQL Command Reference](artifact/pscale-sql/references/commands.md)
- [Organization Command Reference](artifact/pscale-org/references/commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, JSON-oriented pscale examples, and script recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the pscale CLI; jq is required for bundled automation scripts; optional PlanetScale service token environment variables may be used for CI/CD.]

## Skill Version(s):

1.0.27 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

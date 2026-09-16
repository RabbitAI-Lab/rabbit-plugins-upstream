## Description:

PlanetScale CLI Skills helps agents use pscale command references and guarded workflows for PlanetScale authentication, organizations, databases, branches, deploy requests, SQL, metrics, billing, webhooks, credentials, and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they want an agent to propose, interpret, or run PlanetScale CLI workflows for database operations, schema migration, diagnostics, billing, access management, and CI/CD automation. It is intended for users who already have appropriate PlanetScale CLI access and need command guidance with operational safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide powerful PlanetScale operations that affect databases, billing, organizations, service tokens, webhooks, and SQL execution.

Mitigation: Use least-privileged PlanetScale credentials, confirm the exact organization, database, and branch before writes, and require explicit approval for deploys, deletes, billing or organization changes, service-token operations, webhooks, and destructive SQL.

Risk: Operational outputs can expose sensitive tokens, webhook secrets, invoices, audit exports, or credential metadata if captured carelessly.

Mitigation: Keep secrets and sensitive exports out of chat and logs, use environment variables or an approved secret store, and redact sensitive CLI output before sharing it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI Documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI Repository](https://github.com/planetscale/cli)
- [Root Skill Definition](artifact/SKILL.md)
- [Branch Commands](artifact/pscale-branch/references/commands.md)
- [Database Commands](artifact/pscale-database/references/commands.md)
- [Deploy Request Commands](artifact/pscale-deploy-request/references/commands.md)
- [SQL Commands](artifact/pscale-sql/references/commands.md)
- [Organization Commands](artifact/pscale-org/references/commands.md)
- [Webhook Commands](artifact/pscale-webhook/references/commands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pscale command proposals, JSON-output interpretation, and approval-oriented safety checks.]

## Skill Version(s):

1.0.26 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

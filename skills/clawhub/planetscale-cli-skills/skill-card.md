## Description:

PlanetScale CLI (pscale) command reference and workflows for authentication, organizations, databases, branches, maintenance, metrics, insights, diagnostics, SQL, deploy requests, schema migrations, keyspaces, PgBouncers, backups, audit logs, service tokens, passwords, Cloudflare D1 imports, and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan, review, and run PlanetScale CLI workflows for database administration, schema deployment, diagnostics, metrics, backups, audit-log export, service tokens, and related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact PlanetScale database operations, including deploy, delete, force, credential, routing, throttler, backup, and other production-impacting actions.

Mitigation: Keep command execution approval enabled, verify organization, database, and branch names before writes, and require explicit user confirmation for production-impacting operations.

Risk: Authentication material, service tokens, audit-log exports, and database access details may be sensitive.

Mitigation: Keep credentials in environment variables or approved secret storage, avoid printing secrets or raw export archives in logs, and write exported data only to approved paths.

Risk: Automation scripts create branches and deploy requests, and one script can deploy a schema change when explicitly invoked with its deploy option.

Mitigation: Review script arguments before execution, prefer JSON output for machine parsing, inspect diffs and deploy-request status before deployment, and use least-privilege PlanetScale credentials.

## Reference(s):

- [PlanetScale CLI Reference](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub Repository](https://github.com/planetscale/cli)
- [PlanetScale Discussion](https://github.com/planetscale/discussion)
- [Bundled PlanetScale Command References](artifact/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-aware command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute bundled bash scripts or pscale commands when command execution is approved; scripts use jq for structure-aware parsing of pscale JSON output.]

## Skill Version(s):

1.0.15 (source: server release metadata and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

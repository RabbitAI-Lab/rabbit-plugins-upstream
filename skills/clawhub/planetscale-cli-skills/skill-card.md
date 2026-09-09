## Description:

Provides PlanetScale CLI command references, guarded workflows, and shell automation for managing databases, branches, deploy requests, metrics, billing, access controls, webhooks, backups, and related operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database operators, and platform engineers use this skill to plan and execute PlanetScale CLI workflows, inspect CLI output, and generate guarded shell commands or scripts for PlanetScale operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact PlanetScale operations that affect production databases, deploys, billing, SSO, members, webhooks, passwords, service tokens, and access controls.

Mitigation: Require explicit human approval after showing the exact organization, database, branch, resource ID, command, and expected impact before any create, update, delete, deploy, promote, --force, write SQL, billing, SSO, member, webhook, password, or service-token action.

Risk: CLI output can include sensitive credentials, webhook secrets, passwords, billing details, or access-control data.

Mitigation: Keep secrets in environment variables or a secret manager, avoid raw sensitive output in logs or chat, and redact billing, webhook, password, and token details before sharing.

Risk: Operational write commands can be more disruptive than intended when run against the wrong PlanetScale target.

Mitigation: Prefer read-only inspection commands first and verify target identifiers and expected effects before proposing or running write operations.

## Reference(s):

- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI repository](https://github.com/planetscale/cli)
- [PlanetScale create webhook API reference](https://planetscale.com/docs/api/reference/create_webhook)
- [PlanetScale webhook events documentation](https://planetscale.com/docs/api/webhook-events)
- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [Skill source overview](artifact/SKILL.md)
- [Skill release notes](artifact/VERSION)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON-oriented CLI examples, and bash scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the PlanetScale CLI and jq; may depend on PlanetScale authentication or optional service-token environment variables.]

## Skill Version(s):

1.0.22 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

PlanetScale CLI (pscale) command reference and workflows for managing authentication, organizations, databases, branches, deploy requests, SQL, metrics, backups, webhooks, billing, service tokens, passwords, and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database operators, and release engineers use this skill to select and run PlanetScale CLI workflows for database, branch, deploy, billing, organization, credential, monitoring, and migration tasks. It helps agents produce command guidance, shell commands, and safety checks for pscale-based operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide sensitive PlanetScale database, billing, credential, organization, deploy, restore, import, and topology changes.

Mitigation: Require explicit human approval after the agent restates the organization, database, branch or resource ID, expected impact, and rollback or verification plan.

Risk: Deletion and --force workflows may remove branches, policies, payment methods, webhooks, or other resources when the target is wrong.

Mitigation: Confirm the exact resource identifier and intended destructive effect before execution, avoid --force unless explicitly authorized, and verify state afterward.

Risk: Credential, service-token, password, webhook, and API-header workflows can expose secrets through logs, command output, or committed configuration.

Mitigation: Keep credentials in environment variables or secret managers, redact secret-bearing output, and avoid storing API URLs or tokens in repository-local configuration.

## Reference(s):

- [PlanetScale CLI Skills on ClawHub](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub repository](https://github.com/planetscale/cli)
- [Artifact root skill](artifact/SKILL.md)
- [Artifact version and release notes](artifact/VERSION)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration notes, and operational checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pscale CLI commands, jq filters, script usage, and approval gates before sensitive operations.]

## Skill Version(s):

1.0.23 (source: evidence.release.version and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

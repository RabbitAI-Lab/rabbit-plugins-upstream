## Description:

Chat-based Azure infrastructure assistance using Azure CLI and portal context. Use for querying, auditing, and monitoring Azure resources (VMs, Storage, IAM, Functions, AKS, App Service, Key Vault, Azure Monitor, billing, etc.), and for proposing safe changes with explicit confirmation before any write/destructive action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bmdhodl](https://clawhub.ai/user/bmdhodl)

### License/Terms of Use:


## Use Case:

Developers, cloud engineers, and operators use this skill to inspect Azure resources through a local Azure CLI session, audit common infrastructure and security areas, monitor health and cost signals, and prepare safe command proposals for changes that require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can propose Azure CLI commands that affect real cloud resources if executed in the user's active session.

Mitigation: Review each command before execution, confirm the intended subscription or tenant, and require explicit confirmation for resource, IAM, billing, credential, or deletion changes.

Risk: Azure inspection may expose sensitive operational details or secrets from the local environment.

Mitigation: Use the skill only with intended Azure accounts and avoid revealing or logging keys, client secrets, tokens, or credential values.

## Reference(s):

- [Azure CLI Query Patterns](references/azure-cli-queries.md)
- [ClawHub Skill Page](https://clawhub.ai/bmdhodl/skills/azure-infra)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline Azure CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first operational guidance; write or destructive command proposals require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Operate and manage Docker Compose stacks on VPS infrastructure with the strut CLI. Use for any strut task — deploying and releasing services, database backup and restore, debugging production issues, detecting config drift, rotating secrets and keys, setting up monitoring, configuring domains and SSL, validating stacks, or auditing and migrating existing servers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gfargo](https://clawhub.ai/user/gfargo)

### License/Terms of Use:

MIT

## Use Case:

Developers and server operators use strut to deploy, monitor, troubleshoot, back up, validate, and migrate Docker Compose services on VPS infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review identifies host-mounted monitoring setup and unpinned container images as risks.

Mitigation: Review monitoring mounts and image sources before deployment; avoid host mounts when they are not needed and pin images where practical.

Risk: Some commands and examples may expose secrets or production data.

Mitigation: Inspect commands before running them, keep secrets out of logs and shared output, and use non-production data for examples and rehearsals.

Risk: The security review was incomplete, so not every referenced item was fully reviewed.

Mitigation: Review the relevant source files and commands before installing or using the skill on a live host.

## Reference(s):

- [Server-resolved source repository](https://github.com/gfargo/skills/tree/main/plugins/devops/skills/strut)
- [ClawHub release page](https://clawhub.ai/gfargo/skills/strut)
- [Deployment](artifact/references/deployment.md)
- [Debugging](artifact/references/debugging.md)
- [Database backups and restore](artifact/references/backups.md)
- [Drift detection](artifact/references/drift.md)
- [Secrets and key rotation](artifact/references/secrets.md)
- [Monitoring setup](artifact/references/monitoring.md)
- [Domain and SSL configuration](artifact/references/domains-ssl.md)
- [Stack validation](artifact/references/validation.md)
- [VPS audit and migration](artifact/references/migration.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Operational guidance]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes actions that can affect remote VPS services and production data.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; SKILL.md frontmatter lists 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

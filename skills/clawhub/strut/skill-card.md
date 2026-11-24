## Description:

Operate and manage Docker Compose stacks on VPS infrastructure with the strut CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gfargo](https://clawhub.ai/user/gfargo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to deploy, inspect, and maintain Docker Compose services on VPS hosts, including backups, troubleshooting, drift management, secrets, monitoring, domains, validation, and migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious due to automatic production configuration changes and a production backup step without adequate warning; two referenced files were only partially inspected, leaving incomplete evidence.

Mitigation: Review the automatic drift-fix behavior and production backup step before installing, and consider whether you need these features.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gfargo/skills/strut)
- [Server-resolved source repository and path](https://github.com/gfargo/strut/tree/main/skills/strut)
- [Database Backups & Restore](artifact/references/backups.md)
- [Debugging](artifact/references/debugging.md)
- [Deployment](artifact/references/deployment.md)
- [Domain & SSL Configuration](artifact/references/domains-ssl.md)
- [Drift Detection & Auto-Fix](artifact/references/drift.md)
- [VPS Audit & Migration](artifact/references/migration.md)
- [Monitoring Setup](artifact/references/monitoring.md)
- [Secrets & Key Rotation](artifact/references/secrets.md)
- [Stack Validation](artifact/references/validation.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Operational guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and guidance may target a local Docker daemon or a remote VPS.]

## Skill Version(s):

0.1.5 (source: server-resolved ClawHub release; skill frontmatter version: 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Provides an agent-facing workflow for searching and reading Venafi TLS Protect Datacenter data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect connector schemas and run read-oriented Venafi TLS Protect Datacenter actions for policy checks and certificate lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connector access may expose certificate-management data visible to the connected OOMOL account.

Mitigation: Confirm the intended OOMOL account, connection, and Venafi TLS Protect Datacenter scope before installation and limit use to authorized certificate lookups.

Risk: Malformed or stale connector payloads can fail or target the wrong action contract.

Mitigation: Fetch the live connector schema before each action and build JSON payloads from that schema.

Risk: Future write or destructive actions, if added, could change or remove certificate-management data.

Mitigation: Require explicit user confirmation for any action tagged write or destructive before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-venafitlsprotectdatacenter)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [CyberArk Certificate Manager Self-Hosted](https://www.cyberark.com/resources/product-datasheets/cyberark-certificate-manager-self-hosted)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

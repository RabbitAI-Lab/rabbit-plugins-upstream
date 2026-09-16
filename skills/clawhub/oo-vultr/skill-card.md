## Description:

Manage Vultr resources through an OOMOL-connected oo CLI workflow for reading, creating, updating, and deleting account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Vultr account resources through an OOMOL-connected oo CLI workflow, including VPS instances, DNS domains and records, regions, plans, operating systems, snapshots, firewall groups, account details, and power operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup can pipe remote installer scripts directly into a shell.

Mitigation: Install the oo CLI through a signed, versioned, or checksum-verified release path before using the skill.

Risk: Write and destructive Vultr actions can change or delete cloud resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-vultr)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Vultr Homepage](https://www.vultr.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before running oo CLI actions and to request confirmation for write or destructive Vultr operations.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

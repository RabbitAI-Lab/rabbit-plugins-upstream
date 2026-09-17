## Description:

Use this skill for Vultr (vultr.com) requests, including reading, creating, updating, and deleting resources through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Vultr account resources, VPS instances, DNS, snapshots, plans, regions, and firewall groups through an OOMOL-connected CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path recommends running a remote installer that can execute local code.

Mitigation: Review the installer path before use, prefer a verified OOMOL CLI package, or independently inspect and verify the installer before running it.

Risk: Write and destructive Vultr actions can change or permanently delete account resources.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before write or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-vultr)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Vultr Homepage](https://www.vultr.com/)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

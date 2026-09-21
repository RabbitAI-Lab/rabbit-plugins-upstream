## Description:

Provides agent access to Vultr account operations through OOMOL's oo CLI connector, including reading, creating, updating, deleting, and power-managing cloud resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and external users use this skill to manage Vultr resources through an OOMOL-connected account. It supports account lookup, resource discovery, VPS lifecycle operations, power management, firewall and DNS listing, and billing summary lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide installation of the oo CLI through remote pipe-to-shell commands.

Mitigation: Prefer a verified manual installation process before using the skill.

Risk: The skill can modify, power-manage, or delete Vultr cloud resources.

Mitigation: Require exact confirmation of the target, payload, and expected effect before write or destructive actions.

Risk: The skill depends on trusting OOMOL-mediated Vultr operations.

Mitigation: Review the skill before installation and connect the least-privilege Vultr credential that supports the intended tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vultr)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vultr homepage](https://www.vultr.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command execution uses the oo CLI and returns JSON when the skill's documented --json flag is used.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

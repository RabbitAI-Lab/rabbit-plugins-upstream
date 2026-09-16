## Description:

Enables agents to inspect and manage DigitalOcean resources through the OOMOL digital_ocean connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query DigitalOcean account, Droplet, App Platform, database, DNS, firewall, load balancer, and VPC information, and to initiate Droplet lifecycle actions through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Droplet lifecycle actions can change service state through reboot, shutdown, or power-cycle operations.

Mitigation: Require explicit user confirmation of the target Droplet, action, and payload before running lifecycle operations.

Risk: One-line remote installer commands can execute unverified installer content.

Mitigation: Prefer a safer download-and-review installation process before executing installer scripts.

## Reference(s):

- [ClawHub DigitalOcean Skill](https://clawhub.ai/oomol/skills/oo-digital-ocean)
- [DigitalOcean Homepage](https://www.digitalocean.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the user to have oo CLI authentication and a connected DigitalOcean account; action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

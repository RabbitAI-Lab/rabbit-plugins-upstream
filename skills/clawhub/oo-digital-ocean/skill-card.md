## Description:

DigitalOcean helps agents use OOMOL's digital_ocean connector through the oo CLI to read DigitalOcean resources and manage Droplet lifecycle actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect DigitalOcean account, Droplet, App Platform, database, DNS, firewall, load balancer, and VPC resources through an OOMOL-connected account. They may also run Droplet lifecycle actions after confirming the target and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DigitalOcean requests are routed through OOMOL-connected infrastructure.

Mitigation: Install only if that routing is acceptable and connect a least-privilege DigitalOcean credential.

Risk: Droplet lifecycle actions such as reboot, shutdown, and power cycle can change running infrastructure state.

Mitigation: Require explicit confirmation of the target Droplet and lifecycle action before execution.

Risk: The setup guidance includes remote installer commands that execute shell or PowerShell scripts.

Mitigation: Independently trust and verify installer scripts before running pipe-to-shell commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-digital-ocean)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [DigitalOcean](https://www.digitalocean.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; read actions return JSON through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

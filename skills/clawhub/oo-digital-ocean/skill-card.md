## Description:

DigitalOcean (digitalocean.com). Use this skill for any DigitalOcean request, including reading, creating, updating, and deleting data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect DigitalOcean account and team context and manage core DigitalOcean resources through an OOMOL-connected account. It supports inventory queries for Droplets, Apps, databases, DNS, firewalls, load balancers, and VPCs, plus guarded Droplet lifecycle actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote CLI installer commands can execute code during first-time setup if used without inspection.

Mitigation: Install the oo CLI only when required, prefer a verified or inspected installation method, and avoid piping remote installer output directly into a shell where possible.

Risk: Droplet lifecycle actions can interrupt running infrastructure.

Mitigation: Confirm the target Droplet ID, payload, and intended effect with the user before running actions tagged destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-digital-ocean)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [DigitalOcean Homepage](https://www.digitalocean.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

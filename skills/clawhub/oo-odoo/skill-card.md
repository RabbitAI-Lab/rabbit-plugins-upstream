## Description:

Helps agents read and manage Odoo records through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and developers can inspect, search, create, update, and delete Odoo records through a connected account, with confirmation before changes to business data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running unverified remote installer scripts.

Mitigation: Do not run the installer automatically; use a verified installation method where possible.

Risk: Odoo create, update, method calls, and delete actions can change or remove business data.

Mitigation: Require explicit approval of the exact payload and target before these actions, especially in production.

## Reference(s):

- [Odoo skill on ClawHub](https://clawhub.ai/oomol/skills/oo-odoo)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Odoo](https://www.odoo.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain-language guidance and JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action results include an execution ID.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

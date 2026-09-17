## Description:

OpenStatus connector for reading, creating, updating, deleting, listing, and checking OpenStatus monitors through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage OpenStatus monitors and retrieve status, metrics, response logs, and on-demand check results from an OOMOL-connected OpenStatus account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run remote installer scripts directly.

Mitigation: Review installer steps before installing, prefer a verifiable package or checked download, and inspect the installer before running it.

Risk: Write and destructive OpenStatus actions can change or remove monitor data.

Mitigation: Confirm the exact payload, target monitor, and expected effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub OpenStatus Skill Page](https://clawhub.ai/oomol/skills/oo-openstatus)
- [OpenStatus Homepage](https://www.openstatus.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

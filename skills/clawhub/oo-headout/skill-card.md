## Description:

Headout (headout.com). Use this skill for searching and reading Headout data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Headout cities, categories, products, variants, inventory, and accessible bookings through the OOMOL Headout connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask the user or agent to execute remote installer scripts directly in a shell.

Mitigation: Review setup commands before installation, prefer verified or checksum-pinned installers, and avoid elevated sessions unless the installer has been independently verified.

Risk: The skill can read booking, product, city, category, and inventory data available to the connected OOMOL account.

Mitigation: Use an account with only the needed Headout access and review command payloads before running connector actions.

## Reference(s):

- [Headout ClawHub skill page](https://clawhub.ai/oomol/skills/oo-headout)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Headout homepage](https://www.headout.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to fetch live action schemas before sending Headout connector requests.]

## Skill Version(s):

1.0.3 (source: evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

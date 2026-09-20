## Description:

Precoro (precoro.com). Use this skill for ANY Precoro request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to read Precoro purchasing data through an OOMOL-connected Precoro account, including catalog items, purchase orders, suppliers, users, and warehouses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installer commands that users should treat carefully before running.

Mitigation: Confirm OOMOL is trusted and prefer the official install guide or a verified installer before executing installation commands.

Risk: The skill can read Precoro business data visible to the connected account.

Mitigation: Use a connected account with appropriate Precoro permissions and review returned business data before sharing it.

## Reference(s):

- [ClawHub Precoro skill page](https://clawhub.ai/oomol/skills/oo-precoro)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Precoro homepage](https://precoro.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Precoro connector actions return data and execution metadata from the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

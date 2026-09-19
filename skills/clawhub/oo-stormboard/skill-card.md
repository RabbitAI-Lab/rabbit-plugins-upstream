## Description:

Stormboard connector skill for searching and reading Stormboard data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Stormboard profiles, Storms, access levels, participants, tags, ideas, connectors, templates, and template categories through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified pipe-to-shell installer commands.

Mitigation: Review the setup path before installing, and prefer a pinned, verifiable oo CLI release or package manager when available.

Risk: The skill can read Stormboard content visible to the connected account.

Mitigation: Confirm the intended OOMOL and Stormboard accounts before running connector actions.

## Reference(s):

- [Stormboard Homepage](https://stormboard.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Stormboard action schemas before connector calls; credentials remain server-side through OOMOL.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

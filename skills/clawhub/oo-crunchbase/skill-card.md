## Description:

Crunchbase (crunchbase.com). Use this skill for searching and reading Crunchbase data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Crunchbase and retrieve organization, acquisition, and IPO records through an OOMOL-connected Crunchbase account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may run remote installer scripts directly in a shell.

Mitigation: Download and inspect the installer first, verify a checksum or signature from OOMOL when available, and avoid running installer commands automatically or from an elevated session.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-crunchbase)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Crunchbase](https://www.crunchbase.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Use 1Password through an OOMOL-connected account to inspect connector schemas and retrieve vault, item, activity, and health information via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to satisfy 1Password requests by querying vaults, item details, activity events, and service health through an OOMOL-connected 1Password account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 1Password request details and retrieved item contents are routed through OOMOL.

Mitigation: Install only if that routing is acceptable, use a least-privileged 1Password Connect token limited to required vaults, and avoid retrieving full item contents unless necessary.

Risk: First-time setup guidance includes remote installer commands that pipe scripts into a shell.

Mitigation: Verify the installer source and integrity separately before running remote shell installation commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-one-password)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [1Password Homepage](https://1password.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and execution metadata when run with --json.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

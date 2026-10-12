## Description:

Helps agents access OOMOL Console account and team information and manage team members and Connection permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

OOMOL Console users can inspect account billing and usage, review teams and Connections, and request changes to team membership or Connection permissions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup suggests running a remote installer directly in a shell.

Mitigation: Do not run the installer automatically; install the oo CLI through a trusted, verified channel after review.

Risk: Membership and Connection permission changes may alter or remove access.

Mitigation: Confirm the exact target and effect with the user before write actions, and obtain explicit approval for destructive actions.

## Reference(s):

- [OOMOL Console skill on ClawHub](https://clawhub.ai/oomol/skills/oo-oomol-console)
- [OOMOL Console](https://console.oomol.com)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [oo CLI project](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and Markdown with CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account and team results depend on the authenticated user's access.]

## Skill Version(s):

1.0.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

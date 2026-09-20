## Description:

Positionstack connector skill for forward and reverse geocoding through an OOMOL-connected Positionstack account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Positionstack forward and reverse geocoding through an OOMOL-connected account without handling raw Positionstack API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review the setup path before installing, and prefer verified official documentation with version or integrity checks before running installer commands.

Risk: The skill can use an OOMOL-connected Positionstack account after authentication and connection setup.

Mitigation: Only sign in or connect Positionstack when you intend this skill to use that account, and inspect the live connector schema before running an action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-positionstack)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Positionstack Homepage](https://positionstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId when execution succeeds.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

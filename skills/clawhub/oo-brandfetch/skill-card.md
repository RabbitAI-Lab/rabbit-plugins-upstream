## Description:

Brandfetch operates Brandfetch through an OOMOL-connected account to fetch brand profiles and resolve transaction labels via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Brandfetch brand profiles and resolve merchant identities from transaction labels through their OOMOL-connected Brandfetch account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands for the oo CLI.

Mitigation: Review this skill before installing, prefer a signed or package-manager installation path for the oo CLI, and avoid elevated or administrator shells.

Risk: Connector actions depend on a live OOMOL account connection and current Brandfetch action schemas.

Mitigation: Fetch the live connector schema before constructing payloads, and only run authentication or connection setup after a matching failure.

## Reference(s):

- [ClawHub Brandfetch skill](https://clawhub.ai/oomol/skills/oo-brandfetch)
- [Brandfetch homepage](https://brandfetch.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Brandfetch connector schemas through the oo CLI before running actions.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

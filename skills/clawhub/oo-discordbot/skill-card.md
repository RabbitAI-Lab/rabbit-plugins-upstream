## Description:

Helps agents read and manage Discord bot resources through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and community managers can inspect Discord bot resources and, with approval, manage messages, channels, roles, members, and moderation settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad write and destructive actions can alter or remove Discord content and settings.

Mitigation: Review the exact target and payload; require explicit approval before writes or deletions.

Risk: The setup instructions include remote installer commands that run downloaded scripts.

Mitigation: Use a verified oo CLI installation path rather than running the listed pipe-to-shell commands blindly.

## Reference(s):

- [Discord Bot skill release](https://clawhub.ai/oomol/skills/oo-discordbot)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Discord developer portal](https://discord.com/developers/applications)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and Discord action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require an OOMOL-connected Discord bot account and applicable Discord permissions.]

## Skill Version(s):

1.0.6 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

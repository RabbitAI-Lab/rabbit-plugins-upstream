## Description:

GIPHY lets agents use an OOMOL-connected GIPHY account to search and retrieve GIFs, stickers, tags, trending content, categories, random items, and phrase translations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to search GIPHY, fetch GIF or sticker data, retrieve trending categories and tags, and translate phrases into matching GIFs or stickers through an OOMOL-connected GIPHY account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that run shell or PowerShell scripts directly.

Mitigation: Review installer instructions before use and prefer independently verified, signed, or package-manager-based installation steps when available.

Risk: The skill operates through an OOMOL-connected GIPHY account.

Mitigation: Connect the account only if the user trusts OOMOL with that integration and understands the account access involved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-giphy)
- [GIPHY homepage](https://giphy.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

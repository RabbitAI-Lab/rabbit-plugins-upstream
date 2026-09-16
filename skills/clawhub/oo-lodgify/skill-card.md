## Description:

Lodgify (lodgify.com). Use this skill for ANY Lodgify request - searching and reading data. Whenever a task involves Lodgify, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Lodgify connector schemas and retrieve booking, property, room, availability, and quote data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through a verified, version-pinned, signed, or package-manager workflow before using the skill.

Risk: The connector can access Lodgify booking and property data through the user's OOMOL-connected account.

Mitigation: Confirm the Lodgify connection, account, and granted access are appropriate before running connector actions.

## Reference(s):

- [Lodgify homepage](https://www.lodgify.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include Lodgify data and a meta.executionId when commands run successfully.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

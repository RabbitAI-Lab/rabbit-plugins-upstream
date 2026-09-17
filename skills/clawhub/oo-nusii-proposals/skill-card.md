## Description:

Nusii Proposals helps agents operate a user's OOMOL-connected Nusii Proposals account for reading, creating, sending, updating, and archiving proposal data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Nusii Proposals records through an OOMOL-connected account, including account lookup, client and proposal management, template and theme discovery, and proposal sending. The skill is intended to inspect live connector schemas before action execution and to confirm write actions with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the skill before installation, avoid running curl | bash or irm | iex installers unless the OOMOL CLI installer is independently trusted and verified, and prefer signed packages, pinned releases, or checksum-verified downloads.

Risk: Write actions can create, send, update, or archive proposal and client data in the connected Nusii account.

Mitigation: Inspect the live connector schema before constructing payloads and confirm the exact payload and effect with the user before executing write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-nusii-proposals)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Nusii Proposals Homepage](https://nusii.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

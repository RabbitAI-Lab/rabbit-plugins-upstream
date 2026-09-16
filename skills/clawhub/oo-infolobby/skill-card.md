## Description:

InfoLobby helps an agent read, create, update, delete, count, and query InfoLobby records through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate InfoLobby workspaces and tables through a connected OOMOL account, including record reads, queries, creates, updates, deletes, counts, and metadata lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could run arbitrary code on a user's machine.

Mitigation: Review the oo CLI installation path before installing, prefer an official versioned installer or package-manager method with checksum or signature verification, and avoid running installer commands without user approval.

Risk: Write and destructive InfoLobby actions can modify or remove records in the connected account.

Mitigation: Confirm the exact action payload, target record or table, and expected effect with the user before running create, update, or delete actions.

## Reference(s):

- [InfoLobby homepage](https://infolobby.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-infolobby)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live action schemas before constructing InfoLobby connector requests.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

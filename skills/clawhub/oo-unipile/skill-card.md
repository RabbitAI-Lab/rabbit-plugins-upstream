## Description:

Uses OOMOL's oo CLI to search and read Unipile accounts, chats, and messages through a connected Unipile account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Unipile account, chat, and message data through the OOMOL-connected oo CLI. The skill guides agents to inspect live action schemas before constructing JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Use an official pinned or manually reviewed installation path, avoid elevated shells, and run setup commands only after an authentication or connection failure requires them.

Risk: Future or unlisted Unipile actions may be state-changing even though the currently listed actions are read-oriented.

Mitigation: Inspect the live action schema and confirm any state-changing payload and effect with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-unipile)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [Unipile Homepage](https://www.unipile.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-connected credentials and recommends live action schema inspection before payload construction.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Businessmap helps agents read, create, update, and delete Businessmap workspaces, boards, and cards through an OOMOL-connected Businessmap account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Businessmap boards and cards through the OOMOL `oo` CLI. It is suited for agents that need to inspect Businessmap action schemas, run read operations, and prepare confirmed write or delete requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded code directly into a shell.

Mitigation: Install the oo CLI through a verifiable package, pinned release, checksum, or signed installer instead of piping a remote script directly into a shell.

Risk: Connected Businessmap permissions can allow write or destructive changes to boards and cards.

Mitigation: Review each write or delete payload, confirm the exact target and effect with the user, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Businessmap skill page](https://clawhub.ai/oomol/skills/oo-businessmap)
- [Businessmap homepage](https://businessmap.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live Businessmap action schemas before constructing requests; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

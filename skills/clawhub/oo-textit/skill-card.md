## Description:

TextIt enables an agent to read, create, update, delete, and send TextIt workspace, contact, group, message, and broadcast data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to operate TextIt through an OOMOL-connected account. It supports TextIt workspace inspection, contact and group management, message and broadcast listing, and sending individual messages or broadcasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes installer commands downloaded from the internet.

Mitigation: Verify the OOMOL CLI installer source independently before running pasted installer commands.

Risk: Write and destructive actions can send messages or change TextIt contacts, groups, and broadcasts.

Mitigation: Require clear user approval for each send, update, or delete action, including the exact target and payload.

Risk: TextIt access depends on the OOMOL CLI and the user's connected TextIt account.

Mitigation: Confirm that the user trusts the OOMOL CLI and TextIt connection path before installation or account connection.

## Reference(s):

- [TextIt Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-textit)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [TextIt Homepage](https://textit.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or modify TextIt resources; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

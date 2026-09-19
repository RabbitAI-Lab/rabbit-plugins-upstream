## Description:

Operate Quo (OpenPhone) through OOMOL's oo CLI for reading, creating, updating, and deleting contacts and related workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage contacts, messages, phone numbers, and users in a connected Quo (OpenPhone) workspace through OOMOL's oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts executed directly by a shell.

Mitigation: Review and use official, versioned, verifiable oo CLI installation steps instead of piping installer output directly into a shell.

Risk: The skill operates Quo/OpenPhone through OOMOL as a broker for workspace data.

Mitigation: Install only when the user accepts OOMOL handling Quo/OpenPhone access and data for the requested workspace.

Risk: Write and destructive actions can send messages, update contacts, or delete contacts.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before running message-send, update, or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Quo homepage](https://www.quo.com)
- [Quo icon](https://static.oomol.com/logo/third-party/quo.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger read, write, and destructive Quo actions through the oo CLI; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: artifact metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

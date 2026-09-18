## Description:

Magileads helps an agent inspect schemas and read, create, update, or delete Magileads contact lists through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents connected to an OOMOL account use this skill to manage Magileads contact lists, including listing, retrieving, creating, updating, and deleting contact-list records after checking live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct execution of remote oo CLI installer scripts.

Mitigation: Install the oo CLI through a verified package when possible, or inspect a pinned installer and verify its checksum or signature before execution.

Risk: Write and destructive actions can change or delete Magileads contact-list data.

Mitigation: Confirm the exact payload, target identifier, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Magileads skill page](https://clawhub.ai/oomol/skills/oo-magileads)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Magileads homepage](https://www.magileads.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

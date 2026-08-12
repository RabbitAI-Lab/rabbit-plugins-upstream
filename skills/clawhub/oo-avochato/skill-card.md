## Description:

Avochato lets an agent read, create, and update Avochato contacts and messages through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Customer support and operations teams use this skill to retrieve Avochato contacts and messages and, after confirmation, send messages or create and update contacts through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Avochato contact and message data can contain sensitive customer communications.

Mitigation: Install this skill only when agent access to the connected Avochato account is intended, and limit returned contact or message details to the user's requested task.

Risk: The send_message and upsert_contact actions can change Avochato state or contact external recipients.

Mitigation: Review the exact payload and expected effect with the user before approving send_message or upsert_contact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-avochato)
- [Avochato homepage](https://www.avochato.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell commands and JSON action results or summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

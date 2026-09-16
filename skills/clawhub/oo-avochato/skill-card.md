## Description:

Avochato (avochato.com) supports Avochato requests such as reading, creating, and updating contact and message data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Avochato contacts and messages through an OOMOL-connected account, including listing contacts and messages, retrieving records, sending text messages, and upserting contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup steps can execute remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a verified, versioned, manually reviewed process and avoid elevated shells unless strictly required.

Risk: Write actions can send messages or create and update Avochato contacts.

Mitigation: Confirm the exact payload and expected effect with the user before running message sends or contact upserts.

Risk: Connector calls depend on live action schemas and OOMOL-managed credentials.

Mitigation: Inspect the current connector schema before constructing payloads and require a connected, trusted OOMOL account.

## Reference(s):

- [Avochato homepage](https://www.avochato.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-avochato)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that inspect connector schemas and run Avochato connector actions.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

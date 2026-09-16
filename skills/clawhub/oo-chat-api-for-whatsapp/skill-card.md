## Description:

Chat API for WhatsApp enables agents to inspect Chat API settings, status, chats, messages, outbound queues, and send WhatsApp text messages or files through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to read Chat API for WhatsApp account state and perform supported messaging actions through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes one-line remote installer commands for the oo CLI.

Mitigation: Do not let an agent run the installers automatically; install the oo CLI through a verified, versioned, or otherwise trusted method.

Risk: Chat API request and response data passes through OOMOL's connector infrastructure.

Mitigation: Review the connector's data handling expectations, connected account permissions, and acceptable data categories before use.

Risk: Write actions can send text messages or files to WhatsApp chats or phone numbers.

Mitigation: Confirm the exact payload and intended effect with the user before running any write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-chat-api-for-whatsapp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Chat API for WhatsApp Homepage](https://chat-api.com/en/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

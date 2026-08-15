## Description:

Chat API for WhatsApp helps agents inspect Chat API instance data and run approved message or file send actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read Chat API for WhatsApp settings, status, chats, messages, and queues, and to send text or file messages after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read chats and messages from the connected Chat API for WhatsApp instance.

Mitigation: Connect only an OOMOL account and Chat API instance that the agent is intended to access.

Risk: Write actions can send text messages or files through the connected instance.

Mitigation: Confirm the exact target, payload, and effect with the user before running any write action.

## Reference(s):

- [Chat API for WhatsApp homepage](https://chat-api.com/en/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chat-api-for-whatsapp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when actions are run with the oo CLI --json flag.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

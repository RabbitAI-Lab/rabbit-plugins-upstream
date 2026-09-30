## Description:

Helps agents read, send, search, and organize Zoho Mail through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with Zoho Mail can retrieve and search messages, send replies, and manage folders and labels. With separate approval, they can set up Maton-hosted automations using a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Maton grants access to the authorized Zoho Mail account.

Mitigation: Get approval before connecting, prefer device OAuth, grant only needed scopes, and remove unused connections.

Risk: Sending, changing, or deleting mail can affect recipients and account data.

Mitigation: Default to reads and confirm the target and effect of every write before proceeding.

Risk: Automations and trigger destinations may forward matching events persistently.

Mitigation: Obtain separate approval, narrowly scope destinations, and remove them when no longer needed.

Risk: A long-lived API key or untrusted event content could expose credentials or trigger unsafe actions.

Mitigation: Prefer device OAuth, keep keys out of outputs, and run local event handlers only after separate review and approval.

## Reference(s):

- [ClawHub Zoho Mail release](https://clawhub.ai/byungkyu/skills/zoho-mail)
- [Maton homepage](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Zoho Mail API overview](https://www.zoho.com/mail/help/api/overview.html)
- [Zoho Mail email API](https://www.zoho.com/mail/help/api/email-api.html)
- [Time trigger catalog](references/time/triggers.md)
- [Google Mail trigger catalog](references/google-mail/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown guidance with commands, code examples, and API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain private email content; share only the fields needed for the task.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

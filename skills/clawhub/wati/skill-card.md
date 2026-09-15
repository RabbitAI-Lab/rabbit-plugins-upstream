## Description:

WATI (WhatsApp Team Inbox) API integration with managed authentication for sending WhatsApp messages, managing contacts, and handling templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to connect an authorized WATI account through Maton, inspect contacts, messages, and templates, and perform approved WhatsApp business actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on sensitive WhatsApp business data through the user's WATI connection.

Mitigation: Use OAuth where possible, connect only the intended WATI account, specify the intended connection when more than one exists, and avoid raw API keys unless the CLI cannot be used.

Risk: Send, update, delete, connection, hosted function, and trigger actions can create side effects or run later with the deploying account's authority.

Mitigation: Confirm every send, update, delete, new connection, hosted function, and trigger action with the user after showing the target resource, payload, intended effect, and persistence.

Risk: Returned API data, uploaded files, and CSV contact lists can contain personal or business-sensitive information.

Mitigation: Read or transmit only user-named data, extract the minimum fields needed, avoid dumping raw responses into logs or files, and confirm exact files, recipients, row counts, and templates before upload or send operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/wati)
- [Maton homepage](https://maton.ai)
- [WATI API Documentation](https://docs.wati.io/reference/introduction)
- [WATI Help Center](https://docs.wati.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated Maton/WATI requests and asks for confirmation before writes, new connections, hosted functions, triggers, or destructive operations.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

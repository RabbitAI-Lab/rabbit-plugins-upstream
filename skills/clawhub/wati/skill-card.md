## Description:

WATI (WhatsApp Team Inbox) API integration with managed authentication for sending WhatsApp messages, managing contacts, and handling templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operations teams use this skill to access WATI through Maton-managed authentication for approved WhatsApp messaging, contact management, template work, and related automation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send real WhatsApp messages or modify contacts in a WATI business account.

Mitigation: Default to read and list operations, then confirm the target resource, payload, and intended effect before any write or bulk send.

Risk: Actions can affect the wrong WATI or Maton account when multiple connections or profiles exist.

Mitigation: Pin the intended connection or profile before acting and verify account context before writes.

Risk: Long-lived credentials or API keys can be exposed if copied into logs, files, commands, or destination templates.

Mitigation: Use OAuth where possible, avoid printing or persisting credentials, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: Functions, triggers, and destinations can create ongoing automation or persistent data forwarding.

Mitigation: Create them only after explicit user approval and disclose the destination, payload fields, schedule or event source, and persistence.

## Reference(s):

- [ClawHub WATI skill page](https://clawhub.ai/byungkyu/skills/wati)
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

**Output Format:** [Markdown guidance with inline shell, JSON, Python, JavaScript, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated API call patterns, connection setup guidance, and safety checks for WATI actions.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

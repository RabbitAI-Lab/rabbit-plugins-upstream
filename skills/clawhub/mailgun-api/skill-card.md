## Description:

Mailgun API integration with managed OAuth for sending, receiving, and tracking email and for managing domains, routes, templates, mailing lists, suppressions, webhooks, and related automation through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to work with Mailgun through managed OAuth, starting with read and list calls and using explicit user confirmation for writes, new connections, webhooks, hosted functions, and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send email, create webhooks or routes, change tracking, create SMTP credentials, and enable automations that keep running after setup.

Mitigation: Review each proposed write carefully and require explicit user confirmation before any write, new connection, hosted function, trigger, or persistent forwarding change.

Risk: Mailgun responses and trigger payloads can include personal data, message content, contact details, credentials, or business-sensitive information.

Mitigation: Prefer read and list calls first, extract only fields needed for the task, avoid logging raw responses, and use trigger body templates to forward the minimum necessary data.

Risk: Using raw HTTP instead of the Maton CLI exposes a long-lived Maton API key in the process environment.

Mitigation: Use raw HTTP only when the CLI cannot be installed, never print or persist the key, send it only to api.maton.ai, and rotate it if it was exposed.

Risk: Mailgun has US and EU regions, while the documented gateway defaults to the US region.

Mitigation: Confirm the intended Mailgun region and data residency expectations before processing regulated or region-sensitive email data.

## Reference(s):

- [Mailgun API Documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)
- [Mailgun API Reference](https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/intro/)
- [Mailgun Postman Collection](https://www.postman.com/mailgun/mailgun-s-public-workspace/documentation/ik8dl61/mailgun-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Mailgun Skill](https://clawhub.ai/byungkyu/skills/mailgun-api)
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

**Output Format:** [Markdown with inline shell commands, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-authorized Mailgun connection; write operations and new connections require explicit user confirmation.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

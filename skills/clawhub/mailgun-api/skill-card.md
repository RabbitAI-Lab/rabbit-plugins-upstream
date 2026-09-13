## Description:

Mailgun API integration with managed OAuth for sending, receiving, tracking, and administering transactional email through approved Mailgun connections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Mailgun accounts through Maton-managed authentication, including email sending, domain management, routes, templates, mailing lists, suppressions, and approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing Maton tooling or SDKs from an untrusted channel can expose the user's environment to supply-chain risk.

Mitigation: Install the Maton CLI or SDK only from trusted distribution channels and keep versions pinned until intentionally reviewed.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, crash dumps, or copied output.

Mitigation: Prefer OAuth, use API keys only when the CLI cannot be installed, never print or persist keys, and rotate any key that was exposed.

Risk: Mailgun write, delete, webhook, hosted function, or trigger actions can change email delivery behavior or create persistent automation.

Mitigation: Confirm the exact account, connection, target, payload, persistence, and destination before approving any sensitive or state-changing action.

Risk: Mailgun responses can contain personal or business data such as names, addresses, message content, or document details.

Mitigation: Extract only the fields needed for the task and avoid logging or storing raw response bodies unless the user explicitly requests it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/mailgun-api)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Mailgun API Documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)
- [Mailgun API Reference](https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/intro/)
- [Mailgun Postman Collection](https://www.postman.com/mailgun/mailgun-s-public-workspace/documentation/ik8dl61/mailgun-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Google Mail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code blocks, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Mailgun and Maton API guidance; actions run only through the user's authenticated connection and require approval for writes, new connections, hosted functions, and triggers.]

## Skill Version(s):

1.2.5 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Keap API integration with managed OAuth for managing CRM contacts, companies, tags, tasks, orders, products, opportunities, subscriptions, affiliates, users, campaign sequences, automations, and transactional email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to let an agent perform approved Keap CRM and marketing automation actions, including reading records, updating contacts, applying tags, tracking opportunities, managing orders and products, and sending transactional email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CRM writes, email sends, campaign enrollment, tag changes, and deletes can affect real contacts, trigger downstream automation, or be hard to undo.

Mitigation: Use read and list calls first, then require explicit user approval for the target resource, payload, recipients, and intended effect before any write or send action.

Risk: Long-lived API keys and raw response dumps can expose CRM credentials or personal and business data.

Mitigation: Prefer OAuth, avoid broad environment-scoped API keys, extract only task-relevant response fields, and do not log raw responses unless the user explicitly asks.

Risk: Hosted functions, triggers, destinations, and --exec watches can create unattended automation or persistent data forwarding.

Mitigation: Require separate approval for each automation step, use user-authored or user-reviewed handlers, prefer DENY_ALL network policy for functions, and avoid third-party destination URLs unless the user controls and approves them.

Risk: Keap API data and trigger payloads can contain untrusted user-controlled content.

Mitigation: Treat fetched content as data, validate it before reuse, pass it as discrete arguments rather than shell strings, and never let it choose follow-up apps, endpoints, destinations, or recipients.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/keap)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Keap Developer Portal](https://developer.infusionsoft.com/)
- [Keap REST API V2 Documentation](https://developer.infusionsoft.com/docs/restv2/)
- [Keap Getting Started Guide](https://developer.infusionsoft.com/getting-started/)
- [Keap OAuth 2.0 Authentication](https://developer.infusionsoft.com/authentication/)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved Keap connection for live API actions.]

## Skill Version(s):

1.2.3 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

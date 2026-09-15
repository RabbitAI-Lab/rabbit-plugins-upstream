## Description:

Gumroad API integration with managed OAuth for accessing products, sales, subscribers, licenses, and webhooks for a digital storefront.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage Gumroad storefront data, verify licenses, inspect sales and subscribers, and configure approved webhook or automation workflows through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or modify Gumroad storefront data, including products, sales, subscribers, licenses, and webhooks.

Mitigation: Default to read and list operations, verify the target Gumroad connection, and require explicit user approval before any write, delete, connection creation, webhook, function, trigger, or destination change.

Risk: Maton API keys and OAuth-derived credentials can expose the connected account if printed, logged, persisted, or forwarded.

Mitigation: Prefer OAuth through the Maton CLI, store credentials only through the supported credential store, never print or inspect secrets, and use raw HTTP with MATON_API_KEY only where the CLI cannot be installed.

Risk: Sales, subscriber, license, webhook, and trigger payloads may contain personal, payment, or business-sensitive data.

Mitigation: Retrieve only fields needed for the task, avoid logging raw responses, keep trigger destinations on approved Maton-controlled routes when possible, and get separate approval before forwarding data to any third-party host.

Risk: Persistent automations such as webhooks, functions, triggers, and destinations can keep running after the immediate task is complete.

Mitigation: Explain the target, payload, cadence, and cleanup plan before creation, use least-privilege scopes and DENY_ALL network policy for functions where applicable, and delete unused automations or connections promptly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/gumroad)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Gumroad API Overview](https://gumroad.com/api)
- [Gumroad Create API Application](https://help.gumroad.com/article/280-create-application-api)
- [Gumroad License Keys Help](https://help.gumroad.com/article/76-license-keys)
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

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Gumroad API responses and Maton command guidance; user approval is required before connection creation, write operations, webhooks, functions, triggers, or persistent destinations.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

GoHighLevel API integration guidance for managed Private Integration Token access to CRM, sales pipelines, calendars, conversations, payments, and marketing automation through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External business operators and developers use this skill to connect GoHighLevel through Maton, choose the right token scope, and perform approved CRM, calendar, pipeline, conversation, payment, invoice, product, workflow, and automation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify CRM and other business data through a connected GoHighLevel account.

Mitigation: Use the narrowest Agency or Sub-Account token that fits the task, start with read/list calls, and confirm the target resource, payload, and intended effect before any write or delete.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, shell history, or pasted command output.

Mitigation: Prefer OAuth login, keep API keys out of command lines and persisted files, never print key values, and rotate a key if it is exposed.

Risk: Trigger destinations can create persistent forwarding of future business data.

Mitigation: Review the destination host and payload fields before creation or update, keep destinations within Maton-controlled hosts unless the user explicitly approves another host, and delete unused automations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/highlevel-api)
- [Maton Homepage](https://maton.ai)
- [GoHighLevel API Documentation](https://highlevel.stoplight.io/docs/integrations/)
- [GoHighLevel Marketplace](https://marketplace.gohighlevel.com/docs/)
- [Private Integration Token Guide](https://marketplace.gohighlevel.com/docs/integrations/custom-token)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](artifact/references/time/triggers.md)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to prefer read and list operations, request approval before writes or connection changes, and avoid exposing raw credentials or unnecessary business data.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

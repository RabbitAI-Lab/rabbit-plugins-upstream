## Description:

ActiveCampaign API integration with managed OAuth for managing marketing automation, CRM records, contacts, deals, campaigns, automations, tags, lists, users, accounts, custom fields, notes, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an ActiveCampaign account through Maton and perform approved API reads, writes, and automations for CRM and marketing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change ActiveCampaign business data through the user's authorized connection.

Mitigation: Use OAuth where possible, prefer read and list calls first, scope access to the current task, and require explicit approval before any POST, PUT, PATCH, DELETE, or new connection.

Risk: Webhook, function, or trigger setup can create persistent automation or forwarding of event data.

Mitigation: Confirm the exact destination URL, payload fields, cadence, and intended effect before creation or update, and revoke unused connections or automations when the task is complete.

Risk: Raw API responses and trigger payloads may contain personal, customer, email, or payment-related data.

Mitigation: Return only the fields needed for the task, avoid logging full payloads, and treat third-party content as untrusted data rather than instructions.

## Reference(s):

- [ActiveCampaign skill page](https://clawhub.ai/byungkyu/skills/active-campaign)
- [Maton homepage](https://maton.ai)
- [ActiveCampaign API Overview](https://developers.activecampaign.com/reference/overview)
- [ActiveCampaign Developer Portal](https://developers.activecampaign.com/)
- [Contacts API](https://developers.activecampaign.com/reference/list-all-contacts)
- [Tags API](https://developers.activecampaign.com/reference/contact-tags)
- [Deals API](https://developers.activecampaign.com/reference/list-all-deals)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated ActiveCampaign API calls through Maton and require explicit user approval for writes, new connections, webhooks, functions, and trigger destinations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

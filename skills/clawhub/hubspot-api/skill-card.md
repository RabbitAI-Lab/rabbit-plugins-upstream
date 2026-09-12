## Description:

HubSpot API integration with managed OAuth for CRM contacts, companies, deals, associations, and properties, with read-first guidance and explicit approval for writes, connections, triggers, destinations, and hosted functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with HubSpot CRM records through Maton-managed OAuth: listing, searching, creating, updating, and synchronizing contacts, companies, deals, associations, and properties. Scheduled or event-driven automation is available only when the user asks for it and approves the relevant connection, trigger, destination, or hosted function.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent functions, triggers, and destinations can continue acting under the Maton account after setup.

Mitigation: Create them only after explicit user approval, keep function networking at DENY_ALL for HubSpot tasks, and delete unused automation when the task is complete.

Risk: HubSpot CRM records and event payloads can contain customer personal data.

Mitigation: Default to read/list calls, confirm every write, minimize forwarded fields with body templates, and keep destinations on api.maton.ai or *.maton.app unless the user names and approves a third-party host.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is unavoidable, read the key from the environment, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [ClawHub HubSpot Skill Page](https://clawhub.ai/byungkyu/skills/hubspot-api)
- [Maton Homepage](https://maton.ai)
- [HubSpot API Overview](https://developers.hubspot.com/docs/api/overview)
- [HubSpot CRM Search Reference](https://developers.hubspot.com/docs/api/crm/search)
- [HubSpot Contact List API](https://developers.hubspot.com/docs/api-reference/crm-contacts-v3/basic/get-crm-v3-objects-contacts.md)
- [HubSpot Contact Create API](https://developers.hubspot.com/docs/api-reference/crm-contacts-v3/basic/post-crm-v3-objects-contacts.md)
- [HubSpot Companies API](https://developers.hubspot.com/docs/api-reference/crm-companies-v3/basic/get-crm-v3-objects-companies.md)
- [HubSpot Deals API](https://developers.hubspot.com/docs/api-reference/crm-deals-v3/basic/get-crm-v3-objects-0-3.md)
- [HubSpot Associations API](https://developers.hubspot.com/docs/api-reference/crm-associations-v4/basic/get-crm-v4-objects-objectType-objectId-associations-toObjectType.md)
- [HubSpot Properties API](https://developers.hubspot.com/docs/api-reference/crm-properties-v3/core/get-crm-v3-properties-objectType.md)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands, API paths, JSON examples, and optional code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can instruct an agent to make authenticated Maton CLI or HTTPS requests and to configure persistent triggers, destinations, or hosted functions when explicitly approved by the user.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

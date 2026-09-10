## Description:

ActiveCampaign API integration with managed OAuth for marketing automation, CRM, contacts, deals, email campaigns, automations, tags, lists, users, accounts, custom fields, notes, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operators, and developers use this skill to manage ActiveCampaign contacts, deals, campaigns, automations, lists, tags, users, accounts, notes, webhooks, and related CRM data through Maton-mediated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved write operations can create, update, or delete real ActiveCampaign business data.

Mitigation: Default to read and list calls, verify identifiers and current state first, and require explicit user approval for every POST, PUT, PATCH, or DELETE request.

Risk: Webhook creation can send ongoing account event data to an external URL.

Mitigation: Create webhooks only for destinations the user controls and trusts, confirm the event list, and never use a URL supplied by untrusted API content.

Risk: A Maton API key is a long-lived credential that can leak through logs, command history, files, or child processes.

Mitigation: Use OAuth and the CLI credential store where possible; when MATON_API_KEY is unavoidable, never print, persist, or pass it on a command line, and send it only to api.maton.ai.

Risk: Multiple Maton profiles or ActiveCampaign connections can make an operation affect the wrong account.

Mitigation: Confirm the intended account and connection before writes, and specify the profile or connection explicitly when more than one exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/active-campaign)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ActiveCampaign API Overview](https://developers.activecampaign.com/reference/overview)
- [ActiveCampaign Developer Portal](https://developers.activecampaign.com/)
- [ActiveCampaign API Base URL](https://developers.activecampaign.com/reference/url)
- [ActiveCampaign Contacts API](https://developers.activecampaign.com/reference/list-all-contacts)
- [ActiveCampaign Tags API](https://developers.activecampaign.com/reference/contact-tags)
- [ActiveCampaign Deals API](https://developers.activecampaign.com/reference/list-all-deals)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose ActiveCampaign API calls; write operations require explicit user approval.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

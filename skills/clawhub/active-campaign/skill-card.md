## Description:

ActiveCampaign API integration with managed OAuth for managing contacts, deals, tags, lists, automations, campaigns, CRM records, custom fields, notes, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to read and manage ActiveCampaign marketing automation and CRM resources through Maton-authenticated API calls, with explicit approval before writes, webhooks, connections, hosted functions, or triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations, user or account management, and connection changes can affect shared ActiveCampaign resources.

Mitigation: Confirm the exact account, connection, resource IDs, payload, and intended operation with the user before approving any write, delete, or connection action.

Risk: Webhook, trigger, or hosted function workflows may send account event data to a destination or run persistently after setup.

Mitigation: Verify the destination URL, receiving system owner, function code, connection scope, network policy, and persistence before creation; remove automation when the task is finished.

Risk: API-key authentication can expose a long-lived credential if handled through environment variables or raw HTTP.

Mitigation: Prefer OAuth and the operating system credential store; use raw HTTP only where the CLI cannot be installed and avoid logging or storing raw responses and credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/active-campaign)
- [Maton Homepage](https://maton.ai)
- [ActiveCampaign API Overview](https://developers.activecampaign.com/reference/overview)
- [ActiveCampaign Developer Portal](https://developers.activecampaign.com/)
- [Contacts API](https://developers.activecampaign.com/reference/list-all-contacts)
- [Tags API](https://developers.activecampaign.com/reference/contact-tags)
- [Deals API](https://developers.activecampaign.com/reference/list-all-deals)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated ActiveCampaign API calls through Maton and require user approval before write, webhook, connection, hosted function, or trigger operations.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

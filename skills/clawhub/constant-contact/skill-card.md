## Description:

Constant Contact API integration with managed OAuth for reading and managing contacts, email campaigns, lists, tags, custom fields, segments, bulk operations, and marketing analytics through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to administer Constant Contact marketing data through managed OAuth, including contacts, campaigns, lists, tags, custom fields, segments, bulk activities, and analytics. It is intended for read/list operations by default, with explicit user approval before writes, new connections, campaign sends, scheduling, imports, exports, or bulk changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, send, schedule, import, export, and bulk-modify Constant Contact resources.

Mitigation: Default to read/list operations, retrieve the target first, summarize the intended change and consequences, and require explicit confirmation with specific identifiers before any write or bulk action.

Risk: Campaign sends and schedules can reach external recipients and may be irreversible once executed.

Mitigation: Preview the campaign and confirm recipients, subject, sender, content, and schedule with the user before sending or scheduling.

Risk: Long-lived Maton API keys and provider-issued credentials can leak through logs, shell history, files, or command lines.

Mitigation: Prefer OAuth, let the CLI or credential store handle secrets, never print or persist credential values, and send API keys only to api.maton.ai when raw HTTP is unavoidable.

Risk: Constant Contact responses may contain personal data such as names, email addresses, phone numbers, campaign content, and analytics.

Mitigation: Return only fields needed for the task and avoid writing raw response bodies to logs or files unless the user explicitly requests it.

Risk: The Maton API passthrough can reach endpoints beyond the documented examples if the connection is authorized for them.

Mitigation: Treat documented endpoints as the intended surface, verify account and connection context, use least-privilege scopes, and apply the same approval rules to every POST, PUT, PATCH, or DELETE request.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/constant-contact)
- [Maton Homepage](https://maton.ai)
- [Constant Contact V3 API Overview](https://developer.constantcontact.com/api_guide/getting_started.html)
- [Constant Contact API Reference](https://developer.constantcontact.com/api_reference/index.html)
- [Constant Contact Technical Overview](https://developer.constantcontact.com/api_guide/v3_technical_overview.html)
- [Constant Contact Contacts Overview](https://developer.constantcontact.com/api_guide/contacts_overview.html)
- [Constant Contact Email Campaigns Guide](https://developer.constantcontact.com/api_guide/email_campaigns_get_started.html)
- [Constant Contact Contact Lists Overview](https://v3.developer.constantcontact.com/api_guide/lists_overview.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces proposed API operations for the user's review; write-capable operations require explicit user approval before execution.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

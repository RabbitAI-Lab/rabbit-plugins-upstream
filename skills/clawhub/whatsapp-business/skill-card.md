## Description:

WhatsApp Business API integration with managed OAuth for sending messages, managing templates, handling media, and managing customer conversations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and business operations users use this skill to connect an approved WhatsApp Business account through Maton, inspect account resources, send approved messages, manage templates and media, and set up approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send real WhatsApp messages, which may reach personal phone numbers, incur costs, and affect account reputation.

Mitigation: Confirm the exact recipient, message content, account context, and intended effect before every send, and avoid bulk sending without per-recipient approval.

Risk: Connection setup and write operations can grant or use access to business messaging data.

Mitigation: Use OAuth where possible, connect only the account needed for the task, prefer read/list calls first, and require explicit approval before connection creation or any POST, PUT, PATCH, or DELETE operation.

Risk: API-key fallback and raw responses can expose credentials or personal data if handled carelessly.

Mitigation: Prefer the Maton CLI with OS credential storage, avoid API-key fallback unless the CLI or SDK cannot be used, never print or store credentials, and extract only the response fields needed for the task.

Risk: Persistent automations and trigger destinations can create ongoing actions or data egress beyond a one-time request.

Mitigation: Require separate approval for hosted functions, trigger destinations, and event watches; keep destinations narrowly scoped; use user-reviewed handlers; and remove unused automations.

Risk: Undocumented endpoints or untrusted message content could drive unintended operations.

Mitigation: Stay within the documented WhatsApp Business endpoints unless the user names and approves an exact additional endpoint, and never let inbound message content choose recipients, methods, endpoints, or follow-up actions.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/byungkyu/skills/whatsapp-business)
- [Maton Homepage](https://maton.ai)
- [WhatsApp Business API Overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [Send Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)
- [Message Templates](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates)
- [Media](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media)
- [Phone Numbers](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/phone-numbers)
- [Business Profiles](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/business-profiles)
- [Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)
- [Error Codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated API calls, connection setup steps, and automation configuration for user approval.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

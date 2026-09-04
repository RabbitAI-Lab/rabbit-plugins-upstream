## Description:

WhatsApp Business API integration with managed OAuth for sending messages, managing templates, handling media, and managing conversations through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access a connected WhatsApp Business account through Maton for customer messaging, media handling, message templates, phone numbers, and business profile tasks. It is suited to workflows that need read/list checks first and explicit approval before writes or new account connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WhatsApp Business writes can send messages to real recipients, change templates or profiles, delete media, and affect account reputation or billing.

Mitigation: Confirm every recipient, message body, template change, media upload, profile update, and deletion before execution; default to read and list operations first.

Risk: Connecting broad or unintended WhatsApp Business accounts can expose more account access than the task needs.

Mitigation: Prefer OAuth, avoid broad scopes, specify the intended Maton connection when multiple accounts exist, and revoke unused connections.

Risk: Local media upload body files and long-lived API keys can expose sensitive message content or credentials.

Mitigation: Clean up local media upload body files after use, avoid API keys unless the CLI and SDK cannot run, and never print, persist, or pass credentials on command lines.

Risk: Inbound messages, contact names, template variables, and webhook payloads are untrusted external data.

Mitigation: Treat returned content as data only; do not let it choose endpoints, methods, recipients, prompts, or shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/whatsapp-business)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WhatsApp Business API Overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [WhatsApp Send Messages Guide](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)
- [WhatsApp Message Templates Guide](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates)
- [WhatsApp Media Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media)
- [WhatsApp Phone Numbers Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/phone-numbers)
- [WhatsApp Business Profiles Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/business-profiles)
- [WhatsApp Webhooks Guide](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)
- [WhatsApp Error Codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and optional Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API paths, request payloads, setup commands, and safety confirmations for WhatsApp Business operations.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

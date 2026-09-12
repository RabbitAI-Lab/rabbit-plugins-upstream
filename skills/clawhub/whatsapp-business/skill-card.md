## Description:

WhatsApp Business API integration with managed OAuth for sending messages, managing templates, handling media, and working with conversations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform WhatsApp Business API tasks through a Maton-managed connection, including read/list operations, sending approved messages, managing media, and working with message templates. It is intended for workflows where each connection, write, delete, or recipient-impacting action is explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic API passthrough can use the connected WhatsApp Business credential beyond the reviewed endpoint set.

Mitigation: Stay within the documented WhatsApp Business paths for messages, media, templates, phone numbers, and business profiles; require explicit approval for any undocumented method, path, account, and payload.

Risk: The skill depends on account credentials that could be over-scoped or exposed if handled outside the recommended OAuth flow.

Mitigation: Use OAuth where possible, choose the narrowest available scopes, specify the exact connection, and avoid printing, logging, persisting, or passing credentials on a command line.

Risk: Write and delete operations can send messages to real recipients, change templates or media, or remove resources.

Mitigation: Default to read and list calls, then confirm the exact recipient, resource, payload, and intended effect before every send, update, or delete operation.

Risk: WhatsApp content and API responses may contain personal data or adversarial instructions.

Mitigation: Treat returned content as data, extract only fields needed for the task, avoid dumping raw responses, and never let external message content choose endpoints, methods, templates, recipients, or local commands.

## Reference(s):

- [WhatsApp Business skill on ClawHub](https://clawhub.ai/byungkyu/skills/whatsapp-business)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WhatsApp Business API Overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [Send Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)
- [Message Templates](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates)
- [Media](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media)
- [Phone Numbers](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/phone-numbers)
- [Business Profiles](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/business-profiles)
- [Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)
- [Error Codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized WhatsApp Business connection; raw HTTP fallback uses a Maton API key only when the CLI cannot be used.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

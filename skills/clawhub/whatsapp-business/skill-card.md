## Description:

WhatsApp Business API integration with managed OAuth for sending messages, managing templates, handling media, and working with conversations through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent access a connected WhatsApp Business account through Maton for message, template, media, phone-number, and business-profile workflows. The skill is most appropriate when a user explicitly wants WhatsApp Business API actions and can review writes before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send real WhatsApp messages and change account resources.

Mitigation: Review each send, delete, template, media, or profile update before approving it.

Risk: A write can affect the wrong WhatsApp Business account when multiple connections exist.

Mitigation: Specify the intended connection before executing account-specific actions.

Risk: Long-lived API keys can be exposed more easily than OAuth-managed credentials.

Mitigation: Prefer OAuth over API keys and avoid printing, logging, or persisting credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/whatsapp-business)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WhatsApp Business API Overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [WhatsApp Send Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)
- [WhatsApp Message Templates](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates)
- [WhatsApp Media Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media)
- [WhatsApp Phone Numbers Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/phone-numbers)
- [WhatsApp Business Profiles Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/business-profiles)
- [WhatsApp Webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks)
- [WhatsApp Error Codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that call the Maton CLI and JSON payloads for WhatsApp Business API requests.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter says 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

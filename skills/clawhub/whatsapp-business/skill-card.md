## Description:

WhatsApp Business API integration with managed OAuth for sending messages, managing templates, handling media, and working with conversations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access WhatsApp Business from an agent through the Maton CLI or gateway. It supports customer messaging, template management, media handling, phone-number lookup, and business-profile operations while requiring confirmation for writes and new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send real WhatsApp messages to personal phone numbers, which may create cost, privacy, and account-reputation impact.

Mitigation: Review the exact recipient, message text, template, and intended effect with the user before any send or other write operation.

Risk: The skill depends on the Maton gateway, CLI, and package sources for WhatsApp Business access.

Mitigation: Confirm that Maton and the installation sources are trusted before installing or authenticating.

Risk: Using the raw HTTP fallback requires a long-lived Maton API key that can leak through logs, shell history, child processes, or pasted output.

Mitigation: Prefer OAuth through the CLI or SDK; if an API key is unavoidable, do not print, log, persist, or pass it on a command line, and rotate it if exposed.

Risk: The media-upload example writes to a fixed `/tmp/upload.body` path, which is unsuitable for sensitive files without hardening.

Mitigation: Use a secure temporary file with restrictive permissions and cleanup when handling sensitive media.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/whatsapp-business)
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

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request paths, command examples, payload templates, and confirmation guidance for write operations.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
